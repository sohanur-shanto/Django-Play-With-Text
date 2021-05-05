from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render (request, 'index.html')


def analyzing(request):

    djtext = request.POST.get('text', 'default')
    
    removepunc = request.POST.get('removepunc', 'off')
    upperstr = request.POST.get('upperstr', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    numberremover = request.POST.get('numberremover', 'off')

    if removepunc == "on":
        analyzed = ""
        punc_list = string.punctuation
        for char in djtext:
            if char not in punc_list:
                analyzed = analyzed + char
    
            params = {
              'purpose' : 'Remove Punctuation',
              'analyzed_text' : analyzed,
            }

        djtext = analyzed


    if(upperstr == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {
              'purpose' : 'Convert Upper Case',
              'analyzed_text' : analyzed,
            }
        
        djtext = analyzed

    
    if(newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
            
        params = {
              'purpose' : 'New line remove',
              'analyzed_text' : analyzed,
            }
        djtext = analyzed


    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
            
        params = {
              'purpose' : 'Extra Space Remove',
              'analyzed_text' : analyzed,
            }
        
        djtext = analyzed

    if(numberremover == "on"):
        analyzed = ""
        number = '0123456789'
        
        for char in djtext:
            if char not in number:
                analyzed = analyzed + char
            
        params = {
              'purpose' : 'All Number Remove',
              'analyzed_text' : analyzed,
            }
        
        djtext = analyzed

    if(charcount == "on"):
        analyzed = ""

        words = djtext.split(" ")
        analyzed = len(words)
                
        params = {
              'purpose' : 'Count Total Word',
              'analyzed_text' : analyzed,
            }

    if (charcount != "on" and newlineremove != "on" and upperstr !="on" and removepunc != "on" and extraspaceremover != "on" and numberremover !="on"):
        return HttpResponse("<h1> Please fill out the checkbox and try again.</h1>")  
            
    
    return render (request, 'analyze.html', params) 



def contact(request):
    return render (request, 'contact.html')

def aboutme(request):
    return render (request, 'aboutme.html')







