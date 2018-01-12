from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['To contact me, just send me an email:', 'rando.rommot@itcollege.ee']})