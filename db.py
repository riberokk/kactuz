from kactuz import database, app
from kactuz.models import Users, Purchase, Address

with app.app_context():
    database.create_all()
