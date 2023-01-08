import asyncio

class WarframeMKT:
    ''' Classe pai para setar parametros da api'''
    def __init__(self) -> None:
        self._endpoint: str =  'https://api.warframe.market/v1'

class WarMKT(WarframeMKT):

    def get_all_items(self):
        ...
        