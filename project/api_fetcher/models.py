from django.db import models

# Create your models here.


class Item(models.Model):

    """
    a class represents the Items table
    """

    public_id = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.TextField()
    image_url = models.CharField(max_length=250)

    def __str__(self):
        return "{}".format(self.title)