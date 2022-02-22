# Pokedex




## environement


### pipenv : 

- install pipenv

- in root folder of repository run : 


```shell
pipenv shell
```

- run followin command to install packages in current virtual env


```shell
pipenv install
```

### set .env :

- copy .env.example and place it in pokedex/.env 
- set env variables

### postgresql :

run postgresql from docker-compose :


```shell
docker-compose --env-file pokedex/.env up db 
```

### Run backend
in pokedex folder run :

```shell
./manage.py runserver
```
### Full backend :
if don't want to deploy the environnement on your local machine you can run full backend (postgresql and the pokedex app) directly from the docker compose file.


```shell
docker-compose --env-file pokedex/.env up db 
```

### pylint args

 
```shell
--load-plugins=pylint_django \
--django-settings-module=pokedex.settings \
--disable=C0412,E1101,C0103,C0114,C0209,W0223
```