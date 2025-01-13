import requests

def get_quote() -> tuple:
    response = requests.get(url = "https://quotes-api-self.vercel.app/quote")

    if response.status_code != 200:
        return "Everything will be ok", "Terry"
    
    data = response.json()

    content = data["quote"]
    author = data["author"]

    return content, author

def write_to_readme(quote, author):
    f = open("README.md", "w")
    f.write("<i>" + quote + "</i>\n\n" + author)

    f.close()

def generate():
    quote, author = get_quote()
    write_to_readme(quote, author)

generate()
