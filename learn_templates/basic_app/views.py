from django.shortcuts import render

# Create your views here.
def index(request):
    dic = {'text':'Hello World!', 'num': 12345 }
    return render(request, 'basic_app/index.html', dic)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')

