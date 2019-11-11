from django.shortcuts import render
from .forms import NewsUserForm
from . models import NewsUsers
from django.core.mail import send_mail
# Create your views here.

def home(request):
  return render(request, "newsletter/home.html",{})

def newsletter_subscribe(request):
  if request.method == 'POST':
    form = NewsUserForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False) #we dont want to save just yet
    if NewsUsers.objects.filter(email=instance.email).exists():
      print( "your Email Already exists in our database")
    else:
      instance.save()
      print( "your Email has been submitted to our database")
      send_mail('Laughing blog tutorial series', 'welcome', 'emmanuelogundiran5@gmail.com',[instance.email], fail_silently=False)
  else:
    form = NewsUserForm()
  context = {'form':form}
  return render(request, "newsletter/subscribe.html", context)
