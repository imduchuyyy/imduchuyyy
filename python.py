import requests

def get_quote():
    response = requests.get(url = "https://quotes.rest/qod?language=en")
    
    data = response.json()

    if data["success"]["total"] < 1:
        return

    content = data["contents"]["quotes"][0]

    quote = content["quote"]
    author = content["author"]

    return quote, author

def write_to_readme(quote, author):
    f = open("README.md", "w")
    f.write("_**" + quote + "**_\n\n" + author)

    f.close()

def generate():
    quote, author = get_quote()

    write_to_readme(quote, author)

generate()
