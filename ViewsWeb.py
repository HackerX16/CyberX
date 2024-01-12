import aiohttp
import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from PIL import Image, ImageDraw, ImageFont

# Solicita o URL do site e a quantidade de visitas
url = input("Digite o URL do site que deseja visitar: ")
num_visitas = int(input("Digite a quantidade de visitas desejada: "))

# Função para fazer uma visita ao site de forma síncrona
def fazer_visita(url):
    response = requests.get(url)
    if response.status_code == 200:
        return "Visita realizada com sucesso!"
    else:
        return "Erro ao visitar o site"

# Função para realizar as visitas ao site utilizando asyncio e aiohttp
async def fazer_visita_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return "Visita realizada com sucesso!"
            else:
                return "Erro ao visitar o site"

# Função para realizar as visitas ao site utilizando multiprocessing
def fazer_visita_multiprocessing(url):
    response = requests.get(url)
    if response.status_code == 200:
        return "Visita realizada com sucesso!"
    else:
        return "Erro ao visitar o site"

# Função para realizar as visitas ao site utilizando concurrent.futures e threading
def realizar_visitas_threading():
    with ThreadPoolExecutor() as executor:
        results = executor.map(fazer_visita, [url] * num_visitas)
    return results

# Função para realizar as visitas ao site utilizando concurrent.futures e multiprocessing
def realizar_visitas_multiprocessing():
    with ProcessPoolExecutor() as executor:
        results = executor.map(fazer_visita_multiprocessing, [url] * num_visitas)
    return results

# Função para realizar as visitas ao site utilizando asyncio e aiohttp
async def realizar_visitas_asyncio():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for _ in range(num_visitas):
            tasks.append(asyncio.ensure_future(fazer_visita_async(url)))
        results = await asyncio.gather(*tasks)
    return results

# Realiza as visitas ao site utilizando concurrent.futures e threading
results_threading = realizar_visitas_threading()

# Realiza as visitas ao site utilizando concurrent.futures e multiprocessing
results_multiprocessing = realizar_visitas_multiprocessing()

# Realiza as visitas ao site utilizando asyncio e aiohttp
loop = asyncio.get_event_loop()
results_asyncio = loop.run_until_complete(realizar_visitas_asyncio())

# Imprime os resultados das visitas utilizando concurrent.futures e threading
for result in results_threading:
    print(result)

print("Todas as visitas utilizando concurrent.futures e threading foram concluídas.")

# Imprime os resultados das visitas utilizando concurrent.futures e multiprocessing
for result in results_multiprocessing:
    print(result)

print("Todas as visitas utilizando concurrent.futures e multiprocessing foram concluídas.")

# Imprime os resultados das visitas utilizando asyncio e aiohttp
for result in results_asyncio:
    print(result)

print("Todas as visitas utilizando asyncio e aiohttp foram concluídas.")
