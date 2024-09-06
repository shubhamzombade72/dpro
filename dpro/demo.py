from django.shortcuts import render

def addstudent(request):
    students = [
        {
            "roll": 101,
            "fname": 'Shubham',
            "lname": 'Zombade',
            "marks": 99,
        },
        {
            "roll": 102,
            "fname": 'Siddhant',
            "lname": 'Tagare',
            "marks": 9,
        },
        {
            "roll": 103,
            "fname": 'Bhai',
            "lname": 'Pawar',
            "marks": 34,
        },
        {
            "roll": 104,
            "fname": 'Sanmit',
            "lname": 'Pawar',
            "marks": 40,
        }
    ]
    
    
    
    
   
    return render(request, "demo.html", {'students': students})
