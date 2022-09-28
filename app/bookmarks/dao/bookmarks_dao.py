import json


class BookmarksDAO:

    def __init__(self, path):
        self.path = path

    def get_all_bookmarks(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            bookmarks = json.load(file)
        return bookmarks

    def save_bookmarks_to_json(self, bookmarks):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dumps(bookmarks, fp=file, ensure_ascii=False)

    def add_post_to_bookmarks(self, post):
        bookmarks = self.get_all_bookmarks()
        bookmarks.append(post)
        self.save_bookmarks_to_json(bookmarks)

    def delete_post_from_bookmarks(self, pk):
        bookmarks = self.get_all_bookmarks()
        for bookmark in bookmarks:
            if bookmark['pk'] == pk:
                bookmarks.remove(bookmark)
        self.save_bookmarks_to_json(bookmarks)
