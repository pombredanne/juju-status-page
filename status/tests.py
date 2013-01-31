from django.core.urlresolvers import reverse
from django.test import Client, SimpleTestCase

from data import raw

import yaml


class StatusViewTest(SimpleTestCase):
    def test_view(self):
        client = Client()
        response = client.get(reverse("status"))
        self.assertEqual(response.status_code, 200)
        output = yaml.load(raw, Loader=yaml.Loader)
        self.assertDictEqual(response.context['data'], output)
