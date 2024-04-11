from django.db import models

class Task(models.Model):
    class Taskchoice(models.TextChoices):
        NEW = 'new', 'New'
        INPROGRESS = 'in_progress', 'In Progrews'
        DONE = 'done', 'Done'
    title = models.CharField(max_length=100)
    discription = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=100, choices=Taskchoice.choices, default=Taskchoice.NEW)

    def __str__(self) -> str:
        return self.title
