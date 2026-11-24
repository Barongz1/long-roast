"""The Long Roast — entry for make.fun.

Writes one line to /output/entry.txt. The line is a roast of our own AI agent, at most 200 characters.
"""
import os

LINE = "Our agent rewrote the code, fixed nothing, and then wrote a five-paragraph summary explaining why doing nothing was the hardest part."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
