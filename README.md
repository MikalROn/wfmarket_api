# Api Warframe marketing

<p >Classe que busca dados da api do warframe market 
sobre os item e as orders desses items</p>

> Para usar basta importar a classe
````python
from wfmarket_api import WarMKT

api = WarMKT()
````
## Items 

<p>.....</p>

> Para retornar os itens basta chamar <mark>get_items</mark>


````python
from wfmarket_api import WarMKT

api = WarMKT()

items = api.get_items
print(items)
```` 

> Para retornar informações sobre os itens basta chamar <mark>get_info</mark> que recebe a url do item

````python
from wfmarket_api import WarMKT

api = WarMKT()

info = api.get_info('secura_dual_cestra')
print(info)
````