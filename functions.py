import json


def load_posts():
    """Загрузит данные из файла"""
    with open("posts.json", mode='r', encoding='utf-8') as posts:
        return json.load(posts)


def get_posts_by_word(word: str):
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def add_post(post):
    posts = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post
