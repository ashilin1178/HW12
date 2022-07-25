from flask import Blueprint, render_template, request

from loader.utils import load_picture, load_post

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

    else:
        pic = load_picture(picture)

        post = load_post('posts.json', pic, content)

    return render_template('post_uploaded.html', post=post)








