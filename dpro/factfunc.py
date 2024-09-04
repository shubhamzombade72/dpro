from django.shortcuts import render

def factFunc(request):
    if request.POST:
        fact=1
        temp = int(request.POST.get("number"))
        for i in range(1,temp+1):
            fact=fact*i
        data = {
            "fact":fact
        }
        return render(request,"factorial.html",data)  
    else:
        data = {
            "series":[1,2,3,4,5]
        }
        return render(request,"factorial.html",data)