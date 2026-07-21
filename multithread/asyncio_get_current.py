import asyncio

async def mia_coroutine():

    print("Ciao, sono una coroutine!")
    
    current_task = asyncio.current_task()
    
    loop = asyncio.get_running_loop()
    
    print(f"Task corrente: {current_task}")
    
    print(f"Event loop corrente: {loop}")
    
    
if __name__ == "__main__":
    asyncio.run(mia_coroutine())