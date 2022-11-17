import asyncio
from random import randint
from time import sleep


URL = "https://pokeapi.co/api/v2/"

messages = ["Bruno", "Fioreze", "Está", "Construindo", "Esta", "Frase", "De", "Forma", "Assincrona"] 

async def show_message(message):
    delay = randint(1,5)
    await asyncio.sleep(delay)
    print(f"delay = {delay} / message = {message}")

async def main():
    await asyncio.gather(
        *[ show_message(message) for message in messages]
    )
    ...


asyncio.run(main())