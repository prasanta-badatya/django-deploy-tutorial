from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def health(request):
    """Lightweight health check for load balancers / uptime monitors."""
    return JsonResponse({"status": "ok"})
