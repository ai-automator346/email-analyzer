import json
import sys

DEMO_RESPONSE = {
    "summary": "顧客から注文番号12345の商品未着について問い合わせ。3日間配送状況が更新されておらず、急ぎで確認を求めている。",
    "category": "クレーム",
    "urgency": "高",
    "key_points": ["注文番号12345の商品が未着", "配送状況が3日間未更新"],
    "suggested_action": "配送会社へ即日確認し、24時間以内に顧客へ進捗を報告する"
}

def analyze_with_api(text):
    import anthropic
    client = anthropic.Anthropic()
    prompt = f"""以下のメール・文章を分析してください。

---
{text}
---

以下のJSON形式のみで回答してください（説明文は不要）:
{{
  "summary": "3行以内の要約",
  "category": "問い合わせ/クレーム/注文/依頼/報告/一般 のいずれか1つ",
  "urgency": "高/中/低 のいずれか1つ",
  "key_points": ["重要ポイント1", "重要ポイント2"],
  "suggested_action": "担当者への推奨アクション（1文）"
}}"""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(message.content[0].text)


def print_result(result):
    urgency_label = {"高": "[高]", "中": "[中]", "低": "[低]"}.get(result["urgency"], "[-]")
    print("")
    print("[要約]")
    print("  " + result["summary"])
    print("")
    print("カテゴリ : " + result["category"])
    print("緊急度   : " + urgency_label + " " + result["urgency"])
    print("")
    print("[重要ポイント]")
    for point in result["key_points"]:
        print("  - " + point)
    print("")
    print("[推奨アクション]")
    print("  " + result["suggested_action"])
    print("")


def main():
    try:
        print("=== メール・文章 自動分析ツール（Claude API） ===")

        demo_mode = "--demo" in sys.argv
        args = [a for a in sys.argv[1:] if a != "--demo"]

        if demo_mode:
            print("（デモモードで実行中）")
            print("")
            print("テキスト例:")
            print("  先週注文した商品（No.12345）がまだ届いていません。")
            print("  配送状況が3日間更新されておらず急いでいます。")
            print("")
            print("分析中...")
            print_result(DEMO_RESPONSE)
            return

        if args:
            with open(args[0], "r", encoding="utf-8") as f:
                text = f.read()
        else:
            print("")
            print("テキストを入力してください（終了: 空行でEnter）:")
            print("")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            text = "\n".join(lines)

        print("")
        print("分析中...")
        print_result(analyze_with_api(text))

    except Exception as e:
        print("エラーが発生しました: " + str(e))


if __name__ == "__main__":
    main()
