# ThumbyColor-Learning

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

Thumby Color のゲームエンジン API を身につけるための学習リポジトリです。
デバイスへの実装も記録しながら、Phase 1〜4 で段階的に進めています。

## Thumby Color とは

[Thumby Color](https://color.thumby.us/) は [TinyCircuits](https://tinycircuits.com/) が製造する超小型ゲームデバイスです。

| 項目 | 仕様 |
|------|------|
| 画面 | 128×128px 16bit カラー TFT LCD |
| CPU | RP2350 デュアルコア（FPU内蔵） |
| 言語 | MicroPython |
| エンジン | TinyCircuits Tiny Game Engine |

## 学習計画

詳細なテーマリストとチェックボックスは [docs/learning-plan.md](docs/learning-plan.md) で管理しています。

| Phase | レベル | 主な内容 | ゴール |
|-------|--------|----------|--------|
| Phase 1 | 基本（初級） | ゲームループ・図形描画・ボタン入力・ノード | ボタンで動くキャラクターを表示 |
| Phase 2 | 発展（中級） | 画像スプライト・アニメーション・サウンド・セーブ | ミニゲーム製作 |
| Phase 3 | 応用（中上級） | 物理演算・衝突検知・デバッグ | プラットフォーマーの基礎 |
| Phase 4 | 特殊機能 | デバイス間通信・RTC | — |

## ファイル構成

```
ThumbyColor-Learning/
├── main.py              # エントリーポイント（テンプレート実装）
├── docs/
│   └── learning-plan.md # 詳細な学習テーマリスト（チェックボックス付き）
└── LICENSE
```

## 環境・ツール

- **デバイス上のパス**: `/Games/ThumbyColor-Learning/`
- **言語**: MicroPython
- **開発ツール**:
  - [ブラウザエディタ](https://color.thumby.us/code/)（Chrome / Edge）— コード編集・エミュレータ・実機転送
  - [Thonny](https://thonny.org/) — ファイル転送・REPL

## ライセンス

[GNU General Public License v3.0](LICENSE)
