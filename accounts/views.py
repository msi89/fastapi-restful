from accounts.models import User
from core.contrib.generics import BaseView


class AuthView(BaseView):
    model = User
