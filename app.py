from flask import Flask
import logging
from loader.loader import loader_blueprint
from main.main import main_blueprint

app = Flask(__name__)
# подключаем логирование в файл и конфигурируем уровень логирования
logging.basicConfig(filename='log.txt', level=logging.INFO, encoding='utf-8')
# регистрируем blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

if __name__ == '__main__':
    app.run()
