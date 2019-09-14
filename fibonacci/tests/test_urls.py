from django.test import SimpleTestCase
from django.urls import reverse, resolve
from fibonacci.views import index, result


class TestUrls(SimpleTestCase):
    def test_list_url_index(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_list_url_result(self):
        url = reverse('result')
        print(resolve(url))
        self.assertEquals(resolve(url).func, result)
