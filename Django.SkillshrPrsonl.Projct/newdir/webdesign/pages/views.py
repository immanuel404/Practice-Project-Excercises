from django.shortcuts import render

# C# Create your views here.
def home(request):
	list= [2,4,6,8,10]
	diction={'book':'Musk', 'publisher':'oxford'}

	context= {'page_list':list, "dictionary":diction}

	return render(request, "home.html",context)

def about(request):
	return render(request, "about.html",{})


