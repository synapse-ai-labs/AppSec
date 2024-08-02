import os
import json
# import aiohttp

URL = ''


async def create_run(session, repo: str, to_event: str, from_event: str = None):
    async with session.post(url=URL, json={
        'repo': repo,
        'to_event': to_event,
        'from_event': from_event
    }) as response:
        return await response.json()


async def main(
    repo: str,
    to_event: str,
    from_event: str = None
):
    api_token = os.getenv('AUTOGRAD_API_TOKEN')
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    data = {
        "headers": headers,
        "repo": repo,
        "to_event": to_event,
        "from_event": from_event
    }
    raise Exception(json.dumps(data))
    # try:
    #     async with aiohttp.ClientSession(headers=headers) as session:
    #         result = await create_run(session, repo, to_event, from_event)
    #         print(result)
    # except aiohttp.ClientError as ex:
    #     print(str(ex))
    #

