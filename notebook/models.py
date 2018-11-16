from django.db import models

class Note(models.Model):

    created_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default='')
    context = models.TextField(blank=True)


