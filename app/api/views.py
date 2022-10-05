from flask import Blueprint, jsonify
from app.posts.dao.posts_dao import PostsDAO
from log.loger import logger

# Create API Blueprint
api_blueprint = Blueprint("api_blueprint", __name__, url_prefix="/api")
posts = PostsDAO("./data/posts.json")


# Create all posts view
@api_blueprint.route("/posts/")
def get_all_posts():
    all_posts = posts.get_all()
    logger.info(f"Запрос /api/posts")
    return jsonify(all_posts)


# Create post by pk view
@api_blueprint.route("/posts/<int:pk>")
def get_post_by_pk(pk):
    post = posts.get_by_pk(pk)
    logger.info(f"Запрос /api/posts/{pk}")
    return jsonify(post)
