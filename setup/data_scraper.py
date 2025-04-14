import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Example: Replace with your own 100 Wikipedia article titles
WIKI_TITLES = [
    "Python_(programming_language)", "Machine_learning", "Artificial_intelligence", "Deep_learning",
    "Neural_network", "Natural_language_processing", "Data_science", "Computer_vision",
    "OpenAI", "ChatGPT", "Reinforcement_learning", "Generative_adversarial_network", "Transformer_(machine_learning_model)",
    "BERT_(language_model)", "LLaMA_(language_model)", "CUDA", "ROCm", "Linux", "Unix", "Windows_10",
    "Big_data", "Cloud_computing", "Edge_computing", "Quantum_computing", "Cybersecurity",
    "Cryptography", "Blockchain", "Bitcoin", "Ethereum", "Smart_contract", "GPU", "TPU", "CPU",
    "Operating_system", "Internet", "World_Wide_Web", "HTML", "CSS", "JavaScript", "React_(software)",
    "Vue.js", "Angular_(web_framework)", "Flask_(web_framework)", "Django_(web_framework)",
    "PostgreSQL", "MySQL", "MongoDB", "Redis", "GraphQL", "REST", "API", "Web_scraping",
    "Search_engine", "Google", "Microsoft", "Amazon_(company)", "Meta_Platforms", "Nvidia", "AMD",
    "Intel", "Tesla,_Inc.", "SpaceX", "NASA", "Jet_Propulsion_Laboratory", "Mars_rover", "Hubble_Space_Telescope",
    "Astrophysics", "Astronomy", "Physics", "Mathematics", "Statistics", "Probability", "Linear_algebra",
    "Calculus", "Optimization_(mathematics)", "Gradient_descent", "Backpropagation", "Support_vector_machine",
    "Decision_tree", "Random_forest", "K-means_clustering", "Principal_component_analysis", "t-SNE",
    "Autoencoder", "Anomaly_detection", "Data_mining", "Feature_engineering", "Model_selection", 
    "Cross-validation_(statistics)", "Bias–variance_tradeoff", "Overfitting", "Underfitting", 
    "A/B_testing", "Reproducibility", "Explainable_artificial_intelligence", "Ethics_of_artificial_intelligence",
    "Human–computer_interaction", "Cognitive_science"
]

BASE_URL = "https://en.wikipedia.org/wiki/"

def fetch_wikipedia_summary(title):
    url = BASE_URL + title
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraph = soup.select_one("p")
        return title, paragraph.get_text(strip=True) if paragraph else "No summary found"
    except Exception as e:
        return title, f"Error: {str(e)}"

def main():
    start = time.time()
    results = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_wikipedia_summary, title) for title in WIKI_TITLES]
        for future in as_completed(futures):
            title, summary = future.result()
            results.append((title, summary))
            print(f"[✓] {title} scraped")

    print(f"\n✅ Scraped {len(results)} pages in {time.time() - start:.2f} seconds\n")

    # Print a few sample results
    for title, summary in results[:5]:
        print(f"\n== {title} ==\n{summary}\n")

if __name__ == "__main__":
    main()

