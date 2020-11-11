from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    task_id = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        super(Location, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=100)
    place = models.ForeignKey(Location, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # We save this first to ensure self.id is having valid value.
        super(Todo, self).save(*args, **kwargs)

        # This is how we can save Todo's id to Location model's task_id
        self.place.task_id = self.id
        self.place.save()

    def __str__(self):
        return self.title