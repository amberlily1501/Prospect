from app.tools.fetch import fetch_page

text = fetch_page("https://www.rapidetechnologies.com")

print(text[:1000])