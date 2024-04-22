import os
import requests
from pathlib import Path
from bs4 import BeautifulSoup

def fetch_data(url):
    """Extraire le contenu de la page Web à partir de l'URL donnée."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to retrieve data from {url}")
        return None

def clean_data(html_content):
    """Utiliser BeautifulSoup pour nettoyer et extraire le contenu textuel de la page Web."""
    soup = BeautifulSoup(html_content, 'html.parser')
    text = " ".join(soup.stripped_strings)
    return text

def save_data(data, file_path):
    """Enregistrez les données à l'emplacement de fichier spécifié."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)

def main():
    urls = [
        'https://huggingface.co/HuggingFaceH4/starchat2-15b-v0.1'
    ]

    for url in urls:
        file_name_raw = Path(url).name + '_raw.txt'
        file_name_clean = Path(url).name + '_clean.txt'

        html_content = fetch_data(url)
        if html_content:
            save_data(html_content.decode('utf-8'), f'data/raw/{file_name_raw}')

            cleaned_text = clean_data(html_content)
            save_data(cleaned_text, f'data/clean/{file_name_clean}')

if __name__ == "__main__":
    main()
