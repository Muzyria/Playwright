import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Привет")
    await asyncio.sleep(1)
    print("Пока")

async def say_bye():
    await asyncio.sleep(3)  # Теперь задержка 4 секунды
    print("До свидания!")

async def main():
    await asyncio.gather(say_hello(), say_hello(), say_bye())

asyncio.run(main())

