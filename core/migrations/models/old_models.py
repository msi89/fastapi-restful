from tortoise import models, fields
from core.contrib.security import hash_password


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=60, default=None, null=True)
    username = fields.CharField(max_length=25, unique=True)
    email = fields.CharField(max_length=256, unique=True)
    password = fields.CharField(max_length=1000)
    is_admin = fields.BooleanField(default=False)
    is_staff = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)
    avatar = fields.CharField(max_length=256, default=None, null=True)

    def __str__(self):
        return f"{self.name} {self.email}"

    async def save(self, *args, **kwargs) -> None:
        self.password = hash_password(self.password)
        await super().save(*args, **kwargs)

    class PydanticMeta:
        exclude = ['password']

from tortoise import models, fields


class Post(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=180)
    body = fields.TextField()
    picture = fields.CharField(max_length=256, null=True)
    author = fields.ForeignKeyField(
        'diff_models.User', related_name='user', on_delete='CASCADE')

    def __str__(self):
        return self.title

from tortoise import models, fields


class Tournament(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    created = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    tournament = fields.ForeignKeyField(
        'diff_models.Tournament', related_name='events')
    participants = fields.ManyToManyField(
        'diff_models.Team', related_name='events', through='event_team')
    created = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name

    def title(self) -> str:
        return f"{self.id}-{self.name}".strip()

    class PydanticMeta:
        computed = ['title']
        # exclude = ['context']


class Team(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    created = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name

from tortoise import Model, fields

MAX_VERSION_LENGTH = 255


class Aerich(Model):
    version = fields.CharField(max_length=MAX_VERSION_LENGTH)
    app = fields.CharField(max_length=20)

    class Meta:
        ordering = ["-id"]

