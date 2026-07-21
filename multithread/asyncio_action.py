import asyncio

# Scenario 1: Basic use - calling the same function multiple times with different parameters
async def work(url):
    # do stuff
    return f"Result for {url}"

async def run():
    urls = ["http://cafecito.tech", "http://medium.com", "http://demo.com"]
    tasks = [work(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")
    
if __name__ == "__main__":
    run()