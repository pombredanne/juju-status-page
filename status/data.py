import subprocess
import yaml


def juju_output():
    output = subprocess.check_output(["juju", "status"])
    return yaml.load(output, Loader=yaml.Loader)


def extract_machines(data):
    machines = []
    for name, machine in data["machines"].items():
        machines.append((name, machine["agent-state"], machine["instance-state"]))
    return machines
