from flask import Blueprint, render_template, request
from app.posts.dao.posts_dao import PostsDAO
from app.bookmarks.dao.bookmarks_dao import BookmarksDAO

# Create post blueprint
posts_blueprint = Blueprint('posts_blueprint', __name__,
                            template_folder='templates')
posts_dao = PostsDAO('./data/posts.json')
bookmarks_dao = BookmarksDAO('./data/bookmarks.json')


# Create main page views
@posts_blueprint.route('/')
def main_page():
    posts: list[dict] = posts_dao.get_all()
    bookmarks = bookmarks_dao.get_all_bookmarks()
    return render_template('index.html', title='Main page', posts=posts,
                           bookmarks=bookmarks)


# Create views with all users posts
@posts_blueprint.route('/users/<user_name>', methods=['GET'])
def get_posts_by_user(user_name):
    posts: list[dict] = posts_dao.get_by_user(user_name)
    return render_template('user-feed.html', title=user_name, posts=posts)


# Create views with search by word in posts
@posts_blueprint.route('/search/')
def get_posts_by_query():
    query = request.args.get('s')
    posts_with_query: list[dict] = posts_dao.search_for_posts(query)
    return render_template('search.html', title=query,
                           posts_with_query=posts_with_query)


# Create views with full post
@posts_blueprint.route('/posts/<int:post_id>', methods=['GET'])
def get_post_by_post_id(post_id):
    post = posts_dao.get_by_pk(post_id)
    comments = posts_dao.get_comments_by_post_pk(post_id)
    words = posts_dao.tags_create(post_id)
    return render_template('post.html', title=post_id, post=post,
                           comments=comments, word=words)


# Create views with search by tag
@posts_blueprint.route("/tag/<tag_name>")
def page_tag(tag_name):
    tag_name = "#" + tag_name
    posts = posts_dao.search_for_posts(tag_name)
    return render_template("tag.html", posts=posts, tag=tag_name)
