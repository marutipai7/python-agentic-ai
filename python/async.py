import asyncio

async def greet(name):
    print(f"hello {name}")
    await asyncio.sleep(2)
    print(f"goodbye {name}")

async def main():
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Charlie")
    )



asyncio.run(main())