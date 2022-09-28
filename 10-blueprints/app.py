import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask.logging import default_handler


app = Flask(__name__)

app.secret_key = 'BS234523dS8ASDF39SSFA93JD7DFJ8EJ749JF74DHF'

# Logging Configuration
file_handler = RotatingFileHandler('flask-stock-portfolio.log',
                                   maxBytes=16384,
                                   backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.INFO)  # NEW!
# You may also change the level based on the environment. 
# For example: log_level = logging.DEBUG if DEBUG else logging.INFO.
app.logger.addHandler(file_handler)

# Log that the Flask application is starting
app.logger.info('Starting the Flask Stock Portfolio App...')


# Import the blueprints
from project.stocks import stocks_blueprint
from project.users import users_blueprint

# Register the blueprints
app.register_blueprint(stocks_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/users')
