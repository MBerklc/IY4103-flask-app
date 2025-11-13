from app import app, db, User, Place, Comment, Like

with app.app_context():

    User.query.filter(Comment.id > 0).delete()

    db.session.commit()

print("Sample data added!")