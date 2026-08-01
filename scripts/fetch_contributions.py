import json, sys, requests
from bs4 import BeautifulSoup

def fetch_contributions(username="Adhiviraj"):
    url = f"https://github.com/users/{username}/contributions"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    days = [{"date": td.get("data-date"), "level": int(td.get("data-level", "0"))} for td in soup.find_all("td", class_="ContributionCalendar-day") if td.get("data-date")]
    with open("data/contributions.json", "w") as f:
        json.dump({"username": username, "days": days}, f, indent=2)

if __name__ == "__main__":
    fetch_contributions(sys.argv[1] if len(sys.argv) > 1 else "Adhiviraj")