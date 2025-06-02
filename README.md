# 📝 Pure Python Markdown Agent

Convert freeform text into structured Markdown with a lightweight AI assistant built entirely in Python—no frameworks required.

## 🚀 Overview

This terminal-based tool uses the OpenAI API to:
- Accept natural language input (e.g., "Meeting notes about project X...")
- Reformat the text into clean, readable Markdown
- Save the output to a `.md` file with a timestamped filename

It's minimal, extensible, and a perfect building block for personal knowledge management workflows.

---

## 📁 Project Structure

pure-python-markdown-agent/
├── main.py # Core interaction loop
├── markdown_writer.py # File-saving utility
├── config.py # API key configuration
├── requirements.txt
└── README.md


---

## 🛠️ Installation

Clone the repo and install the requirements:

```bash
git clone https://github.com/your-username/pure-python-markdown-agent
cd pure-python-markdown-agent
pip install -r requirements.txt

