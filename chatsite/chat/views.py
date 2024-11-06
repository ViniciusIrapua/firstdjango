from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def about(request):
    return render(request, 'chat/about.html')

def contacts(request):
    return render(request, 'chat/contacts.html')

def policies(request):
    return render(request, 'chat/policies.html')