from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    #return  HttpResponse('Hello')
    return render(request,'home.html')

# def eggs(request):
#     return HttpResponse('Eggs are great!')

def count(request):
    text=request.GET['fulltext']

    wordlist = text.split()

    num=len(wordlist)

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:

            worddictionary[word]+=1
        else:

            worddictionary[word]=1

    sorted_list=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    print("THE SORTED LIST IS:", sorted_list)

    return render(
                    request,
                    'count.html',
                    {'text_entered':text,'words_number':num,'wordlist':sorted_list}
                )
