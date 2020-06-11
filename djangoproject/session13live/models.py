from django.db import models

# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=100)
    number_of_votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question.text} - {self.text}: {self.number_of_votes}"
