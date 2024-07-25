from flask import Blueprint, request, render_template, redirect
from random import choice, sample

from ..joke_form import JokeForm
from ..models import db, Joke, User

jokes = Blueprint('jokes', __name__)


@jokes.route('/')
def home():
    jokes = Joke.query.all()
    joke = choice(jokes)
    # return render_template('index.html', page="Home", joke=joke)
    return joke.to_dict()


@jokes.route('/jokes/<int:num>')
def all_jokes(num):
    num_jokes = Joke.query.count()
    print(F"Total jokes in DB: {num_jokes}")
    joke_ids = sample(range(1, num_jokes + 1), num)
    print(joke_ids)
    jokes = [ Joke.query.get(joke_id) for joke_id in joke_ids]
          
    # return render_template('alljokes.html', page="All Jokes", jokes=jokes)
    return {"jokes":[joke.to_dict() for joke in jokes]}


@jokes.route('/<int:id>')
def joke_by_id(id):
    joke = Joke.query.get(id)
    return joke.to_dict()


@jokes.route('/addjoke', methods=['POST'])
def add_jokes():
    data = request.json
    
    print(data)
    user = User.query.get(1)
    new_joke = Joke(
        joke_body=data['joke_body'],
        punchline=data['punchline'],
        rating=data['rating'],
        user= user
    )
        
    db.session.add(new_joke)
    db.session.commit()
    return new_joke.to_dict()

    # form = JokeForm()

    # if form.validate_on_submit():
        
    #     new_joke= Joke(
    #         joke_body=form.data['joke'],
    #         punchline=form.data['punchline'],
    #         rating=form.data['rating'],
    #     )
    #     db.session.add(new_joke)
    #     db.session.commit()
    #     return redirect('/api/jokes/jokes')
    
    # return render_template("jokeform.html", page="Joke Form", form=form, errors=form.errors)
