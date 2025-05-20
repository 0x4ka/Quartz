import os
import re
import yaml
import jieba
import jieba.posseg as pseg
from pathlib import Path
from typing import List, Dict, Tuple, Set
from datetime import datetime
import difflib

class NoteRefiner:
    def __init__(self, content_dir: str):
        self.content_dir = Path(content_dir)
        self.all_notes: Dict[str, str] = {}  # filename -> content
        self.load_all_notes()
        
    def load_all_notes(self):
        """Load all markdown files from the content directory"""
        for md_file in self.content_dir.rglob("*.md"):
            if md_file.name.startswith(".") or "templates" in str(md_file):
                continue
            with open(md_file, "r", encoding="utf-8") as f:
                self.all_notes[str(md_file.relative_to(self.content_dir))] = f.read()

    def extract_frontmatter(self, content: str) -> Tuple[Dict, str]:
        """Extract YAML frontmatter from markdown content"""
        if not content.startswith("---"):
            return {}, content
        
        parts = content.split("---", 2)
        if len(parts) < 3:
            return {}, content
            
        try:
            frontmatter = yaml.safe_load(parts[1])
            return frontmatter, parts[2].strip()
        except:
            return {}, content

    def generate_title(self, content: str) -> str:
        """Generate a title from content (25 chars max, no period)"""
        # Remove frontmatter and get first paragraph
        _, body = self.extract_frontmatter(content)
        first_para = body.split("\n\n")[0].strip()
        
        # Clean up and limit to 25 chars
        title = re.sub(r'[^\w\s]', '', first_para)
        title = title[:25].strip()
        
        # Ensure it ends with a noun
        words = list(pseg.cut(title))
        if words and words[-1].flag.startswith('n'):
            return title
        return title.rsplit(' ', 1)[0]

    def extract_tags(self, content: str) -> List[str]:
        """Extract 5-10 relevant tags from content"""
        _, body = self.extract_frontmatter(content)
        
        # Extract nouns and important words
        words = pseg.cut(body)
        tags = set()
        
        for word, flag in words:
            if flag.startswith('n') and len(word) > 1:  # Only nouns longer than 1 char
                tags.add(word)
        
        # Convert to list and limit to 5-10 tags
        tag_list = list(tags)
        return tag_list[:min(10, max(5, len(tag_list)))]

    def find_potential_links(self, content: str) -> Tuple[List[str], List[str]]:
        """Find potential internal links and new note suggestions"""
        _, body = self.extract_frontmatter(content)
        existing_links = []
        new_notes = []
        
        # Get all potential note titles
        note_titles = {Path(f).stem: f for f in self.all_notes.keys()}
        
        # Find potential matches
        words = pseg.cut(body)
        for word, flag in words:
            if flag.startswith('n') and len(word) > 1:
                # Check for exact matches
                if word in note_titles:
                    existing_links.append(word)
                # Check for similar matches
                else:
                    matches = difflib.get_close_matches(word, note_titles.keys(), n=1, cutoff=0.8)
                    if matches:
                        existing_links.append(matches[0])
                    else:
                        new_notes.append(word)
        
        return list(set(existing_links)), list(set(new_notes))

    def process_note(self, filepath: str) -> Tuple[str, List[str], List[str]]:
        """Process a single note and return the refined content"""
        content = self.all_notes[filepath]
        frontmatter, body = self.extract_frontmatter(content)
        
        # Generate new title
        new_title = self.generate_title(content)
        
        # Extract tags
        tags = self.extract_tags(content)
        
        # Find potential links
        existing_links, new_notes = self.find_potential_links(content)
        
        # Create new frontmatter
        new_frontmatter = {
            "title": new_title,
            "date": frontmatter.get("date", datetime.now().isoformat()),
            "tags": tags
        }
        
        # Create new content
        new_content = f"---\n{yaml.dump(new_frontmatter, allow_unicode=True)}---\n\n{body}\n\n"
        
        # Add link summary
        if existing_links or new_notes:
            new_content += "===\n---\n## 追加リンク一覧\n"
            for link in existing_links:
                new_content += f"- [[{link}]] … 関連ノート\n"
            for note in new_notes:
                new_content += f"- [[{note}(新規)]]🆕 … 新規作成推奨\n"
        
        return new_content, existing_links, new_notes

    def show_diff(self, original: str, refined: str) -> str:
        """Show diff between original and refined content"""
        diff = difflib.unified_diff(
            original.splitlines(),
            refined.splitlines(),
            lineterm=''
        )
        return '\n'.join(diff)

def main():
    refiner = NoteRefiner("content")
    
    # Process each note
    for filepath in refiner.all_notes.keys():
        print(f"\nProcessing: {filepath}")
        original = refiner.all_notes[filepath]
        refined, links, new_notes = refiner.process_note(filepath)
        
        # Show diff
        diff = refiner.show_diff(original, refined)
        print("\nChanges:")
        print(diff)
        
        # Ask for confirmation
        response = input("\nApply changes? (y/n): ")
        if response.lower() == 'y':
            with open(Path("content") / filepath, "w", encoding="utf-8") as f:
                f.write(refined)
            print("Changes applied!")
        else:
            print("Changes discarded.")

if __name__ == "__main__":
    main() 