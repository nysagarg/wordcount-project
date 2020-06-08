from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, "home.html")

def count(request):
    fullText=request.GET['fullText']
    wordlist = fullText.split()

    wordict={}
    for word in wordlist:
        if word in  wordict:
            wordict[word]+=1
        else:
            wordict[word]=1
    sortedwords = sorted(wordict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, "count.html", {'fullText':fullText, 'count':len(wordlist), 'sortedwords': sortedwords})

def about(request):
    return render(request, "about.html")
