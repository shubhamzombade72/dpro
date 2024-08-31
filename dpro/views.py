from django.shortcuts import render

def dashboard(request):
    return render(request,"index.html")

def calculator(request):
    return render(request,"cal.html")

def card(request):
    return render(request,"card.html")

def time_table(request):
    return render(request,"time_table.html")

def armstrong(request):
    return render(request,"armstrong.html")