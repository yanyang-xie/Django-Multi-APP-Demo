from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app2/app2-base.html')