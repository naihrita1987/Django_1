from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("<em>My Second App</em>")
    my_dict = {"insert_me": "This is my new views.."}
    return render(request,"help.html",context=my_dict)
    #I have made some changes 

