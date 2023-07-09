from django.db import models
from django.urls import reverse

# Create your models here.

class Task(models.Model):
    name = models.TextField(blank=True)
    human_description = models.TextField(blank=True)
    machine_description = models.TextField(blank=True)
    supercategory = models.TextField(blank=True)
    category = models.TextField(blank=True)
    subcategory = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}|{self.human_description}'

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('task-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name', 'human_description']


class TaskTag(models.Model):
    key = models.TextField()
    value = models.TextField()
    task = models.ForeignKey(Task, related_name='tasktag_task', on_delete=models.CASCADE, )

    def __str__(self):
        return ' '.join([self.key, self.value])

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('tasktag-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['key', 'value']
        unique_together = ('key', 'value', 'task')