from django.db import models


# Create your models here.
class FibonacciSeries(models.Model):

    index = models.IntegerField()  # stores the index(nth) for the fibonacci number
    fibonacciNumber = models.TextField()  # stores result of the fibonacci number

    class Meta:
        db_table = "fibonacci_number"

    def __str__(self):
        return self.index
