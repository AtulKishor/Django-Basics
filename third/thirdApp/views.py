from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello</h1>")
    return render(request, 'thirdapp/index.html', {'insert_me': "Content inserted here!"})
