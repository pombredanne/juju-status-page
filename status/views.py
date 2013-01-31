from django.shortcuts import render_to_response

from data import extract_machines, juju_output


def index(request):
    output = juju_output()
    context = {
        "data": output,
        "machines": extract_machines(output),
    }
    return render_to_response("status.html", context)
