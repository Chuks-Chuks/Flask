import requests
blog_endpoint = 'https://api.npoint.io/3802efb26c49136e928e'
request_blog_posts = requests.get(blog_endpoint)
blog_json = request_blog_posts.json()
print(blog_json)