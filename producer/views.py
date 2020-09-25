from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'index.html', context)
    else:
        return redirect('/login', permanent=False)