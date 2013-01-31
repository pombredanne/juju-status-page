from django.core.urlresolvers import reverse
from django.test import Client, SimpleTestCase

from data import output


class StatusViewTest(SimpleTestCase):
    def test_view(self):
        client = Client()
        response = client.get(reverse("status"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['data'], output)
