import subprocess
import yaml


def juju_output():
    output = subprocess.check_output(["juju", "status"])
    data = yaml.load(output, Loader=yaml.Loader)
    return extract_machines(data), extract_services(data)


def extract_machines(data):
    machines = []
    for name, machine in data["machines"].items():
        machines.append((name, machine["agent-state"], machine["instance-state"]))
    return machines


def extract_services(data):
    services = []
    for service in data["services"].values():
        for name, unit in service["units"].items():
            services.append((name, unit["agent-state"]))
    return services
