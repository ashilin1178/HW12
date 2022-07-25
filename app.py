import logging

from flask import Flask

from loader.loader import loader_blueprint
from main.main import main_blueprint

# from functions import ...

# POST_PATH = "posts.json"
# UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

logging.basicConfig(filename='log.txt', level=logging.INFO, encoding='utf-8')

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)



if __name__ == ('__main__'):
    app.run()

