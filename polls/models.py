from django.db import models
from django.utils.text import slugify

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_description = models.CharField(max_length = 1000, blank=True)
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField(max_length=255, unique=False, null = True)

    class Meta:
        verbose_name_plural = 'Questions'
        ordering = ['-pub_date']

    def __str__(self):
        return self.question_text

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question_text)
        super(Question, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return '/{}/{}/'.format('polls',self.slug)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return 'Choice for : {}'.format(self.question.question_text)

