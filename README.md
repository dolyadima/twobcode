
# 2bcode userlist project
this project was created for the qualifying stage IT Revolution 2022

## Environment setup

- clone from git
- run `cp .env.example .env`

### IF you want http:80
- run `mv nginx80.conf nginx.conf`
- open `nginx.conf` replace `REPLACE_DOMAIN` with your domain
- run `mv docker-compose80.yml docker-compose.yml`

### IF you want https:443
- run `mv nginx443.conf nginx.conf`
- open `nginx.conf` replace `REPLACE_DOMAIN` with your domain
- temporary comment block server 443 in `nginx.conf` 
- run `docker compose run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d YOUR_DOMAIN_HERE`
- back uncomment block server 443 in `nginx.conf`
- run `mv docker-compose443.yml docker-compose.yml`

### Finally
- run `docker compose up`
- enter to docker container `web` and run `./manage.py migrate`
- run `./manage.py collectstatic`  
