from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    items = Project.objects.all()
    return render(request, 'home_app/home.html',
                  {'items':items})