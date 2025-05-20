#!/usr/bin/env python3
import os
import re
import yaml
import glob
from pathlib import Path
from typing import List, Dict, Set, Tuple
import difflib
from dataclasses import dataclass
import jieba
import jieba.posseg as pseg

@dataclass
class NoteMetadata:
    title: str
    date: str
    tags: List[str]
    link_exclude: bool = False

class NoteRefiner:
    def __init__(self, content_dir: str):
        self.content_dir = content_dir
        self.all_notes: Dict[str, str] = {}  # title -> path
        self.load_all_notes()
        
    def load_all_notes(self):
        """Load all markdown files in the content directory"""
        for md_file in glob.glob(f"{self.content_dir}/**/*.md", recursive=True):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract title from frontmatter
                title_match = re.search(r'title:\s*"([^"]+)"', content)
                if title_match:
                    title = title_match.group(1)
                    self.all_notes[title] = md_file

    def extract_frontmatter(self, content: str) -> Tuple[NoteMetadata, str]:
        """Extract frontmatter from markdown content"""
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
        if not frontmatter_match:
            return None, content

        frontmatter_text = frontmatter_match.group(1)
        body = frontmatter_match.group(2)
        
        # Parse frontmatter
        metadata = {}
        for line in frontmatter_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                if key == 'tags':
                    metadata[key] = [tag.strip() for tag in value.split('-') if tag.strip()]
                else:
                    metadata[key] = value

        return NoteMetadata(
            title=metadata.get('title', ''),
            date=metadata.get('date', ''),
            tags=metadata.get('tags', []),
            link_exclude=metadata.get('link_exclude', False)
        ), body

    def generate_title(self, content: str) -> str:
        """Generate a title under 25 characters without periods"""
        # Use the first sentence or paragraph as base
        first_para = content.split('\n\n')[0]
        # Remove markdown syntax
        clean_text = re.sub(r'[#*`_\[\]]', '', first_para)
        # Take first 25 chars and remove trailing punctuation
        title = clean_text[:25].strip('.,;:!?')
        return title

    def extract_tags(self, content: str) -> List[str]:
        """Extract 5-10 relevant tags from content"""
        # Use jieba for Chinese text segmentation
        words = pseg.cut(content)
        # Filter for nouns and important words
        tags = []
        for word, flag in words:
            if len(word) >= 2 and flag.startswith('n'):  # Only nouns
                tags.append(word)
        
        # Limit to 5-10 tags
        return tags[:10]

    def find_link_candidates(self, content: str) -> List[Tuple[str, str]]:
        """Find potential internal links in content"""
        candidates = []
        for title, path in self.all_notes.items():
            if title in content:
                candidates.append((title, path))
        return candidates

    def insert_links(self, content: str, candidates: List[Tuple[str, str]]) -> Tuple[str, List[str], List[str]]:
        """Insert internal links into content"""
        if len(candidates) > 25:
            return content, [], candidates

        modified_content = content
        existing_links = []
        new_notes = []

        for title, path in candidates:
            # Check if this is a new note
            if not os.path.exists(path):
                new_notes.append(title)
                continue

            # Replace first occurrence only
            if title in modified_content:
                modified_content = modified_content.replace(title, f"[[{title}]]", 1)
                existing_links.append(title)

        return modified_content, existing_links, new_notes

    def process_note(self, file_path: str) -> Tuple[str, List[str], List[str]]:
        """Process a single note file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        metadata, body = self.extract_frontmatter(content)
        if metadata.link_exclude:
            return content, [], []

        # Generate new title and tags
        new_title = self.generate_title(body)
        new_tags = self.extract_tags(body)

        # Find and insert links
        candidates = self.find_link_candidates(body)
        modified_body, existing_links, new_notes = self.insert_links(body, candidates)

        # Construct new frontmatter
        new_frontmatter = f"""---
title: "{new_title}"
date: {metadata.date}
tags:
{chr(10).join(f'  - {tag}' for tag in new_tags)}
---

"""
        new_content = new_frontmatter + modified_body

        # Add link summary
        if existing_links or new_notes:
            new_content += "\n===\n---\n## 追加リンク一覧\n"
            for link in existing_links:
                new_content += f"- [[{link}]] … 関連理由\n"
            for note in new_notes:
                new_content += f"- [[{note}🆕]] … 新規作成推奨\n"

        return new_content, existing_links, new_notes

    def show_diff(self, old_content: str, new_content: str):
        """Show diff between old and new content"""
        diff = difflib.unified_diff(
            old_content.splitlines(),
            new_content.splitlines(),
            lineterm=''
        )
        print('\n'.join(diff))

def main():
    refiner = NoteRefiner('content')
    
    # Process all markdown files
    for md_file in glob.glob('content/**/*.md', recursive=True):
        print(f"\nProcessing {md_file}...")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            old_content = f.read()
        
        new_content, existing_links, new_notes = refiner.process_note(md_file)
        
        # Show diff
        refiner.show_diff(old_content, new_content)
        
        # Ask for confirmation
        response = input("\nApply changes? (y/n): ")
        if response.lower() == 'y':
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Changes applied.")
        else:
            print("Changes discarded.")

if __name__ == "__main__":
    main() 