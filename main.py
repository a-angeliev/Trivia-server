from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
# import smtplib
from config import DevApplication
from db import db
from resources.routes import routes

app = Flask(__name__)
app.config.from_object(DevApplication)
db.init_app(app)

migrate = Migrate(app, db)
api = Api(app)

[api.add_resource(*r) for r in routes]


# @app.route("/")
# def index():
#     # msg = Message('Hello', recipients=['homev54268@whecode.com'])
#     # mail.send(msg)
#     # return"send"
#     massage = "THis is thest massage"
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login("yreest@gmail.com", "testtest1!")
#     server.sendmail("yreest@gmail.com", "xotama9016@vinopub.com", massage)
#     return "send"

if __name__ == "__main__":
    app.run()
