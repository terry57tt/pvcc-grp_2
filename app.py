from flask import Flask
from jardiquest import controller, model


# config the app to make app.py the start point but the actual program is one directory lower
flask_serv = Flask(__name__,
                   static_folder="jardiquest/static",
                   template_folder='jardiquest/view')

# allow the link to the controller part
flask_serv.register_blueprint(controller.app)


# all operation of closing ressources like database
@flask_serv.teardown_appcontext
def close_ressource(exception):
    model.close_connection(exception)
