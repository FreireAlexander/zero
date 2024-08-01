'''
    Goal: get download sounds file and IPA ffrom internet for a list of world

'''
import requests
from bs4 import BeautifulSoup
import urllib

URL_BASE = "https://es.forvo.com/word/"

URL = "https://es.forvo.com/word/chien/#fr"

API_WIKI = "https://en.wiktionary.org/w/api.php?action=help&modules=parse"

DOWNLOAD="https://upload.wikimedia.org/wikipedia/commons/transcoded/c/c5/Fr-Paris--dit.ogg/Fr-Paris--dit.ogg.mp3"



def main():
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
    except Exception as e:
        print(str(e))
        print("None")

    forvo_web = requests.get(URL, headers=headers)
    web_page = BeautifulSoup(forvo_web.content,"html.parser")
    print(web_page)
    response = requests.get(DOWNLOAD)
    
    with open("music.mp3", "wb") as file:
        file.write(response.content)
    



if __name__ == "__main__":
    main()