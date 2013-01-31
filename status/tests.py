from django.core.urlresolvers import reverse
from django.test import Client, SimpleTestCase

from stubs import raw
from data import extract_machines

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
        machines = extract_machines(output)
        self.assertDictEqual(response.context['data'], output)
        self.assertListEqual(response.context['machines'], machines)
        check_output.assert_called_with(["juju", "status"])


class ExtractData(SimpleTestCase):
    def test_machines(self):
        output = yaml.load(raw, Loader=yaml.Loader)
        data = extract_machines(output)
        expected = [
            (0, "running", "running"),
            (128, "running", "running"),
            (129, "running", "running"),
            (142, "running", "running"),
            (113, "running", "running"),
            (114, "running", "running"),
            (147, "running", "running"),
            (127, "running", "running"),
        ]
        self.assertListEqual(data, expected)
