import json


class BookmarksDAO:

    def __init__(self, path):
        self.path = path

    def get_all_bookmarks(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            bookmarks = json.load(file)
        return bookmarks

    def add_post_to_bookmarks(self, post):
        bookmarks = self.get_all_bookmarks()
        with open(self.path, 'w', encoding='utf-8') as file:
            bookmarks.append(post)
            json.dump(bookmarks, fp=file, ensure_ascii=False, indent=4)

    def delete_post_from_bookmarks(self, pk):
        bookmarks: list[dict] = self.get_all_bookmarks()
        for bookmark in bookmarks:
            if bookmark['pk'] == pk:
                with open(self.path, 'w', encoding='utf-8') as file:
                    bookmarks.remove(bookmark)
                    json.dump(bookmarks, fp=file, ensure_ascii=False, indent=4)
