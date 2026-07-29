##########################################################################################
###### qui, asyncio gestisce solo un thread che esegui multi task in modo concorrente. ####
### pero, devi utilizzare libreri asycronous al fine di rendere il processo concorrente ###
#----------------------------------------------------------------------------------------#
# Output: ~1.2 secondi (tutte partono insieme!)
import aiohttp
import time
import asyncio
urls = ["https://www.uninettunouniversity.net/it/default.aspx"] * 10


async def scarica_async(session, url):
    async with session.get(url) as response:
        return response.status
    
    
async def scarica_asyncio(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [scarica_async(session, url) for url in urls]  
        risultati = await asyncio.gather(*tasks)
        return risultati
    
    
inizio = time.time()
asyncio.run(scarica_asyncio(urls))