from django.core.urlresolvers import reverse
from django.test import Client, SimpleTestCase

from stubs import raw

import yaml
import mock


class StatusViewTest(SimpleTestCase):
    @mock.patch("subprocess.check_output")
    def test_view(self, check_output):
        check_output.return_value = raw
        client = Client()
        response = client.get(reverse("status"))
        self.assertEqual(response.status_code, 200)
        output = yaml.load(raw, Loader=yaml.Loader)
        self.assertDictEqual(response.context['data'], output)
        check_output.assert_called_with(["juju", "status"])
