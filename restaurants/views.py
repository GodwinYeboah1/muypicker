from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

# function based view
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