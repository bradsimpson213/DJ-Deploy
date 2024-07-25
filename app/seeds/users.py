from app.models import db, User, environment

# Adds a demo user, you can add other users here if you want
def seed_users():

    user1 = User(username="BradS", email="brad@gmail.com", password="password")
    user2 = User(username="demo123", email="demo_user@demo.com", password="demopassword")
    user3 = User(username="Andyman11", email="andy@gmail.com", password="password")

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")
        
    db.session.commit()