from duckduckgo_search import DDGS

results = DDGS().text("jokowi site:kompas.com", max_results=100)
print(results)