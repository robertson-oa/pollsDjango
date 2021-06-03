from django.contrib import admin

# Register your models here.
from .models import Question, Choice


admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('question_text',)}
    #fields = ('pub_date','question_text')
    list_display = ('id','pub_date','question_text')

admin.site.register(Question, QuestionAdmin)