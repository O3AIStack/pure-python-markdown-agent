from openai import OpenAI
from config import OPENAI_API_KEY
from markdown_writer import save_markdown
import datetime

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_markdown(note):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Markdown formatter. Take user input and return well-structured Markdown."},
            {"role": "user", "content": note}
        ]
    )
    return response.choices[0].message.content.strip()

def main():
    print("📝 Markdown Note-Taking Agent (Type 'exit' to quit)\n")
    while True:
        user_input = input("Enter your note: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        markdown_note = generate_markdown(user_input)
        print("\n--- Generated Markdown Preview ---\n")
        print(markdown_note)
        save_markdown(markdown_note)

if __name__ == "__main__":
    main()
