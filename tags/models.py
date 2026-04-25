from django.db import models

class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    #What tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type (product, video, article)
    # ID
    product = models.ForeignKey(ContentType)
