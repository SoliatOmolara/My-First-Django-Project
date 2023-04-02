from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello! Welcome to my first django view")