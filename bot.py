
import requests
from datetime import date

CITY = "Thiruvananthapuram"

def get_weather():
    response = requests.get(f"https://wttr.in/{CITY}?format=3", timeout=10)
    response.raise_for_status()
    return response.text

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=20)
        response.raise_for_status()
        data = response.json()
        return data[0]["q"], data[0]["a"]
    except Exception:
        return "Keep learning and keep building.", "Pulse Bot"
def build_summary():
    today = date.today()
    weather = get_weather()
    quote, author = get_quote()
    print("=== DAILY PULSE ===")
    print(f"Date: {today}")
    print(weather)
    print()
    print(f'"{quote}"')
    print(f"- {author}")
def run():
    build_summary()

if __name__ == "__main__":
    run() 