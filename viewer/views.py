from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse
from .models import Movie
# We define a new view

#def hello_view(request,s):
 #   return HttpResponse(f"Hello {s} World!")


def hello_view(request):
    s = request.GET.get('s','')
    n = request.GET.get('n', 0)

    adjective = "sunny"

    return render(
        request,
        "hello.html",
        context={"adjectives": [s, n, adjective]}
    )



def index(request):
    return  render(request, template_name="base.html")



def test_view(request):
     return render(request,template_name="test.html")

def movies(request):
    return render(
        request,template_name='movies.html',
        context={'movies': Movie.objects.all()}
    )