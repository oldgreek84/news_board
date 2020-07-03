# news_board
Test web application with REST API.
This application will has to run as a docker container.

## requirements for run application
installed docker engine:

(link to install)[https://docs.docker.com/engine/install/]

installed docker-compose:

(link to install)[https://docs.docker.com/compose/install/]

installed git:

(link to install)[https://git-scm.com/downloads]

## steps to install and run application:
* clone repository:
```bash
git clone https://github.com/oldgreek84/news_board.git
```
* enter to directory with running code(contain Dockerfile):
```bash
cd news_board/news-board/
```
* create migrations for database:
```bash
docker-compose run web python3 /code/manage.py migrate
```
* create superuser for work with application:
```bash
docker-compose run web python3 /code/manage.py createsuperuser
```
* run application with docker container(needs some time):
```bash
docker-compose up
```
* now you will may open application in browser for address:
*localhost:8000*

* for close docker file and stop application:
```bash
docker-compose down
```

## command to clear upvotes of posts:
```bash
docker-cpmpose run web python3 /code/manage.py clear_votes
```

## REST API docs:
endpoints to work with api:

*main url for api: *"/api"*

url for get, post a posts:

*"/api/posts/"*

url for put, patch, delete a posts:

*"/api/posts/{post_id}/"*

url for patch a upvotes in post:

*"/api/votes/{post_id}/"*

url for get, post a comments:

*"/api/comments/"*

url for put, patch, delete a comments:

*"/api/comments/{comment_id}/"*

## example to work api with curl:
get all posts from site:
```bash
curl -X GET -H "Content-Type: application/json" localhost:5000/api/posts/
```
post new post to site:
```bash
curl -X POST -H "Content-Type: application/json"
     -d '{"title":{title of post}, "link":{link to post news}, "author_name":{author name}' {url}/api/posts/
```
