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

    def test_search_for_posts(self):
        all_posts = posts.get_all()
        assert 'еда' in all_posts[0]['content']

    def test_get_by_pk(self):
        assert type(posts.get_by_pk(1)) == dict
        assert posts.get_by_pk(1)["pk"] == 1

    def test_get_by_pk_exeptions(self):
        with pytest.raises(KeyError):
            posts.get_by_pk(1)[""]

    def test_load_comments(self):
        assert type(posts.load_comments()) == list


    def test_tags_create(self,):
        pass
