from app import app, db, User, Place, Comment, Like

with app.app_context():
    # 1) Tablo içindeki tüm kayıtları sil
    Comment.query.delete()
    Like.query.delete()
    User.query.delete()
    Place.query.delete()
    db.session.commit()


print("All records deleted and ID counters reset!")
