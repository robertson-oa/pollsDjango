from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate


# Create your views here.


def signup(request):
    #template = 'registration/signup.html'
    #context = {'form':form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = UserCreationForm()
    
    return render(request,'registration/signup.html',{'form':form})




    ############ LOGIN VIEW ############
def signin(request):
    form = AuthenticationForm(request.POST)
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=username, password='password')        
    if user is not None:
        login(request, user)
        return redirect('polls:home')
    else:
        
        form = AuthenticationForm()
    template = 'registration/signin.html'
    context = {'form': form}
    return render(request,template,context)