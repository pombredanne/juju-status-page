import subprocess
import yaml


def juju_output():
    output = subprocess.check_output(["juju", "status"])
    return yaml.load(output, Loader=yaml.Loader)
