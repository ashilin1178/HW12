from flask import json


def get_post_list(file_name: json):
    """
    функция выгружает данные из json в список словарей
    :param file_name:
    :return:
    """

    with open(file_name, 'r', encoding='utf-8') as file:
        post_list = json.load(file)

    return post_list


def get_post(post_list: list, search_word: str) -> list:
    """
    функция ищет пост по ключевым словам
    :param post_list:
    :param search_word:
    :return:
    """

    answer_list = []
    for post in post_list:
        if search_word.lower() in post['content'].lower():
            answer_list.append(post)

    return answer_list
