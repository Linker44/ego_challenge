Esto codigo fue creado para ser entregado en el code challenge de EGO

Requerimientos:

- tener python instalado

Instrucciones:

1. source ./env/bin/activate
2. python3 -m pip install -r requirements.txt
3. python3 manage.py migrate
4. python3 manage.py createsuperuser --username=admin --email=admin@example.com
5. python3 manage.py runserver

API:

Si no se esta haciendo el request como super usuario solo se aceptara GET.
Si se esta logueado como el usuario se aceptan PATCH, PUT, GET, POST, DELETE

/auto/ lista todos los autos con sus fichas y caracteristicas

acepta los siguientes filtros:

- /auto/fecha_modelo={fecha}
  - /auto/fecha_modelo_gt={fecha} lista todos los autos que tengan fecha igual o superior
  - /auto/fecha_modelo_lt={fecha} lista todos los autos que tengan fecha igual o inferior
- /auto/precio={precio}
  - /auto/precio_gt={precio} lista todos los autos que tengan precio igual o superior
  - /auto/precio_lt={precio} lista todos los autos que tengan precio igual o inferior
- /auto/tipo={auto/pickup/comercial/suv/crossover} lista todos los autos de ese tipo

ej:
{
"url": "http://127.0.0.1:8000/auto/1/",
"ficha": {
"url": "http://127.0.0.1:8000/ficha/1/",
"hero": {
"id": 1,
"pre_titulo": "toyota camri",
"titulo": "El mejor Auto que podes soniar",
"descripcion": "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum",
"image": null
},
"caracteristicas": [
{
"id": 1,
"titulo": "manual",
"descripcion": "lorem ipsum",
"image": null,
"ficha": 1
},
{
"id": 2,
"titulo": "Vidrios reforzados",
"descripcion": "dolor isem",
"image": null,
"ficha": 1
}
],
"prestaciones": [
{
"id": 1,
"titulo": "Nuevos motores",
"descripcion": "lorem ipsum dolor iset",
"image": null,
"ficha": 1
}
]
},
"nombre": "toyota camri",
"tipo": "auto",
"fecha_auto": "2024-03-10",
"precio": 30000,
"image": null
},

/ficha/ lista todas las fichas
ej:

{
"url": "http://127.0.0.1:8000/ficha/1/",
"hero": {
"id": 1,
"pre_titulo": "toyota camri",
"titulo": "El mejor Auto que podes soniar",
"descripcion": "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum",
"image": null
},
"caracteristicas": [
{
"id": 1,
"titulo": "manual",
"descripcion": "lorem ipsum",
"image": null,
"ficha": 1
},
{
"id": 2,
"titulo": "Vidrios reforzados",
"descripcion": "dolor isem",
"image": null,
"ficha": 1
}
],
"prestaciones": [
{
"id": 1,
"titulo": "Nuevos motores",
"descripcion": "lorem ipsum dolor iset",
"image": null,
"ficha": 1
}
]
}

Tanto /auto/ como /ficha/ permiten la creacion y actualizacion de ficha.

/ficha/tambien acepta la asignacion de un auto con su id mediante "auto": {id}.

/admin/ nos permite ingresas al django admin
