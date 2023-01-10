from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	context = {
		'name': 'Fahd Agodzo',
		'age': 25,
		'nationality': 'Ghanaian'
	}
	return render(request,'index.html',context)