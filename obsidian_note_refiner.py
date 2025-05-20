#!/usr/bin/env python3
import os
import re
import sys
import glob
from pathlib import Path
import argparse
from datetime import datetime

def extract_frontmatter(content):
    """Extract frontmatter from markdown content"""
    pattern = r'^---\s*$(.*?)^---\s*$'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    
    if match:
        frontmatter = match.group(1)
        content_without_frontmatter = content[match.end():].strip()
        return frontmatter.strip(), content_without_frontmatter
    
    return "", content

def parse_frontmatter(frontmatter):
    """Parse frontmatter into a dictionary"""
    result = {}
    lines = frontmatter.split('\n')
    
    current_key = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if line is a key-value pair
        if ':' in line and not line.startswith('  - '):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            result[key] = value
            current_key = key
        # Check if line is a list item
        elif line.startswith('  - '):
            item = line[4:].strip()
            if current_key not in result:
                result[current_key] = []
            if isinstance(result[current_key], list):
                result[current_key].append(item)
            else:
                result[current_key] = [result[current_key], item]
                
    return result

def generate_title(content, max_length=25):
    """Generate a title from content, limited to 25 characters"""
    # Remove markdown symbols, URLs, and other non-text content
    clean_content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    clean_content = re.sub(r'\[.*?\]\(.*?\)', '', clean_content)
    clean_content = re.sub(r'```.*?```', '', clean_content, flags=re.DOTALL)
    clean_content = re.sub(r'#+ ', '', clean_content)
    clean_content = re.sub(r'[*_~`]', '', clean_content)
    
    # Get the first sentence or chunk of text
    first_chunk = clean_content.split('\n')[0].split('.')[0]
    
    # Truncate and clean
    title = first_chunk[:max_length]
    title = title.strip()
    
    # Remove trailing punctuation
    title = re.sub(r'[.,;:!?]$', '', title)
    
    return title

def extract_tags(content, num_tags=10):
    """Extract relevant tags from content"""
    # Common Japanese topics from the content
    common_topics = [
        "ビジネス", "投資", "テクノロジー", "暗号資産", "ブロックチェーン", 
        "NFT", "DeFi", "ウォレット", "スマートコントラクト", "イノベーション",
        "マーケティング", "組織", "プロジェクト管理", "起業", "資金調達",
        "戦略", "分析", "研究", "開発", "設計", "実装", "検証", "運用",
        "暗号技術", "分散型", "P2P", "トークン", "ネットワーク", "セキュリティ",
        "プライバシー", "規制", "法律", "ガバナンス", "コミュニティ", "エコシステム"
    ]
    
    # Extract potential tags based on content
    tags = []
    
    # Check if any common topics appear in the content
    for topic in common_topics:
        if topic.lower() in content.lower():
            tags.append(topic)
    
    # Extract potential technical terms using regex
    tech_terms = re.findall(r'\b[A-Z][a-zA-Z0-9]*(?:\s[A-Z][a-zA-Z0-9]*)*\b', content)
    for term in tech_terms:
        if term not in tags and len(term) > 2:
            tags.append(term)
    
    # Return limited number of tags
    return tags[:num_tags]

def find_existing_notes(content_dir):
    """Find all existing markdown files in the content directory"""
    md_files = glob.glob(f"{content_dir}/**/*.md", recursive=True)
    notes = {}
    
    for file_path in md_files:
        file_name = os.path.basename(file_path)
        note_name = os.path.splitext(file_name)[0]
        notes[note_name] = file_path
        
        # Also read the title from the frontmatter if available
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            frontmatter, _ = extract_frontmatter(content)
            if frontmatter:
                fm_dict = parse_frontmatter(frontmatter)
                if 'title' in fm_dict and fm_dict['title']:
                    title = fm_dict['title'].strip('"\'')
                    notes[title] = file_path
    
    return notes

