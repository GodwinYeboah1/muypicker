from django.shortcuts import render
from django.http import HttpResponse
from django.views import TemplateView, View
import random
# Create your views here.

# function based view

class AboutView(View):
    template_name = 'about.html'
    content = {'key': 'This is from the About view page'}

    def get(self, request, *args, **kwargs):
        return render(request, "about.html")





def home(request):
    random_number = random.randint(0,600)
    response = {
        "title": "godwin website page 1",
        'shit_load': "i am the best there is",
        'lucky_number': random_number
    }
    return render(request, "base.html",response)

def home2(request):
    random_number = random.randint(0,600)
    response = {
        "title": "godwin website page 2",
        'shit_load': "i am the best there is",
        'lucky_number': random_number
    }
    return render(request, "home2.html", response)

def home3(request):
    random_number = random.randint(0,600)
    response = {
        "title": "godwin website page 3",
        'shit_load': "i am the best there is",
        'lucky_number': random_number
    }
    return render(request, "home3.html", response)