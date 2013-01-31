from django.shortcuts import render_to_response

from data import extract_machines, extract_services, juju_output


def index(request):
    output = juju_output()
    context = {
        "machines": extract_machines(output),
        "services": extract_services(output),
    }
    return render_to_response("status.html", context)
