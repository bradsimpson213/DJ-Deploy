from app.models import db, Joke, User, environment
from random import choice

# Adds seed jokes, you can add other jokes here if you want
def seed_jokes():

    users = [ User.query.get(num) for num in range(1, 4) ]

    starter_jokes = [
        {   "joke_body": "What do mermaids wash their fins with?",
            "punchline": "Tide...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Did you know in King Arthur's time, one of the knights of the round table collected taxes?",
            "punchline": "His name was Sir Charge...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What did the fried rice say to the shrimp?",
            "punchline": "Don't Wok away from me...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Did you hear Steve Harvey and his wife got into a fight?",
            "punchline": "It was a real family feud...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What kind of car does an egg drive?",
            "punchline": "A Yolkswagon...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What do you call someone who gets mad when they don't have any bread?",
            "punchline": "Lack toast intolerant...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What did the plumber say to the singer?",
            "punchline": "Nice pipes...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What do you call a lazy doctor?",
            "punchline": "Dr Doo-little...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Did you know on average people want 3 covers on the bed at all times?",
            "punchline": "That's just a blanket statement...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What did the pot eat on its birthday?",
            "punchline": "Pancakes...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Where would you grow a chef?",
            "punchline": "Bakersfield...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What do you call a camel in a drought?",
            "punchline": "A dry humper...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "How do you get a squirrel out of a tree?",
            "punchline": "Show him your nutts...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "Why don't eggs tell jokes?",
            "punchline": "They'd crack each other up...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Did you hear the rumor about butter?",
            "punchline": "Well, I'm not going to spread it...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "How many tickles does it take to make an octopus laugh?",
            "punchline": "Ten tickles...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What concert costs just 45 cents?",
            "punchline": "50 Cent featuring Nickelback...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "How do you make a tissue dance?",
            "punchline": "You put a little boogie in it...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Why did the math book look so sad?",
            "punchline": "Because of all of its problems...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What do you call cheese that isn't yours?",
            "punchline": "Nacho cheese...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What kind of shoes do ninjas wear?",
            "punchline": "Sneakers...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "How does a penguin build its house?",
            "punchline": "Igloos it together...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "When does a joke become a dad joke?",
            "punchline": "When it becomes apparent...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What do sprinters eat before a race?",
            "punchline": "Nothing, they fast...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Why do melons have weddings?",
            "punchline": "Because they cantaloupe...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What's the difference between a poorly dressed man on a tricycle and a well-dressed man on a bicycle?",
            "punchline": "Attire...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What happens when you go to the bathroom in France?",
            "punchline": " European...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "A cheese factory exploded in France...",
            "punchline": "Da brie is everywhere...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Why did the old man fall in the well?",
            "punchline": "Because he couldn't see that well...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Why did the invisible man turn down the job offer?",
            "punchline": "He couldn't see himself doing it...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Want to hear a joke about construction?",
            "punchline": " I'm still working on it...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "How does Moses make his coffee?",
            "punchline": "Hebrews it...",
            "rating": "G",
            "user": choice(users) 
        },
        {   "joke_body": "I was just reminiscing about the beautiful herb garden I had when I was growing up...",
            "punchline": "Good thymes...",
            "rating": "G",
            "user": choice(users) 
        },
        {   "joke_body": "Why did the scarecrow win an award?",
            "punchline": "Because he was outstanding in his field...",
            "rating": "G",
            "user": choice(users) 
        },
        {   "joke_body": "Why was the coach yelling at a vending machine?",
            "punchline": "He wanted his quarter back...",
            "rating": "G",
            "user": choice(users) 
        },
        {   "joke_body": "Why do vampires seem sick?",
            "punchline": "They're always coffin...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Did you hear about the Italian chef who died?",
            "punchline": "He pasta way...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What did the Ranch say when someone opened the refrigerator door?",
            "punchline": "Close the door, I'm dressing...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "What do you call it when a group of apes starts a company?",
            "punchline": "Monkey business...",
            "rating": "G",
            "user": choice(users) 
        },
        {   "joke_body": "How can you tell it’s a dogwood tree?",
            "punchline": "By the bark...",
            "rating": "G",
            "user": choice(users) 
        },
        {   "joke_body": "What did the accountant say while auditing a document?",
            "punchline": "This is taxing...",
            "rating": "G",
            "user": choice(users) 
        },
        {   "joke_body": "Why are spiders so smart?",
            "punchline": "They can find everything on the web...",
            "rating": "G",
            "user": choice(users) 
        },
        {   "joke_body": "What do you call two octopuses that look the same?",
            "punchline": "Itenticle...",
            "rating": "G",
            "user": choice(users) 
        },
        {   "joke_body": "How do you weigh a millennial?",
            "punchline": "In Instagrams...",
            "rating": "G",
            "user": choice(users) 
        },
        {   "joke_body": "Why don’t crabs give to charity?",
            "punchline": "Because they’re shellfish...",
            "rating": "G",
            "user": choice(users) 
        },
        {   "joke_body": "How do you tell the difference between an alligator and a crocodile?",
            "punchline": "You will see one later and one in a while...",
            "rating": "G",
            "user": choice(users) 
        },
        {   "joke_body": "What kind of exercises do lazy people do?",
            "punchline": "Diddly squats...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Why did the coffee file a police report?",
            "punchline": "It got mugged...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "How do trees access the internet?",
            "punchline": "They log in...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "A slice of apple pie is $2.50 in Jamaica and $3.00 in the Bahamas...",
            "punchline": "These are the pie rates of the Caribbean...",
            "rating": "G",
            "user": choice(users)
        },

        {   "joke_body": "How do you find Will Smith in a snowstorm?",
            "punchline": "You look for fresh prints...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What do you call a bundle of hay in a church?",
            "punchline": "Christian Bale...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "What’s an astronaut’s favorite part of the computer?",
            "punchline": "The space bar...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Why did the scarecrow win an award?",
            "punchline": "Because he was outstanding in his field...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What did the grape do when he got stepped on?",
            "punchline": "He let out a little wine...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "How did Darth Vader know what Luke got him for Christmas?",
            "punchline": "He felt his presents...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Why can’t you trust atoms?",
            "punchline": "They make up everything...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What was Forrest Gump’s email password?",
            "punchline": "1forrest1...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "What did one ocean say to the other ocean?",
            "punchline": "Nothing, they just waved...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "Why don’t oysters share their pearls?",
            "punchline": "Because they’re shellfish...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What do you call the boss at Old McDonald’s Farm?",
            "punchline": "The CIEIO...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "How do astronomers organize a party?",
            "punchline": " They planet...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "How do you deal with a fear of speed bumps?",
            "punchline": "You slowly get over it...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "What was the most ground-breaking invention?",
            "punchline": "A shovel...",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "How did the hipster burn his mouth?",
            "punchline": "He ate the pizza before it was cool...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "What did the grape do when he got stepped on?",
            "punchline": "He let out a little wine....",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "I just watched a program about beavers...",
            "punchline": "It was the best dam program I've ever seen...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "I wrote a song about a tortilla...",
            "punchline": "Well actually, it’s more of a wrap...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "If you ever get cold, just stand in a corner...",
            "punchline": "They’re usually 90 degrees...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "I used to hate facial hair...",
            "punchline": "But then it grew on me...",
            "rating": "PG",
            "user": choice(users)
        },
        {   "joke_body": "I read a book today about fixing boats...",
            "punchline": "...it was riveting",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "My friend David lost his id...",
            "punchline": "...now I just call him Dave",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "where does a lizard go after it loses its tail?",
            "punchline": "...a retail store",
            "rating": "G",
            "user": choice(users)
        },
        {   "joke_body": "how much does it cost Santa to park his sleigh?",
            "punchline": "...Nothing! It's on the house",
            "rating": "G",
            "user": choice(users)
        }
    ]
  
    [ db.session.add(
        Joke(
            joke_body=joke["joke_body"], 
            punchline=joke["punchline"],
            rating=joke["rating"],
            user=joke["user"]
        )
    ) for joke in starter_jokes ]
      
    db.session.commit()



# Uses a raw SQL query to TRUNCATE the jokes table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_jokes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.jokes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM jokes")
        
    db.session.commit()