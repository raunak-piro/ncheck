from django.shortcuts import render
from django.http import HttpResponse
def index (request):
	dic={'key':"Hello From Dictionary!"}
	return render(request,"myapp/index.html",context=dic)
# Create your views here.
