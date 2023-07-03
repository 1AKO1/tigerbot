import requests
from bs4 import BeautifulSoup

import os
os.environ["http_proxy"] = "socks5://127.0.0.1:10808"
os.environ["https_proxy"] = "socks5://127.0.0.1:10808"

def search(query):
    search_url = f"https://www.google.com/search?sxsrf=AB5stBgfi_HNXP2sDT8-4uSBF8MKwLIH8g:1688347233920&q={query}&tbm=nws&sa=X&ved=2ahUKEwjZk4rJr_H_AhUKMDQIHXeYDbMQ0pQJegQICRAB&cshid=1688347398165159&biw=580&bih=658&dpr=1.25"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    response = requests.get(search_url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    search_results = soup.select(".SoaBEf")

    for result in search_results:
        item = result.select(".iRPxbe div")
        title = item[1].get_text()
        content = item[2].get_text()
        print(f"Title: {title}")
        print(f"Content: {content}\n")

# Example usage
search("蔡徐坤")