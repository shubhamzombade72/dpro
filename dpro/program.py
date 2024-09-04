from django.shortcuts import render

def seriesForm(request):
    if request.POST:
        tempArr = []
        temp = int(request.POST.get("number"))
        for i in range(1,temp+1):
            tempArr.append(i)
        data = {
            "series":tempArr
        }
        return render(request,"series.html",data)  
    else:
        data = {
            "series":[1,2,3,4,5]
        }
        return render(request,"series.html",data)  