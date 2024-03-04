import json
import time
import psutil
from duckduckgo_search import DDGS

# Inisialisasi waktu awal
start_time = time.time()

with DDGS() as ddgs:
    results = [r for r in ddgs.text("jokowi site:kompas.com", max_results=1000)]

# Hitung waktu yang diperlukan
elapsed_time = time.time() - start_time

# Menyimpan hasil pencarian ke dalam file JSON
link=[]
for r in results:
    link.append(r['href'])
    
# Hitung penggunaan memori
memory_usage = psutil.Process().memory_info().rss
print(f"jumlah link yang diambil dalam", len(link))
print("Waktu yang diperlukan:", elapsed_time, "seconds")
print("Penggunaan memori:", memory_usage / (1024 * 1024), "MB") 