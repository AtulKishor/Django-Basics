from django.shortcuts import render
from my_first_app.models import Topic, WebPage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    return render(request, 'my_first_app/index.html', {'access_records': webpages_list})

