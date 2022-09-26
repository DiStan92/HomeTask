from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.pk} - {self.question_text}'

    class Meta:
        verbose_name = 'Polls Question'
        verbose_name_plural = 'Polls questions'
        ordering = ['pk']


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=70)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.pk} - {self.choice_text}'

    class Meta:
        verbose_name = "Question's answer"
        verbose_name_plural = "Question's answers"
        ordering = ['question']

