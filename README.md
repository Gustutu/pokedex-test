# Pokedex




## environement


### pipenv : 

deploy dev env localy using pipenv
once pienv install just run pipenv install

### .env :

copy .env.example in and place it in pokedex/.env and set env variables

### postgresql :

run postgresql from docker-compose

`
docker-compose --env-file pokedex/.env up db 
`

### Full backend :
if want you can run full backend (postgresql and the pokedex)

`
docker-compose --env-file pokedex/.env up db 
`

### pylint args

`
        "--load-plugins=pylint_django",
        "--django-settings-module=pokedex.settings",
        "--disable=C0412,E1101,C0103,C0114,C0209,W0223"
`