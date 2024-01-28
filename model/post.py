from model.user import User


class Post:

    def __init__(self, post_id: int, title: str, body: str, author: User):
        self.post_id = post_id
        self.title = title
        self.body = body
        self.author = author
