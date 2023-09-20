from bs4 import BeautifulSoup
import requests

try:
    source = requests.get('https://realpython.github.io/fake-jobs/')
    source.raise_for_status() #used to raise an error if url is not found

    soup = BeautifulSoup(source.text, 'html.parser') 
    print(soup)

except Exception as e:
    print(e)