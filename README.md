# news_board

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

## example to add post with curl:
```bash
curl -X POST -H "Content-Type: application/json"
     -d '{"title":{title of post}, "link":{link to post news}, "author_name":{author name}' {url}/api/posts/
```
