from flask import Blueprint, render_template, request

from main.utils import get_post_list, get_post

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    search_query = request.args.get('s', '')
    posts_list = get_post_list('posts.json')
    posts = get_post(posts_list, search_query)
    return render_template('post_list.html', posts=posts, search_query=search_query)
