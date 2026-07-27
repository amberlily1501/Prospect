import requests
from bs4 import BeautifulSoup


def fetch_page(url: str) -> str:
    response = requests.get( 
        url,
        timeout=10,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text(separator=" ", strip=True)

    return text[:5000]