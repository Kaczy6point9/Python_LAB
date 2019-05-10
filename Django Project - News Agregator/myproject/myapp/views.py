import random
from django.shortcuts import render

# Create your views here.
def home(request):
    num = random.randint(1, 100)
    some_list = [
       random.randint(1, 100000),
       random.randint(1, 100000),
       random.randint(1, 100000),
    ]
    context = {
      'bool_item': True,
      'num': num,
      'list': some_list
    }
    return render(request, 'myapp/home.html', context)


def contact(request):
    return render(request, 'myapp/contact.html')

def about(request):
    tvseries = [
        {'title': 'Game of Thrones', 'seasons': 7, 'genre': 'fantasy', 'year': 2011, 'ongoing': True},
        {'title': 'Breaking Bad', 'seasons': 5, 'genre': 'drama', 'year': 2008, 'ongoing': False},
        {'title': 'Sons of Anarchy', 'seasons': 7, 'genre': 'crime drama', 'year': 2008, 'ongoing': False},
        {'title': 'The Big Bang Theory', 'seasons': 10, 'genre': 'comedy', 'year': 2007, 'ongoing': True},
        {'title': 'Silicon Valley', 'seasons': 4, 'genre': 'comedy', 'year': 2014, 'ongoing': True},
        {'title': 'The Walking Dead', 'seasons': 7, 'genre': 'horror', 'year': 2010, 'ongoing': True},
    ]
    context = {
      'lucky_num': random.randint(1, 10),
      'unlucky_num': random.randint(1, 10),
      'tvseries': tvseries
    }
    return render(request, 'myapp/about.html', context)