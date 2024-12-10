import os
import requests
from datetime import date

SESSION_COOKIE = "53616c7465645f5f47cc1cbf3394370d0cedd7dd9a454b58b816a040679550c4dd7bf80946ddff1c7f52f6f020ecfdf9a461ffd3b7c3be8666b2f9516ad43b22"

YEAR = date.today().year

def download_input(day):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    headers = {"Cookie": f"session={SESSION_COOKIE}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        directory = f"day_{day:01d}"
        filename = f"{directory}/part_1.txt"
        
        with open(filename, "w") as f:
            f.write(response.text.strip())
        
        print(f"Downloaded input for Day {day}")
    else:
        print(f"Failed to download input for Day {day}. Status code: {response.status_code}")

def main():
    for day in range(1, 26):
        download_input(day)

if __name__ == "__main__":
    main()
