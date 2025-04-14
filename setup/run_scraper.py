# run_scraper.py

import json
import time
from data_scraper import scrape_wikipedia_articles

WIKI_TITLES = [
    "Python_(programming_language)", "Machine_learning", "Artificial_intelligence", "Deep_learning",
    "Neural_network", "Natural_language_processing", "Data_science", "Computer_vision",
    "OpenAI", "ChatGPT", "Reinforcement_learning", "Generative_adversarial_network", "Transformer_(machine_learning_model)",
    "BERT_(language_model)", "LLaMA_(language_model)", "CUDA", "ROCm", "Linux", "Unix", "Windows_10"
    # Add more if needed
]

def main():
    start = time.time()
    print("⏳ Scraping articles...\n")

    results = scrape_wikipedia_articles(WIKI_TITLES)

    with open("wikipedia_scraped.jsonl", "w", encoding="utf-8") as f:
        for item in results:
            json.dump(item, f, ensure_ascii=False)
            f.write("\n")

    print(f"\n✅ Done in {time.time() - start:.2f} seconds.")
    print("📄 Output saved to `wikipedia_scraped.jsonl`\n")

    for item in results[:3]:
        print(f"== {item['title']} ==\n{item['text'][:500]}...\n")

if __name__ == "__main__":
    main()

