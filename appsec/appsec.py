
async def main(
    api_token: str,
    commit_from: str = None,
    commit_to: str = None
):
    # tasks = asyncio.create_task(
    #
    # )
    # try:
    #     await asyncio.gather(*tasks)
    # except Exception as ex:
    #     print(str(ex))
    try:
        raise Exception("Raising exception")
    except Exception as ex:
        print(str(ex))
        raise ex

