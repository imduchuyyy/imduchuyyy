from random_word import RandomWords
import requests

def get_quote() -> tuple:
    response = requests.get(url = "https://api.quotable.io/random")

    if response.status_code != 200:
        return "Everything will be ok", "Terry"
    
    data = response.json()

    content = data["content"]
    author = data["author"]

    return content, author

def write_to_readme(quote, author):
    f = open("README.md", "w")
    f.write("_**" + quote + "**_\n\n" + author)

    f.close()

def generate():
    quote, author = get_quote()
    write_to_readme(quote, author)

generate()
