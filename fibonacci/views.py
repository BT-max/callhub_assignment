from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def result(request):
    num = int(request.GET['num'])
    if num < 0:
        raise ValueError("Negative arguments not implemented")
    nth = find_fib(num)

    return render(request, 'result.html', {'result': nth[0]})


def find_fib(num):
    if num == 0:
        return 0, 1
    else:
        a, b = find_fib(num // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b

        if num % 2 == 0:
            return c, d
        else:
            return d, c + d
