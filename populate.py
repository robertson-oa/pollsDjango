from polls.models import Question, Choice
import csv
import django
from django.utils import timezone
import os

#from django.conf import settings
#s.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")
#django.setup()

def read_data():
    data = []
    with open('questions.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)



def create_question_and_choices(question,choices):
    q = Question.objects.create(question_text=question,pub_date=timezone.now())
    q.save()
    for choice in choices:
        c = Choice.objects.create(question = q,choice_text = choice )
        c.save()


def populate_questions(data):
    print('Starting to run population script...')
    for datapoint in data:
        q =datapoint[0]
        c = datapoint[1:]
        create_question_and_choices(question = q,choices = c)
    print('Finished running script')



# run here
input_data = read_data()
input_data = input_data[1:]
populate_questions(data = input_data)
# if __name__ == '__main__':
#     #os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
#     populate_questions(data)

        