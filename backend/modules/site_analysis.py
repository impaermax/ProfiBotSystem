import requests
from urllib.parse import urlparse

def analyze_website(url):
    try:
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            return {"error": "Invalid URL"}

        response = requests.get(url, timeout=5)
        response.raise_for_status()

        analysis = {
            "status_code": response.status_code,
            "response_time": response.elapsed.total_seconds(),
            "content_length": len(response.content),
            "seo_score": "Good",  # Простой пример SEO-оценки
        }
        return analysis
    except Exception as e:
        return {"error": str(e)}
