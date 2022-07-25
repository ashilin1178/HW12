import logging

from flask import Blueprint, render_template, request

from loader.utils import load_picture, load_post, get_cheking_extention

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post():
    """
    загружает новый пост
    :return:
    """

    picture = request.files.get('picture')
    content = request.form.get('content')


    if not picture or not content:
        return "нет картинки или текста"


    try:

        if get_cheking_extention(picture):
            pic = load_picture(picture)

            post_ = load_post('posts.json', pic, content)

            return render_template('post_uploaded.html', post=post_)

        else:
            logging.info('Недопустимое расширение файла картинки')
            return "Недопустимое расширение файла картинки"

    except:
        return "Ошибка загрузки поста"



