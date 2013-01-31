from django.shortcuts import render_to_response

from data import juju_output


def index(request):
    machines, services = juju_output()
    context = {
        "machines": machines,
        "services": services,
    }
    return render_to_response("status.html", context)
