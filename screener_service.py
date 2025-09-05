import requests
from bs4 import BeautifulSoup

def get_fundamentals(symbol):
    url = f"https://www.screener.in/company/{symbol}/"
    resp = requests.get(url, timeout=15)
    soup = BeautifulSoup(resp.text, "html.parser")
    out = {}
    # Example extractions (keep minimal to avoid heavy scraping)
    pe = soup.find("li", string=lambda t: t and "P/E" in t)
    roe = soup.find("li", string=lambda t: t and "ROCE" in t or "ROE" in t)
    out["P/E"] = pe.get_text(strip=True) if pe else "N/A"
    out["ROE/ROCE"] = roe.get_text(strip=True) if roe else "N/A"
    return out
