from django.shortcuts import render

def employee_add(request):
    employee=[
        {
            "id":1,
            "name":'subhash',
            "salary":40000,
            "days":4,
        },
        {
            "id":2,
            "name":'prabhas',
            "salary":40000,
            "days":3,
        },
        {
            "id":3,
            "name":'Ramesh',
            "salary":40000,
            "days":2,
        },
        {
            "id":4,
            "name":'Suresh',
            "salary":40000,
            "days":5,
        },
    ]
    return render(request,"employee.html",{'employee':employee})
    