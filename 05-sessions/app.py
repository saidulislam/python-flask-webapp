from flask import Flask, escape, render_template, request
from pydantic import BaseModel, validator
from pydantic import BaseModel, validator, ValidationError
from flask import session, redirect, url_for


class StockModel(BaseModel):
    """Class for parsing new stock data from a form."""
    stock_symbol: str
    number_of_shares: int
    purchase_price: float

    @validator('stock_symbol')
    def stock_symbol_check(cls, value):
        if not value.isalpha() or len(value) > 5:
            raise ValueError('Stock symbol must be 1-5 characters')
        return value.upper()


app = Flask(__name__)

app.secret_key = 'BS234523dS8ASDF39SSFA93JD7DFJ8EJ749JF74DHF'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', company_name='saidulislam.com', pname='Saidul (c)')


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')

        try:
            stock_data = StockModel(
                stock_symbol=request.form['stock_symbol'],
                number_of_shares=request.form['number_of_shares'],
                purchase_price=request.form['purchase_price']
            )
            print(stock_data)

            # Save the form data to the session object
            session['stock_symbol'] = stock_data.stock_symbol
            session['number_of_shares'] = stock_data.number_of_shares
            session['purchase_price'] = stock_data.purchase_price
            
            return redirect(url_for('list_stocks'))  # NEW!!
        
        except ValidationError as e:
            print(e)

    return render_template('add_stock.html')


@app.route('/example', methods=['GET', 'POST'])
def example():
    return 'an example'


@app.route('/stocks/')
def list_stocks():
    return render_template('stocks.html')


@app.route('/hello/<message>')
def hello_message(message):
    return f"<h2>Hello {escape(message)}!</h2>"

 
@app.route('/blog_posts/<int:post_id>')
def display_blog_post(post_id):
    return f'<h1>Blog Post #{post_id}...</h1>'