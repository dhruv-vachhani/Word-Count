from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def countpage(request):
    string = request.GET['fulltextarea']
    wordlist = string.split()
    lenght = len(wordlist)

    wordDic = {}

    for word in wordlist:
        if word in wordDic:
            wordDic[word] += 1
        else:
            wordDic[word] = 1

    newwordDic = sorted(wordDic.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html', { 'ans':lenght , 'word_dis':newwordDic} )