def insert_links(content, existing_notes, content_dir):
    """Insert internal links and track new note suggestions"""
    modified_content = content
    added_links = {}
    new_notes = {}
    
    # Sort note names by length (descending) to prevent partial matches
    note_names = sorted(existing_notes.keys(), key=len, reverse=True)
    
    # Only process if there are fewer than 25 potential matches
    if len(note_names) > 25:
        return content, {}, note_names
    
    # Track already linked terms to avoid duplicates
    linked_terms = set()
    
    for note_name in note_names:
        # Skip if note has link_exclude: true
        note_path = existing_notes[note_name]
        with open(note_path, 'r', encoding='utf-8') as f:
            note_content = f.read()
            frontmatter, _ = extract_frontmatter(note_content)
            fm_dict = parse_frontmatter(frontmatter)
            if fm_dict.get('link_exclude') == 'true':
                continue
        
        # Skip if already linked or too short
        if note_name in linked_terms or len(note_name) < 3:
            continue
            
        # Create pattern that respects word boundaries and isn't already part of a link
        pattern = r'(?<!\[\[)(?<!\|)(?<!\w)\b' + re.escape(note_name) + r'\b(?!\]\])(?!\|)(?!\w)'
        
        # Find the first occurrence
        match = re.search(pattern, modified_content)
        if match:
            # Replace with link
            replacement = f"[[{note_name}]]"
            start, end = match.span()
            modified_content = modified_content[:start] + replacement + modified_content[end:]
            
            # Add to list of added links
            added_links[note_name] = "関連キーワード"
            linked_terms.add(note_name)
    
    # Check for potential new notes
    words = re.findall(r'\b\w+\b', modified_content)
    unique_words = set([w for w in words if len(w) > 3])
    
    for word in unique_words:
        if word not in existing_notes and word not in linked_terms and not any(word in note for note in note_names):
            # Add as a potential new note with special marker
            pattern = r'(?<!\[\[)(?<!\|)\b' + re.escape(word) + r'\b(?!\]\])(?!\|)'
            match = re.search(pattern, modified_content)
            if match:
                replacement = f"[[{word}(新規)]]"
                start, end = match.span()
                modified_content = modified_content[:start] + replacement + modified_content[end:]
                new_notes[word] = "新規作成推奨"
                linked_terms.add(word)
    
    return modified_content, {**added_links, **new_notes}, []

def generate_link_summary(links):
    """Generate a summary of added links"""
    summary = "---\n## 追加リンク一覧\n"
    
    for link, reason in links.items():
        if "(新規)" in link:
            link = link.replace("(新規)", "")
            summary += f"- [[{link}]]🆕 … {reason}\n"
        else:
            summary += f"- [[{link}]] … {reason}\n"
            
    return summary

def refine_note(file_path, content_dir):
    """Refine an Obsidian note file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract and parse frontmatter
    frontmatter, note_content = extract_frontmatter(content)
    fm_dict = parse_frontmatter(frontmatter)
    
    # Generate title if needed
    title = fm_dict.get('title', '')
    if not title or len(title) > 25:
        title = generate_title(note_content)
    
    # Extract tags
    tags = extract_tags(note_content)
    
    # Find existing notes
    existing_notes = find_existing_notes(content_dir)
    
    # Insert links and get link data
    linked_content, links, excess_links = insert_links(note_content, existing_notes, content_dir)
    
    # If too many potential links, just provide the list
    if excess_links:
        print(f"⚠️ 警告: 潜在的なリンク候補が多すぎます ({len(excess_links)}件)")
        print("リンク候補:")
        for i, link in enumerate(excess_links[:25]):
            print(f"- {link}")
        if len(excess_links) > 25:
            print(f"...他 {len(excess_links) - 25} 件")
        return
    
    # Generate link summary
    link_summary = generate_link_summary(links)
    
    # Remove existing link summary if present
    pattern = r'---\s*\n## 追加リンク一覧.*?$'
    linked_content = re.sub(pattern, '', linked_content, flags=re.MULTILINE | re.DOTALL)
    
    # Create new frontmatter
    new_frontmatter = f"""---
title: "{title}"
date: {fm_dict.get('date', datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000+09:00'))}
tags:
"""
    
    for tag in tags:
        new_frontmatter += f"  - {tag}\n"
        
    new_frontmatter += "---\n\n"
    
    # Construct final content
    final_content = new_frontmatter + linked_content.strip() + "\n\n" + link_summary
    
    # Show diff
    print("==== リファイン前 ====")
    print(content)
    print("\n==== リファイン後 ====")
    print(final_content)
    
    # Ask for confirmation
    confirmation = input("\n変更を保存しますか？ (y/n): ")
    if confirmation.lower() == 'y':
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"✅ {file_path} を更新しました")
    else:
        print("❌ 変更を破棄しました")

def main():
    parser = argparse.ArgumentParser(description='Obsidian ノートリファイナー')
    parser.add_argument('file', help='リファインするファイルパス')
    parser.add_argument('--content-dir', default='content', help='コンテンツディレクトリのパス')
    
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.exists(args.file):
        print(f"エラー: ファイル {args.file} が見つかりません")
        return 1
        
    refine_note(args.file, args.content_dir)
    return 0

if __name__ == "__main__":
    sys.exit(main()) 