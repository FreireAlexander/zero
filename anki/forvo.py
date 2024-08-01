import math
from bs4 import BeautifulSoup
import cloudscraper
import base64
import re 
import time
import random

def get_audio_link(onclickFunction):
    #example js play functions from forvo:
    #Play(6166435,'OTg4MTIyMC8xMzgvOTg4MTIyMF8xMzhfMzM5MDIxLm1wMw==','OTg4MTIyMC8xMzgvOTg4MTIyMF8xMzhfMzM5MDIxLm9nZw==',false,'by80L280Xzk4ODEyMjBfMTM4XzMzOTAyMS5tcDM=','by80L280Xzk4ODEyMjBfMTM4XzMzOTAyMS5vZ2c=','h');return false;
    #Play(6687207,'OTU5NzcxMy8xMzgvOTU5NzcxM18xMzhfNjk2MDEyMi5tcDM=','OTU5NzcxMy8xMzgvOTU5NzcxM18xMzhfNjk2MDEyMi5vZ2c=',false,'','','l');return false;
    # All audios have an ogg version as a fallback on the mp3. Ogg is open source and compresses audio to a smaller size than mp3.
    # So I grab the ogg base64 string and decode it.
    print(f"List: \n{onclickFunction.split(',')}\n")
    base64audio = onclickFunction.split(',')[2].replace('\'', "")
    print(f"base64audio: {base64audio}")
    print(f"encode to ASCII : \n{base64audio.encode('ascii')}\n")
    print(f"bs64decode to ASCII : \n{base64.b64decode(base64audio.encode('ascii'))}\n")
    decodedLink = base64.b64decode(base64audio.encode('ascii')).decode('ascii')
    print(decodedLink)
    return "https://audio00.forvo.com/ogg/" + decodedLink


def get_link(audio):
    base64audio = audio.split(',')[2]
    decode = base64.b64decode(base64audio).decode('ascii')
    print(f"decode string: {decode}")
    return "https://audio00.forvo.com/ogg/" + decode


def main():
    language_id ="es"
    word = "pizza"
    pattern = re.compile(r"Play\([\d,'\w=); ]*false")
    scraper = cloudscraper.create_scraper() 
    url = f"https://es.forvo.com/word/{word}/"
    info = scraper.get(url)
    while info.status_code != 200:
        number = random.randint(10,15)
        print(f"Error -> Status Code: {info.status_code}")
        print(f"Trying again in {number} seconds")
        time.sleep(number)
        info = scraper.get(url)
    
    soup = BeautifulSoup(info.text, "html.parser")
    #print(soup.find(class_ = "play").get_text())
    
    languages = soup.find_all('article', class_='pronunciations', id=f"language-{language_id}")
    print(len(languages))
    language = BeautifulSoup(str(languages), "html.parser")
    #print(f"language {language_id}:\n{language}\n")
    listas = language.find_all('li', class_='pronunciation')
    print(f"lista: {len(listas)}")
    for index, item in enumerate(listas):
        sopa = BeautifulSoup(str(item), "html.parser")
        votes = str(sopa.find('span', class_='num_votes').text)
        votes = re.findall(r'\d{1,}', votes)[0]
        print(f"Num de votos para el link {index+1}: {votes}")
        names = str(sopa.find('span', class_='info').text)
        res = re.findall('\w{1,}', names)[-1]
        print(f"Nombre {index+1}: {res}")
    #audio_elements = language.find_all('div', class_='play')
    #print(audio_elements)
    #print(len(audio_elements))
    '''
    for index, audio in enumerate(audio_elements):
        #print(f"{index}: {audio}")
        #print(str(audio))
        match = re.findall(pattern, str(audio))
        #print(match[0])
        link = get_link(match[0])
        #print(link)
        scraper = cloudscraper.create_scraper() 
        audio = scraper.get(link)
        #print(f"response for audio {index}: {audio} \n{link}")
        
        #print(audio.content)
        with open(f"fr_pron_word_{index}.mp3", "wb") as file:
            file.write(audio.content)

        file.close()
    '''
    


# Ejemplo de uso

if __name__ == "__main__":
    main()