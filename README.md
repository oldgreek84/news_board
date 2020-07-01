# news_board

# command to clear upvotes of posts:

python3 manage.py clear_votes

# work  with api:

main url for api: "/api"
url for posts: "/api/posts"url
url for comments: "/api/comments"

# example to add post with curl:
curl -X POST -H "Content-Type: application/json"
     -d '{"title":{title of post}, "link":{link to post news}, "author_name":{author name}' {url}/api/posts/
