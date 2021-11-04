from flask import Flask 
from .config import Config
from .seeds import seed_commands
from flask_migrate import Migrate

from .api.user_routes import user_routes
from .api.joke_routes import jokes

from .models import db


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(jokes, url_prefix='/api/jokes')
app.register_blueprint(user_routes, url_prefix='/api/users')

Migrate(app, db)

app.cli.add_command(seed_commands)

# @app.route('/')
# def home():
#     jokes = Joke.query.all()
#     joke = choice(jokes)
#     return render_template('index.html', page="Home", joke=joke)


# @app.route('/jokes')
# def all_jokes():
#     jokes = Joke.query.all()
#     return render_template('alljokes.html', page="All Jokes", jokes=jokes)



# @app.route('/addjoke', methods=['GET', 'POST'])
# def add_jokes():
#     form = JokeForm()

#     if form.validate_on_submit():
        
#         new_joke= Joke(
#             joke_body=form.data['joke'],
#             punchline=form.data['punchline'],
#             rating=form.data['rating'],
#         )
#         db.session.add(new_joke)
#         db.session.commit()
#         return redirect('/jokes')
    
#     return render_template("jokeform.html", page="Joke Form", form=form, errors=form.errors)
