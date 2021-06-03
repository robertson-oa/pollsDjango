from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .models import Question, Choice

# forms
from .forms import ChoiceForm, QuestionForm, CreateQuestionForm #,UserForm

# Create your views here.

def pollhome(request):
    questions_list = Question.objects.all()[0:4]
    template = 'polls/home.html'
    context = {'questions':questions_list}


    return render(request,template,context)
    #return HttpResponse(output)

def results(request,slug):
    question = get_object_or_404(Question, slug=slug)
    return render(request, 'polls/results.html', {'question': question})


def detail(request, slug):
    """
    Returns a path to the detail view for a single question
    """
    try:
        question = Question.objects.get(slug=slug)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, slug):
    question = get_object_or_404(Question, slug=slug)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:result', args=(question.slug,)))



def choice_form(request):
    
    form = ChoiceForm()
    template = 'polls/choiceview.html'
    context = {
        'form':form
    }
    return render(request,template,context = context)

def edit_question_form(request,id):

    question = Question.objects.get(pk=id)
    form = QuestionForm(instance = question)
    template = 'polls/choiceview.html'
    context = {
        "form":form,

    }
    return render(request,template,context = context)

def create_new_question(request):    
    
    if request.method == 'POST':
        q_text = request.POST.cleaned_data['question_text']
        new_question = Question(question_text = q_text)
        form = CreateQuestionForm(request.POST,instance=new_question) 
        if form.is_valid():
            form.save()
            HttpResponseRedirect('/polls/home.html')
    
    else:
        form = CreateQuestionForm()
    

    template = 'polls/newquestion.html'
    context = {
        "form":form
    }

    return render(request = request, template_name=template, context = context)


def signup(request):
    #template = 'registration/signup.html'
    #context = {'form':form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('polls:home')
    else:
        form = UserCreationForm()
    
    return render(request,'polls/signup.html',{'form':form})




    