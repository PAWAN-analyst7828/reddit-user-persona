# persona_builder.py

import sys
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
from utils.reddit_scraper import scrape_user_content
from utils.persona_generator import generate_persona

def extract_username_from_url(url):
    parsed = urlparse(url)
    if "reddit.com" not in parsed.netloc:
        raise ValueError("Invalid Reddit URL")
    parts = parsed.path.strip("/").split("/")
    if len(parts) < 2 or parts[0] != "user":
        raise ValueError("URL must be in format https://www.reddit.com/user/<username>/")
    return parts[1]

def main():
    load_dotenv()
    if len(sys.argv) != 2:
        print("Usage: python persona_builder.py <Reddit Profile URL>")
        sys.exit(1)

    url = sys.argv[1]
    username = extract_username_from_url(url)

    print(f"🔍 Scraping Reddit data for u/{username}...")
    comments, posts = scrape_user_content(username)

    print(f"🧠 Generating user persona for u/{username}...")
    persona = generate_persona(username, comments, posts)

    output_path = os.path.join("personas", f"{username}.txt")
    os.makedirs("personas", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"✅ Persona saved to {output_path}")

if __name__ == "__main__":
    main()
