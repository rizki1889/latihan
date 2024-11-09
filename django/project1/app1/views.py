from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Topic, Webpage, AccesRecord
# Create your views here.

def index(request):
    webpage_list = AccesRecord.objects.order_by('date')
    date_dict = {'access_record': webpage_list}
    return render(request, 'app1/index.html', context=date_dict)