from django.shortcuts import render

# Create your views here.
def homey(request):
	return render(request, "homey.html",{})


def about(request):
	return render(request, "about.html",{})