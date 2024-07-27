#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def get_news24_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.content, 'html.parser')

       
        headlines = soup.find_all('h1', class_='article__title')
        

        if not headlines:
            print("No headlines found on the page.")
            return

        for i, headline in enumerate(headlines, start=1):
            print(f"{i}. {headline.text.strip()}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the headlines: {e}")
        
        
        
        

def main():
    url = 'https://www.news24.com/news24/investigations/suspect-surve-top-editors-face-criminal-probe-for-goolam-gaffe-20240726'
    get_news24_headlines(url)
    
if __name__ == "__main__":
    main()    
    
