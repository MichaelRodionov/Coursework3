from flask import Flask
from app.bookmarks.views import bookmarks_blueprint
from app.posts.views import posts_blueprint
from app.api.views import api_blueprint

# Create app
app = Flask(__name__)

# Register blueprints
app.register_blueprint(posts_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(api_blueprint)


# Add Error Handlers
@app.errorhandler(404)
def error404(error):
    return "статус-код 404"


@app.errorhandler(500)
def error500(error):
    return "статус-код 500"


if __name__ == '__main__':
    app.run(debug=True)
