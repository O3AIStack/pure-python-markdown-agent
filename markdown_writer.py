import datetime

def save_markdown(content):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"note-{timestamp}.md"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"✅ Markdown saved to {filename}\n")
