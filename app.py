from api import createApp, db
from dotenv import load_dotenv

load_dotenv()

app = createApp("development")

with app.app_context():
    db.create_all() # Creates the tables if not exist

if __name__ == "__main__":
    app.run()