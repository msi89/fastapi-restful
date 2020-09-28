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
        'models.Tournament', related_name='events')
    participants = fields.ManyToManyField(
        'models.Team', related_name='events', through='event_team')
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
