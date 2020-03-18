# Coronavirus CoVid-19 Social Platform (https://covid.social)

THIS IS NOT AN OFFICIAL GOVERNMENT WEBSITE AND IT IS NOT INTENDED TO OFFER HELP IN CASE
OF EMERGENCY ! (AT LEAST NOT YET !)

The aim of this platform is to try and help people in need during this awful pandemic. The main goals are:

* Implement country-specific maps
* Give users the possibility to mark themselves as possible infected or infected when the have a proof
* Let users help other users in need. For example, people in quarantine should be able to ask help with groceries
* Implement translations for as many languages as possible

The possibilities are endless. Any ideas are more than welcome.

While governments and big tech companies are doing their part of the job (at least some of them), I think the open source community can achieve so much more if we join forces ! 

I was sitting these days and thinking how can I help ? How can I do something for people ? And this is what I came up with. 

I really hope that at least some of you will appreciate my intention and maybe even contributing to this project. 

I am working on this late in the evenings as I am the father of a 1.5 years old boy, expecting a daughter any day now and working remotely from 08:00 to 16:00    

Let's make something useful for our fellows, for us. 

This README is a draft and I will do my best to update it as often as I can. 

# Quick QA
```
Q: Is this platform funded ?
A: NO

Q: Where is it hosted ? 
A: Private server, in Paris, France 

Q: How is it deployed ? 
A: For now, using Capistrano

Q: Why Django ?
A: Scalable and perfect for RAD

Q: What's with this code ?
A: The base of this code is something that I use for prototyping apps.

Q: Is it production-ready ? 
A: Kind of. Needs testing, but I use more than 70% of it in production environments.
```


## Local setup

### Requirements
* docker
* docker compose

#### Clone this repository
```shell script
git clone git@github.com:calinrada/covid.git \
  && cd covid \
  && cp .env.dist .env \
  && db.env.dist db.env
```

## Configuration

You need to set environment variables in your local .env file and db.env before you start docker. AWS is not needed for local development.

#### Docker
```shell script
# Create external volumes
docker volume create covid_postgres_data \
    && docker volume create covid_redis_data \
    && docker volume create covid_rabbitmq_data \
    && docker volume create covid_elasticsearch_data
```

Before running the next commands, edit .env file and add your settings

```shell script
docker-compose -f docker/docker-compose.local.yml up --build
```

After the image is build, create rabbitmq users and vhosts:

```shell script
docker-compose -f docker/docker-compose.local.yml exec rabbitmq rabbitmqctl add_user covid_dev covid_dev \
  && docker-compose -f docker/docker-compose.local.yml exec rabbitmq rabbitmqctl add_vhost covid_dev \
  && docker-compose -f docker/docker-compose.local.yml exec rabbitmq rabbitmqctl set_permissions -p covid_dev covid_dev ".*" ".*" ".*" \
  && docker-compose -f docker/docker-compose.local.yml restart rabbitmq
```

Now run migrations

```shell script
./manage.sh ./manage.py migrate
```

TIP: If you want to generate a secret key django way: 

```shell script
$ python
> from django.core.management.utils import get_random_secret_key
> get_random_secret_key()
```

## Assets

Assets are managed by gulp. Check <code>gulpfile.js</code> from the project root. The project 
contains assets to start with check <code>static-dev/assets/frontend/</code> . 

The project is SCSS ready. 

**Common assets comands:**

<code>$ gulp build</code> to build js and css

<code>$ gulp watch</code> to compile js or css everytime a file has changed

Unfortunately you will need to have nodejs and npm installed on your local machine. Hopefully we will have 
a docker image for this soon.
