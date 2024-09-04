from django.shortcuts import render

def addition(request):
    if request.method == "POST":
        temp = int(request.POST.get("number", 0))
        add = sum(range(1, temp + 1))
        
        data = {
            "add": add
        }
        return render(request, "addtion.html", data)
    
    return render(request, "addtion.html")
