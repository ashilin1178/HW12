import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from main.utils import get_post_list, get_post

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    """
    главная страница
    :return:
    """
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    """
    страница поиска
    :return:
    """
    try:
        logging.info("Поиск работает")
        #принимаем из запроса агрумент поиска "s" поиска
        search_query = request.args.get('s', '')
        #выгружаем файл со списком всех постов
        posts_list = get_post_list('posts.json')
        #находим посты по критерию поиска
        posts = get_post(posts_list, search_query)

        return render_template('post_list.html', posts=posts, search_query=search_query)
    #ошибка наличия файла со списком постов
    except FileNotFoundError:
        logging.error("файл 'posts.json' не найден")
        return "файл 'posts.json' не найден"
    #ошибка чтения файла JSON
    except JSONDecodeError:
        logging.error("файл 'posts.json' поврежден")
        return "файл 'posts.json' поврежден"
