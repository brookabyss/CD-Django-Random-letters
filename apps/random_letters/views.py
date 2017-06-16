from django.shortcuts import render,HttpResponse,redirect
import random

context={
    'words':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Second Sunday','Third Sunday','Fourth Sunday','Fifth Sunday'],
    'attempt': 1,
    "random_word": "Try it!"
}
def index(request):
    return render(request,'random_letters/index.html', context)
def generate(request):
    status="on"
    r=random.randint(1,len(context['words'])-1)
    context['random_word']=context['words'][r]
    print context['random_word']
    context['attempt']+=1
    return redirect('/')
def reset(request):
    context['attempt']=1
    context['random_word']= "Try it!"
    return redirect('/',context)
