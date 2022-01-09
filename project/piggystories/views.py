from django.shortcuts import render

# relative import of forms
from .models import StoryModel
from .forms import StoryForm

# Create your views here.

def index(request):
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = StoryModel.objects.all().order_by("-date")

    return render(request, "piggystories/index.html", context)

def login(request):
    return render(request, "piggystories/login.html")

def register(request):
    return render(request, "piggystories/register.html")

def dashboard(request):
    return render(request, "piggystories/dashboard.html")

def profile(request):
    return render(request, "piggystories/profile.html")

def create_story(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = StoryForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "piggystories/create_story.html", context)

