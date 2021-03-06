# news_board
Test web application with REST API.
This application will has to run as a docker container.

- link to working app:

[https://news-board-rest-api.herokuapp.com/](https://news-board-rest-api.herokuapp.com/)

- link to REST API documentation:

[postman documentation](https://documenter.getpostman.com/view/11911939/T17Kc667?version=latest)



## requirements for run application
installed docker engine:
[link to install docker](https://docs.docker.com/engine/install/)

installed docker-compose:
[link to install docker-compose](https://docs.docker.com/compose/install/)

installed git:
[link to install git](https://git-scm.com/downloads)

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
## link to deploied app

[https://news-board-rest-api.herokuapp.com/](https://news-board-rest-api.herokuapp.com/)

## command to clear upvotes of posts:
```bash
docker-compose run web python3 /code/manage.py clear_votes
```

## REST API docs:

**REST API documentation link:**

- [postman documentation](https://documenter.getpostman.com/view/11911939/T17Kc667?version=latest)

**For work with API you will need registrate in app:**

- [link to register](https://news-board-rest-api.herokuapp.com/accounts/register)

**Endpoints to work with api:**

- main url for api: 

*"/api"*

- url for get you auth token:

*"/api/api-token-auth/"*

- url for get all posts without auth:

*"/api/posts/all/"*

- url for get, create a posts:

*"/api/posts/"*

- url for put, patch, delete a posts:

*"/api/posts/{post_id}/"*

- url for patch a upvotes in post:

*"/api/upvote/{post_id}/"*

- url for get all comments without auth:

*"/api/comments/"*

- url for get, post a comments:

*"/api/comments/{post_id}/"*

- url for put, patch, delete a comments:

*"/api/comments/{post_id}/{comment_id}"*

