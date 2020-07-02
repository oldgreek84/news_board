# news_board
Test web application with REST API.

## after clone:
create migrsations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
create super_user:
```bash
python3 manage.py createsuperuser
```
run test server:
```bash
python3 manage.py runserver 5000
```

## command to clear upvotes of posts:

python3 manage.py clear_votes

## work  with api:
```bash
main url for api: "/api"
url for get, post a posts: "/api/posts/"
url for put, patch, delete a posts: "/api/posts/{post_id}/"

url for patch a upvotes in post: "/api/votes/{post_id}/"

url for get, post a comments: "/api/comments/"
url for put, patch, delete a comments: "/api/comments/{comment_id}/"
```

## example to work api with curl:
get post
```bash
curl -X GET -H "Content-Type: application/json" localhost:5000/api/posts/
```
post post
```bash
curl -X POST -H "Content-Type: application/json"
     -d '{"title":{title of post}, "link":{link to post news}, "author_name":{author name}' {url}/api/posts/
```
