from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="server_owner",
    )
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name="server_category"
    )
    description = models.CharField(max_length=250, null=True, blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="channel_owner",
    )
    topic = models.CharField(max_length=100)
    server = models.ForeignKey(
        Server, on_delete=models.DO_NOTHING, related_name="chanel_server"
    )

    def save(self, *args, **kwargs):
        self.name = self.name.lower()

        super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
