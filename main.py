import os

import psutil
import asyncio
import aiohttp
import logging
from dotenv import load_dotenv

load_dotenv()

ALERTS_LOGS = os.getenv('ALERTS_LOGS')
ALERT_PERCENT = int(os.getenv('ALERT_PERCENT'))
ALERT_API = os.getenv('ALERT_API')
ALERT_API_ERROR = os.getenv('ALERT_API_ERROR')

logging.basicConfig(
    filename=ALERTS_LOGS,
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


async def alert_request(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.text()
                    return data
                else:
                    return f'{ALERT_API_ERROR}, status: {response.status}'
        except aiohttp.ClientConnectorError as e:
            return f'{ALERT_API_ERROR} - {e}'


async def monitor_memory():
    if psutil.virtual_memory().percent > ALERT_PERCENT:
        alert_response = await alert_request(ALERT_API)
        logging.debug(alert_response)


async def main():
    while True:
        await monitor_memory()
        await asyncio.sleep(1)

asyncio.run(main())
