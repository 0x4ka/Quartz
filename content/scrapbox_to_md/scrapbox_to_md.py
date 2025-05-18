#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re
import requests
from urllib.parse import urlparse
import sys
from pathlib import Path

def download_image(url, save_dir):
    """
    URLから画像をダウンロードして、指定されたディレクトリに保存する
    
    Args:
        url (str): 画像のURL
        save_dir (str): 保存先ディレクトリ
        
    Returns:
        str: 保存されたファイルのパス、失敗した場合はNone
    """
    try:
        # URLからファイル名を抽出
        parsed_url = urlparse(url)
        file_name = os.path.basename(parsed_url.path)
        
        # 保存先パスを作成
        save_path = os.path.join(save_dir, file_name)
        
        # 既に存在する場合はダウンロードをスキップ
        if os.path.exists(save_path):
            print(f"画像ファイルは既に存在します: {save_path}")
            return save_path
        
        # 画像をダウンロード
        response = requests.get(url, stream=True)
        response.raise_for_status()  # エラーがあれば例外を発生
        
        # ファイルに保存
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print(f"画像をダウンロードしました: {save_path}")
        return save_path
    
    except Exception as e:
        print(f"画像のダウンロードに失敗しました: {url}, エラー: {e}")
        return None

def convert_scrapbox_to_markdown(json_data, img_dir="./img"):
    """
    ScrapboxのJSONデータをMarkdownに変換する
    
    Args:
        json_data (dict): ScrapboxのJSONデータ
        img_dir (str): 画像の保存先ディレクトリ
        
    Returns:
        dict: ページタイトルをキー、Markdown内容を値とする辞書
    """
    # ユーザー情報の辞書を作成（IDをキーにする）
    users = {user["id"]: user for user in json_data.get("users", [])}
    
    # 結果を格納する辞書
    markdown_pages = {}
    
    # ページごとに処理
    for page in json_data.get("pages", []):
        title = page.get("title", "Untitled")
        lines = page.get("lines", [])
        
        # Markdownコンテンツを構築
        md_content = f"# {title}\n\n"
        
        # 作成日時と更新日時を追加
        created = page.get("created")
        updated = page.get("updated")
        if created:
            created_date = f"作成日時: {format_timestamp(created)}\n"
            md_content += created_date
        if updated:
            updated_date = f"更新日時: {format_timestamp(updated)}\n"
            md_content += updated_date
        
        md_content += "\n"
        
        # 行ごとに処理
        for line in lines:
            text = line.get("text", "")
            user_id = line.get("userId")
            
            # 空行の場合
            if not text:
                md_content += "\n"
                continue
            
            # インデントを処理（タブをスペースに変換）
            indent_level = 0
            while text.startswith("\t"):
                indent_level += 1
                text = text[1:]
            
            # インデントに応じてMarkdownの箇条書きを追加
            prefix = "  " * indent_level
            if indent_level > 0:
                prefix += "- "
            
            # 画像リンクを処理
            # パターン1: [https://scrapbox.io/files/xxxx.png]
            img_pattern1 = r'\[(https://scrapbox\.io/files/[^\]]+\.(png|jpg|jpeg|gif))\]'
            # パターン2: [[https://scrapbox.io/files/xxxx.png]]
            img_pattern2 = r'\[\[(https://scrapbox\.io/files/[^\]]+\.(png|jpg|jpeg|gif))\]\]'
            
            # パターン1の画像リンクを処理
            for match in re.finditer(img_pattern1, text):
                img_url = match.group(1)
                file_name = os.path.basename(urlparse(img_url).path)
                img_path = f"{img_dir}/{file_name}"
                
                # 画像をダウンロード
                try:
                    download_image(img_url, img_dir.lstrip("./"))
                except Exception as e:
                    print(f"画像のダウンロードに失敗しました: {img_url}, エラー: {e}")
                
                # Markdownの画像リンクに置換
                text = text.replace(match.group(0), f"![{file_name}]({img_path})")
            
            # パターン2の画像リンクを処理
            for match in re.finditer(img_pattern2, text):
                img_url = match.group(1)
                file_name = os.path.basename(urlparse(img_url).path)
                img_path = f"{img_dir}/{file_name}"
                
                # 画像をダウンロード
                try:
                    download_image(img_url, img_dir.lstrip("./"))
                except Exception as e:
                    print(f"画像のダウンロードに失敗しました: {img_url}, エラー: {e}")
                
                # Markdownの画像リンクに置換
                text = text.replace(match.group(0), f"![{file_name}]({img_path})")
            
            # 通常のリンクを処理
            link_pattern = r'\[(https?://[^\]]+)\]'
            for match in re.finditer(link_pattern, text):
                link_url = match.group(1)
                # Markdownのリンクに置換（タイトルなしの場合）
                text = text.replace(match.group(0), f"[{link_url}]({link_url})")
            
            # タイトル付きリンクを処理
            titled_link_pattern = r'\[(https?://[^ \]]+) ([^\]]+)\]'
            for match in re.finditer(titled_link_pattern, text):
                link_url = match.group(1)
                link_title = match.group(2)
                # Markdownのリンクに置換
                text = text.replace(match.group(0), f"[{link_title}]({link_url})")
            
            # 行を追加
            md_content += f"{prefix}{text}\n"
            
            # ユーザー情報を追加（オプション）
            if user_id and user_id in users:
                user = users[user_id]
                user_name = user.get("displayName") or user.get("name", "Unknown")
                # コメントとしてユーザー情報を追加することもできる
                # md_content += f"{prefix}<!-- by {user_name} -->\n"
        
        # 結果を辞書に追加
        markdown_pages[title] = md_content
    
    return markdown_pages

def format_timestamp(timestamp):
    """
    UNIXタイムスタンプを読みやすい形式に変換
    
    Args:
        timestamp (int): UNIXタイムスタンプ
        
    Returns:
        str: フォーマットされた日時文字列
    """
    from datetime import datetime
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def main():
    """
    メイン関数
    """
    if len(sys.argv) < 2:
        print("使用方法: python scrapbox_to_md.py <scrapbox_json_file>")
        sys.exit(1)
    
    json_file = sys.argv[1]
    output_dir = "."
    img_dir = "./img"
    
    # コマンドライン引数からオプションを解析
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    
    if len(sys.argv) > 3:
        img_dir = sys.argv[3]
    
    # 出力ディレクトリとイメージディレクトリを作成
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(img_dir.lstrip("./"), exist_ok=True)
    
    # JSONファイルを読み込む
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except Exception as e:
        print(f"JSONファイルの読み込みに失敗しました: {e}")
        sys.exit(1)
    
    # Markdownに変換
    markdown_pages = convert_scrapbox_to_markdown(json_data, img_dir)
    
    # Markdownファイルを保存
    for title, content in markdown_pages.items():
        # ファイル名に使えない文字を置換
        safe_title = re.sub(r'[\\/*?:"<>|]', "_", title)
        md_file = os.path.join(output_dir, f"{safe_title}.md")
        
        try:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Markdownファイルを保存しました: {md_file}")
        except Exception as e:
            print(f"Markdownファイルの保存に失敗しました: {md_file}, エラー: {e}")

if __name__ == "__main__":
    main()
