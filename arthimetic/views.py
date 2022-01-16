from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
a, b = 5, 6

posts = [

    {
        'author': 'Sreenath',
        'title': 'Blog post1',
        'content': 'First post content',
        'date_posted': ' August 27, 2018'
    },
    {
        'author': 'Sandhya',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'December 22, 2021'

    }
]

employees = {

    'data': {

        'type': 'users',
        'attributes': [
            {"first_name": "Foo1",
             "last_name": "Bar1",
             "email_address": "baz1@qux.com",
             "country": "Ireland"
             },
            {"first_name": "Foo2",
             "last_name": "Bar2",
             "email_address": "baz2@qux.com",
             "country": "UK"
             },
            {"first_name": "Foo3",
             "last_name": "Bar3",
             "email_address": "baz3@qux.com",
             "country": "USA"
             }

        ]
    }

}

print('Emp First name is '+employees['data']['attributes'][2]['first_name'])


def add(request):
    c = a + b
    return HttpResponse('a plus b is ' + str(c))


def substract(request):
    d = b - a
    return HttpResponse('b minus a is ' + str(d))


def hometmpl(request):
    context = {
        'keys': posts
    }
    return render(request, 'arthimetic/hometmpl.html', context)


def abttmpl(request):
    return render(request, 'arthimetic/abouttmpl.html', {'title': 'Blog'})


def employee(request):
    return render(request, 'arthimetic/employee.html', employees)


def getexample(request):
    return render(request, "arthimetic/getexample.html")


def add1(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1 + num2
    return render(request, "arthimetic/add1.html", {'sum': result})
