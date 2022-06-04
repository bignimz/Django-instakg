from django.shortcuts import render

def index(request):
    # Getting the instance of the current logged in user
    current_user = request.user
    return render(request, 'index.html')
