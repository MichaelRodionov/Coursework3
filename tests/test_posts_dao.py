import pytest
from app.posts.dao.posts_dao import PostsDAO


posts = PostsDAO("./data/posts.json")


class TestPostsDAO:

    def test_get_all(self):
        assert type(posts.get_all()) == list
        assert type(posts.get_all()[1]) == dict

    def test_get_by_user(self):
        assert type(posts.get_by_user("leo")) == list
        assert posts.get_by_user("leo")[0]["poster_name"] == "leo"

    def test_get_by_user_exceptions(self):
        with pytest.raises(ValueError):
            posts.get_by_user("123")

    def test_search_for_posts(self):
        result = posts.search_for_posts("Ага")
        assert type(posts.search_for_posts(" ")) == list
        assert "Ага" in result[0]["content"]

    def test_get_by_pk(self):
        assert type(posts.get_by_pk(1)) == dict
        assert posts.get_by_pk(1)["pk"] == 1

    def test_load_comments(self):
        assert type(posts.load_comments()) == list

    def test_get_comments_by_post_pk(self):
        with pytest.raises(ValueError):
            posts.get_comments_by_post_pk(10)
