__author__ = 'bernardino'
import uuid
from database import Database

class Post():
    def __init__(self, title, content, author, date_created, blog_id ='This blog', post_id=None):
        self.blog_id = blog_id
        self.post_id = uuid.uuid4().hex if post_id is None else post_id
        self.title = title
        self.date_created = date
        self.content = content
        self.author = author

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

    @staticmethod
    def from_mongo(id):
        data = Database.find_one(collection='posts', query={'id':id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id':id})]
