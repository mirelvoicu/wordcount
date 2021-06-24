from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return  HttpResponse('Hello')
    return render(request,'home.html')

# def eggs(request):
#     return HttpResponse('Eggs are great!')

def count(request):
    text=request.GET['fulltext']

    num=len(text.split(" "))
    return render(
                    request,
                    'count.html',
                    {'text_entered':text,'words_number':num}
                )
