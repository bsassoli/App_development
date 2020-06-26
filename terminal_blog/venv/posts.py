__author__ = 'bernardino'


class Post():
    def __init__(self, post_id, title, content, author, date_created, blog_id ='This blog'):
        self.blog_id = blog_id
        self.post_id = post_id
        self.title = title
        self.content = content
        self.author = author
        self.date_created = date_created

    def save_to_mongo(self):
        pass

    def json(self):
        Database.insert(collection='posts', data=self.json())

        return{
            'post_id': self.post_id,
            'blog_id': self.post_id,
            'author': self.author,
            'title': self.author,
            'content': self.author,
            'date_created': self.date_created
        }
