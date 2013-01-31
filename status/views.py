from django.shortcuts import render_to_response

from data import output


def index(request):
    context = {"data": output}
    return render_to_response("status.html", context)
