---
title: "settings"
date: September 1, 2024
tags: 
---

source: [/0x4ka-extensions](https://scrapbox.io/0x4ka-extensions)

## 画像サイズ
style.css

```
/* 画像サイズ [*** [画像URL] ] で設定できるようにする */
.level-1 img { width: 16.7%; max-height: none!important; }
.level-2 img { width: 33.3%; max-height: none!important; }
.level-3 img { width: 50%; max-height: none!important; }
.level-4 img { width: 66.7%; max-height: none!important; }
.level-5 img { width: 83.3%; max-height: none!important; }
.level-6 img { width: 100%; max-height: none!important; }
```


## チェックボックス
style.css

```
 /* チェックボックスになるタグ v2 Font Awesome版 */
 .line:not(.cursor-line) a[href='./o']:not(.icon) span,
 .line:not(.cursor-line) a[href='./v']:not(.icon) span {
   display: inline-block; width: 0; text-indent: -9999px }
 .line:not(.cursor-line) a[href='./o']:not(.icon)::after,
 .line:not(.cursor-line) a[href='./v']:not(.icon)::after {
   display: inline-block; min-width: 1.15em; padding-left: 1px;
   font-family: FontAwesome; font-size: 120%; text-align: center; vertical-align: middle }
 .line:not(.cursor-line) a[href='./o']:not(.icon)::after { content: '\f096'; color: #08BDBD }
 .line:not(.cursor-line) a[href='./v']:not(.icon)::after { content: '\f046'; color: #2489C5 }
```


## コードハイライト
style.css

```
/*--コードハイライト系--*/
 .line code {
   padding: 4px 0;
   font-size: 0.8em;
   color: #c5c8c6;
   background-color: #1d1f21;
 }
 .line span.code-block {
   background-color: #1d1f21;
 }
 .page-list-item .description code {
   padding: 4px;
   font-size: 0.8em;
   color: #c5c8c6;
   background-color: #1d1f21;
 }
```


## Tommoro comment?
style.css

```
/* Tomorrow Comment */
  .hljs-comment,
  .hljs-quote {
    color: #969896;
  }
  
  /* Tomorrow Red */
  .hljs-variable,
  .hljs-template-variable,
  .hljs-tag,
  .hljs-name,
  .hljs-selector-id,
  .hljs-selector-class,
  .hljs-regexp,
  .hljs-deletion {
    color: #cc6666;
  }
  
  /* Tomorrow Orange */
  .hljs-number,
  .hljs-built_in,
  .hljs-builtin-name,
  .hljs-literal,
  .hljs-type,
  .hljs-params,
  .hljs-meta,
  .hljs-link {
    color: #de935f;
  }
  
  /* Tomorrow Yellow */
  .hljs-attribute {
    color: #f0c674;
  }
  
  /* Tomorrow Green */
  .hljs-string,
  .hljs-symbol,
  .hljs-bullet,
  .hljs-addition {
    color: #b5bd68;
  }
  
  /* Tomorrow Blue */
  .hljs-title,
  .hljs-section {
    color: #81a2be;
  }
  
  /* Tomorrow Purple */
  .hljs-keyword,
  .hljs-selector-tag {
    color: #b294bb;
  }
```


## ハッシュタグ
style.css

```
 a[type="hashTag"] {   
    padding: 0.4em 0.6em;
    font-size: 0.8em;
    color: #fff !important;
    background-color: #36383d;
    border-radius: 4px;
 }
```


## 背景色
style.css

```
 body {background-color: #26282B;}
.page {
	background: #2B2D31;
	margin: initial;
}
.content {
	background: #2B2D31;
}

.title-with-description {
	color: #f0f0f0;
}
.list li.page-list-item a .description {
    color: rgba(240, 240, 240,0.7);
}
```


## 検索時のハイライト
style.css

```
/*検索にマッチした文字のハイライト*/
.list li.page-list-item a .search-matched {
    font-weight: bold;
    background-color: #6d5127;
}
.list > li.page-list-item { 
	background-color: #2B2D31; 
}
/*ホバー状態の背景色*/
 .list li.page-list-item a:hover {
     background-color: #222427!important;
 }
```


## カードサイズ
style.css

```
.page-list .grid li {
     height: 160px;
 }
 @media (max-width: 450px) {
 	.page-list .grid li {
      width: 160px;
       height: 160px;
   }
 }
 .grid li.page-list-item a {
     background-color: initial;
     box-shadow: initial;
     border-radius: 2px;
 }
```


## 引用
style.css

```
.line .quote {
    background: #313338;
    color: #ABABAB;
    text-decoration: none !important;
 }
 .link {
 	color: #6096bd !important;
 }
```


## 外部リンク
style.css

```
 /* 外部リンクにiconをつける from tkgshn settings https://scrapbox.io/tkgshn/settings#604c694e09c5f20000e9d254*/
  .line span:not(.modal-image):not(.pointing-device-map) > a.link:not(.icon)::after {
      font-family: 'Font Awesome 5 Free';
      content: ' \f35d';
      font-weight: 900;
      display: inline-block;
    }
  
 .quote > span > a.link {
     text-decoration: underline;
     -webkit-tap-highlight-color: rgba(0,0,0,.2);
     color: #4f6777 !important;
 }
 .grid li.page-list-item a {
     display: block;
 }
 .new-button {
 	background-color: #4D4D4D !important;
 }
 .new-button > div {
   	background-color: #C1C1C1 !important;
 }
 .line .telomere .telomere-border.updated-after-load { border-color: #E23758; }
 .line .telomere .telomere-border.unread:not(.updated-after-load) {
     border-color: #E23758;
 }
```


## インデント
style.css

```
 /*インデントのドットの形状と色を変える*/
 .line .indent-mark .dot {
     display: block;
     position: absolute;
     right: 9px;
     top: 12px;
     width: 8px;
     height: 3px;
     border-radius: initial;
 }
 .line .indent-mark span:nth-child(1) + .dot {
    	background-color: #D9D9D9;
    }
 .line .indent-mark span:nth-child(2) + .dot {
  	background-color: #F77A27;
  }
 .line .indent-mark span:nth-child(3) + .dot {
  	background-color: #3b8edb;
  }
 .line .indent-mark span:nth-child(4) + .dot {
  	background-color: #f7c027;
  }
   .line .indent-mark span:nth-child(5) + .dot {
       	background-color: #D9D9D9;
       }
    .line .indent-mark span:nth-child(6) + .dot {
     	background-color: #F77A27;
     }
    .line .indent-mark span:nth-child(7) + .dot {
     	background-color: #3b8edb;
     }
    .line .indent-mark span:nth-child(8) + .dot {
     	background-color: #f7c027;
     }
 /*インデントに背景色をつける*/ 
  .indent-mark {
    	height: 100% !important;
    }
  .indent-mark .pad {
    	height: 100% !important;
    	overflow: unset !important;
  }
  .indent-mark span:nth-child(1) .pad {
  		background: rgba(217, 217, 217,0.1);
  }
  .indent-mark span:nth-child(2) .pad {
        background: rgba(247, 122, 39,0.1);
  }
  .indent-mark span:nth-child(3) .pad {
      	background: rgba(59, 142, 219,0.1);
  }
  .indent-mark span:nth-child(4) .pad {
       	background: rgba(247, 192, 39,0.1);
  }
  .indent-mark span:nth-child(5) .pad {
  		background: rgba(217, 217, 217,0.1);
  }
  .indent-mark span:nth-child(6) .pad {
        background: rgba(247, 122, 39,0.1);
  }
  .indent-mark span:nth-child(7) .pad {
      	background: rgba(59, 142, 219,0.1);
  }
  .indent-mark span:nth-child(8) .pad {
       	background: rgba(247, 192, 39,0.1);
  }
  /* コードブロックの場合、インデントの背景色をコードブロックのカラーに合わせる */
  .text.code-block > .indent-mark span:nth-child(1) .pad { 
  	background: #1d1f21!important;
   }
   /* コードブロックの場合、インデントの背景色をコードブロックのカラーに合わせる */
      .text.code-block > .indent-mark span:nth-child(2) .pad { 
      	background: #1d1f21!important;
       }
       /* コードブロックの場合、インデントの背景色をコードブロックのカラーに合わせる */
          .text.code-block > .indent-mark span:nth-child(3) .pad { 
          	background: #1d1f21!important;
           }
  
```


## 数式の文字サイズ
style.css

```
 /*数式の文字サイズ*/
 .line .formula .katex-display {
 	font-size: 12px;
 }
```


## カーソル
style.css

```
 /* カーソルの幅と色替え */
.cursor { width: 3px; background-color: #E23758; }
.cursor svg { display: none; }
.scroll-bar-overlay .unread-bar {background-color: #E23758;}]
```


## ヘッダーのアイコンをScrapboxから変更する
[/akio6o6/Scrapboxのロゴ画像を変更する](https://scrapbox.io/akio6o6/Scrapboxのロゴ画像を変更する)
style.css 

```
/* ロゴ変更 */
.navbar .navbar-brand img {
    display: none;
}
.navbar-brand:before {
    content: '';
    background: url('https://pbs.twimg.com/profile_images/1532013477870440448/2u4HmssF_400x400.jpg');
    background-size: contain;
    width: 0;
    height: 0;
    margin: 10px 16px 0 0;
    flex-shrink: 0;
    border-radius: 25%;
}
.icon-arrow-down:before {
    color: white;
}
```


### ピン留めされたページを独立した段に表示する
- [/bluemountain-theme/settings#60b8d53a79e1130000a6fd75](https://scrapbox.io/bluemountain-theme/settings#60b8d53a79e1130000a6fd75)
- cf. [/aioilight/settings](https://scrapbox.io/aioilight/settings)
style.css

```
.page-list-item.pin + .page-list-item:not(.pin) {
  	clear: both;
}
```


薄く表示 `[( 薄く表示]` で出ます
- [/tkgshn-extension/settings#610034a609c5f2000063389d](https://scrapbox.io/tkgshn-extension/settings#610034a609c5f2000063389d)
style.css

```
.deco-\( {
  opacity: 0.5;
} 
```


インライン引用
    - [/scrasobox/拡張記法がきた！#59e5376896b9040000af6917](https://scrapbox.io/scrasobox/拡張記法がきた！#59e5376896b9040000af6917)
style.css

```
.deco-\" {
  font-size:100%;
  font-style: italic;
  color: #ABABAB;
  }
.deco-\"::before {
  font-size:85%;
  font-family: 'Font Awesome 5 Free';
  color: #ABABAB;
  font-weight:900;
  content: '\f10e';
  vertical-align: super;
  margin-right: 6px;
  }
```


コードブロックに行数
- [/takker/コードブロック記法に行番号を表示するUserCSS](https://scrapbox.io/takker/コードブロック記法に行番号を表示するUserCSS)
 style.css 

```
 .section-title, .code-block-start {
   counter-reset: codeline
 }
 .code-block .indent-mark > span.char-index:last-child {
   counter-increment: codeline 
 }
 
 body:not(.presentation) .code-block .indent-mark > span.char-index:last-child::before {
   content: counter(codeline); 
   position: absolute;
   padding-left: 4px;
 }
 .code-block .indent-mark > span.char-index:last-child::before {
   color: var(--code-line-number-color, #3f3f3f);
 }
 /* カーソル選択時の行番号の色 */
 .cursor-line .code-block .indent-mark > span.char-index:last-child::before {
   color: var(--cursor-code-line-number-color, #E23758); 
 }
    
```


テーブルのセルをわかりやすくする
[/scrasobox/テーブルのセルをわかりやすくする](https://scrapbox.io/scrasobox/テーブルのセルをわかりやすくする)
 style.css

```
/* テーブルのセルをわかりやすくする */
.table-block table { background-color: transparent; border-collapse: separate; border-spacing: 2px }
.table-block table tr td:nth-child(odd) { padding: .1em; background-color: rgba(0,0,0,0.04) }
.table-block table tr:nth-child(even) td { background-color: rgba(0,0,0,0.06) } /* 偶数行を濃くする */
.table-block table tr:first-child td { font-weight: bolder; text-align: center } /* 1行目だけ太字&中央揃え */
.table-block table tr td:first-child { padding: 0; background-color: transparent; border-width: 0 }
```



