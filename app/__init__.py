from flask import Flask 
from .config import Config
from .seeds import seed_commands
from flask_migrate import Migrate
from flask_cors import CORS

from .api.user_routes import user_routes
from .api.joke_routes import jokes

from .models import db
import os

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(jokes, url_prefix='/api/jokes')
app.register_blueprint(user_routes, url_prefix='/api/users')

Migrate(app, db)

# Application Security
CORS(app)

app.cli.add_command(seed_commands)


# Since we are deploying with Docker and Flask,
# we won't be using a buildpack when we deploy to Heroku.
# Therefore, we need to make sure that in production any
# request made over http is redirected to https.
# Well.........
@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)
            

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    if path == 'favicon.ico':
        return app.send_static_file('favicon.ico')
    return app.send_static_file('index.html')