from flask import Flask, escape

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello Saidul!"


@app.route('/about')
def about():
    return '<h2>This is the about page</h2>'


@app.route('/example', methods=['GET', 'POST'])
def example():
    return 'an example'


@app.route('/stocks/')
def stocks():
    return '<h2>Stock List...</h2>'


@app.route('/hello/<message>')
def hello_message(message):
    return f"<h2>Hello {escape(message)}!</h2>"

 
@app.route('/blog_posts/<int:post_id>')
def display_blog_post(post_id):
    return f'<h1>Blog Post #{post_id}...</h1>'