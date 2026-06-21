---
# メール・文章 自動分析ツール

Claude APIを使って、メールや文章を自動で要約・分類するPythonツールです。

## できること

- 文章を貼り付けるだけで自動分析
- カテゴリ分類（問い合わせ／クレーム／注文／依頼など）
- 緊急度判定（高／中／低）
- 対応アクションの提案

## 活用シーン

- 問い合わせメールの優先順位付け
- カスタマーサポートの効率化
- 社内レポートの要点抽出

## 使い方

```bash
pip install -r requirements.txt
python analyzer.py          # テキストを入力して分析
python analyzer.py --demo   # デモモード（APIキー不要）

技術スタック

- Python
- Claude API（Anthropic）

---
