from tortoise import models, fields


class Post(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=180)
    body = fields.TextField()
    picture = fields.CharField(max_length=256, null=True)
    author = fields.ForeignKeyField(
        'models.User', related_name='user', on_delete='CASCADE')

    def __str__(self):
        return self.title
