from django.shortcuts import render
from django.http import HttpResponse
import time
from fibonacci.models import FibonacciSeries
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def index(request):
    """
    A function that renders the index.html page
    """

    return render(request, 'index.html')


def get_fib(request):
    """
    Function which gets the nth fibonacci number

    - startTime: Stores the time when the function is invoked
    - endTime: Stores the time when the function completes computation
    - timeTaken: Stores the total time taken to process the request in string format
    - num: Receives the nth number from the user
    - answer: searches if number is present in the database
    - fibonacciNumber: stores the result
    -solution: Dictionary object that returns the result
    """

    startTime = time.time()
    num = int(request.GET.get("num"))
    # search database for existing entry
    try:
        answer = FibonacciSeries.objects.get(index=num)
    except FibonacciSeries.DoesNotExist:
        answer = None

    if answer:
        fibonacciNumber = answer.fibonacciNumber
    else:
        # if entry doesnt exist then calculate fibonacciNumber
        fibonacciNumber = calculate_fib(num)
        # create new entry for future use
        entry = FibonacciSeries.objects.create(index=num, fibonacciNumber=str(fibonacciNumber))
        entry.save()
    endTime = time.time() - startTime
    timeTaken = str(endTime)
    solution = {"result": fibonacciNumber, "timeTaken": timeTaken}
    return render(request, 'result.html', solution)


def calculate_fib(num):
    """
    Function that calculates nth fibonacci number using fast doubling fibonacci algorithm

    """
    if num == 0:
        return 0
    if num <= 2:
        return 1
    k = int(num / 2)
    a = calculate_fib(k + 1)
    b = calculate_fib(k)
    if num % 2 == 1:
        return a * a + b * b
    return b * (2 * a - b)
