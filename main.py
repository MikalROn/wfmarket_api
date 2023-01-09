import aiohttp
import asyncio
import pandas as pd
from dataclasses import dataclass

class _WarframeMKT:
    '''Classe pai para setar parametros da api'''

    def __init__(self) -> None:
        self._endpoint: str = 'https://api.warframe.market/v1'

class WarMKT(_WarframeMKT):

    _counter = 0

    @property
    def get_items(self) -> dict:
        url: str = f'{self._endpoint}/items'
        return asyncio.run(self._request(url))['payload']['items']

    def get_info(self, item_url: str):
        url: str = f'{self._endpoint}/items/{item_url}'
        return asyncio.run(self._request(url))['payload']['item']

    def get_orders(self, item_url: str) -> dict:
        url: str = f'{self._endpoint}/items/{item_url}/orders'
        return asyncio.run(self._request(url))['payload']['item']

    @property
    def get_all_ordders(self):
        ''' [-*AVISO*-]
        ::> Metodo demora muito a ser executado em media 20 minutos
        '''
        items_url = self._all_items_url
        return asyncio.run(self._get_all_item_orders(items_url))

    async def _get_all_item_orders(self, items_url: list):
        async with aiohttp.ClientSession() as session:
            tasks = []
            results = []
            for item_url in items_url:
                task = asyncio.create_task(self._get_item_order(session, item_url))
                tasks.append(task)
            for task in asyncio.as_completed(tasks):
                result = await task
                results.append(pd.DataFrame(result['payload']['orders']))
            return results

    async def _get_item_order(self, session, item_url) -> dict:
        url = f'{self._endpoint}/items/{item_url}/orders'
        response = await asyncio.wait_for(session.get(url), timeout=1000)
        if response.status == 200:
            self._add_counter()
            print(self._counter)
            return await response.json()
        else:
            return await self._get_item_order(session, item_url)

    async def _request(self, url: str) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                if r.status == 200:
                    return await r.json()
                else:
                    raise ValueError(f'{r.status}')

    @property
    def _all_items_url(self) -> list:
        data = pd.DataFrame(self.get_items)
        return data['url_name'].tolist()


    def _add_counter(self):
        self._counter += 1

