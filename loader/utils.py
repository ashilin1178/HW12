from flask import json


def get_post_list(file_name: json):
    """
    функция выгружает данные из json в список словарей
    :param:
    :return:
    """

    with open(file_name, 'r', encoding='utf-8') as file:
        post_list = json.load(file)

    return post_list


def load_picture(picture):
    """
    функция сохраняет картинку в папку и возвращает путь до сохраненного файла
    :param picture:
    :return:
    """
    filename = picture.filename
    path_ = f'./uploads/images/{filename}'
    picture.save(path_)
    return path_


def load_post(file_name, pic_path, content) -> dict:
    """
    функция записывает ссылку на картинку и описание поста в файл json и возвращает словарь с этой записью
    :param file_name:
    :param pic_path:
    :param content:
    :return:
    """

    post_list = get_post_list(file_name)

    post_list.append({'pic': pic_path, 'content': content})

    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(post_list, file, ensure_ascii=False)

    return {'pic': pic_path, 'content': content}


def get_cheking_extention(picture) -> bool:
    """
    функция проверки разрешенного расширения файла картинки
    :return:
    """
    allowed_extensions = {'png', 'jpg', 'jpeg'}

    return picture.filename.split('.')[-1].lower() in allowed_extensions
