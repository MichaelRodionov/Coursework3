import json


class PostsDAO:

    def __init__(self, path):
        self.path = path

    def get_all(self) -> list[dict]:
        """
        Load data from json file
        :return: list of all posts
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_by_user(self, user_name) -> list[dict]:
        """
        :return: list of posts with 'user_name'
        """
        posts = self.get_all()
        user_posts = [post for post in posts if user_name == post['poster_name']]
        if not user_posts:
            raise ValueError("Нет такого пользователя")
        return user_posts

    def search_for_posts(self, query) -> list[dict]:
        """
        :return: list of posts, sorted by query
        """
        posts = self.get_all()
        posts_by_query = [post for post in posts if query.lower() in post['content'].lower()]
        return posts_by_query

    def get_by_pk(self, post_id) -> dict:
        """
        :return: post by pk
        """
        posts = self.get_all()
        for post in posts:
            if post['pk'] == post_id:
                return post

    def load_comments(self):
        with open("./data/comments.json", encoding="utf-8") as file:
            return json.load(file)

    def get_comments_by_post_pk(self, post_pk):
        comments = self.load_comments()
        post_comments = [comment for comment in comments if comment["post_id"] == post_pk]
        if not post_comments:
            raise ValueError("У поста нет комментариев")
        return post_comments

    def tags_create(self, pk):
        post = self.get_by_pk(pk)
        text = post["content"]
        words = text.split()
        for index, word in enumerate(words):
            if word.startswith("#"):
                if word[1:].isalpha():
                    word = word[1:]
                    word = word.replace(word, f"<a href='/tag/{word}'>#{word}</a>")
                    words[index] = word
                else:
                    sym = word[-1]
                    word = word[1:-1]
                    word = word.replace(word, f"<a href='/tag/{word}'>#{word}</a>")
                    words[index] = word + sym
        return " ".join(words)
