from blog.models import Post
from core.contrib.generics import BaseView


class PostView(BaseView):
    model = Post

    def hello(self):
        return "hello world"
