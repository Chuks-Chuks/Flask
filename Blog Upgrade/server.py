from flask import Flask, render_template, request
import requests
from EMAIL import Email

app = Flask(__name__)

blog_endpoint = 'https://api.npoint.io/3802efb26c49136e928e'
request_blog_posts = requests.get(blog_endpoint)
blog_json = request_blog_posts.json()
print(blog_json)


@app.route('/')
def home():
    return render_template('index.html', posts=blog_json)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone']
        message = request.form['message']

        final_message = f'Name: {username}\nEmail: {email}\nPhone Number: {phone_number}\nMessage: {message}'
        Email(email, final_message)
        return render_template('contact.html', heading_message=True)
    else:
        return render_template('contact.html', heading_message=False)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    read_blog = None
    for blog_post in blog_json:
        if blog_post['id'] == blog_id:
            read_blog = blog_post
    return render_template('post.html', open_blog=read_blog)


if __name__ == '__main__':
    app.run(debug=True)