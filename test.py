from asyncflows import AsyncFlows



async def main():
    # Load the flow from the file
    flow = AsyncFlows.from_file("test.yaml")
    # Run the flow
    result = await flow.set_vars(name="Roba").run()
    # Print the result
    print(result)


import asyncio
asyncio.run(main())