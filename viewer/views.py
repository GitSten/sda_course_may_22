from django.shortcuts import render

from django.http import HttpResponse

# We define a new view

#def hello_view(request,s):
 #   return HttpResponse(f"Hello {s} World!")


def hello_view(request):
    s = request.GET.get('s','')
    n = request.GET.get('n', 0)

    return  HttpResponse(f"Hello {s} World! {n} times")