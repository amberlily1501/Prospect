from app.tools.search import search_web

results = search_web("Rapide Technologies Lahore")

for result in results:
    print(result)
    print()