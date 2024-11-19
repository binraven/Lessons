import asyncio


async def start_strongman(name, power):

    print(f"Силач {name} начал соревнования.")

    for i in range(1, 6):
        print(f"Силач {name} поднял {i}")
        await asyncio.sleep(10/power)

    print(f"Силач {name} закончил соревнования.")


async def start_tournament():

    body1 = asyncio.create_task(start_strongman("Pasha", 3))
    body2 = asyncio.create_task(start_strongman("Denis", 4))
    body3 = asyncio.create_task(start_strongman("Ka4ok", 5))
    await body1
    await body2
    await body3


asyncio.run(start_tournament())