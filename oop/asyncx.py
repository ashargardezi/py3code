import time
import asyncio
import requests

async def function1():
    
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram1.ico", "wb").write(response.content)
    await asyncio.sleep(2)
    print("func1")
    return "result1"
async def function2():
    
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
    
    print("func2")
    return "result1"
async def function3():
    
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)
  
    print("func3")
    return "result1"
# async def main():
#    x= await asyncio.gather()
#    task=asyncio.create_task(function2())    
#    await function1()
#    await function2()
#    await function3()
# asyncio.run(main())
async def main():
    x= await asyncio.gather(
       function1(),
       function2(),
       function3(),
     )
    print(x)
asyncio.run(main())