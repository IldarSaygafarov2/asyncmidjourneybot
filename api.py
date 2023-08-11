import asyncio
import json

import aiohttp

import config

url = "https://api.thenextleg.io/v2/"
msg_url = "https://api.thenextleg.io/v2/message"


async def make_reqeust(prompt):
    payload = json.dumps({
        "cmd": "imagine",
        "msg": f"{prompt}",
    })
    headers = {
        'Authorization': f'Bearer {config.API_TOKEN}',
        'Content-Type': 'application/json'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=headers) as resp:
            result = await resp.json()
            return result


async def get_result_by_message_id(message_id: str):
    headers = {
        'Authorization': f'Bearer {config.API_TOKEN}',
    }
    async with aiohttp.ClientSession() as session:
        await asyncio.sleep(60)
        async with session.get(f"{msg_url}/{message_id}", headers=headers) as resp:
            return await resp.json()
