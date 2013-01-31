from django.shortcuts import render_to_response

from data import juju_output


def index(request):
    context = {"data": juju_output()}
    return render_to_response("status.html", context)
