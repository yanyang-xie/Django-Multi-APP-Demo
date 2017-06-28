from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    return render_to_response('app1/app1-base.html')
    #return render_to_response('app2/app2-base.html')