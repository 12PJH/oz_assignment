from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_feed(request):
    return HttpResponse("show feed")

def all_feed(request):
    return HttpResponse("all feed")

def one_feed(request, feed_id, feed_content):
    return HttpResponse(f"feed_id = {feed_id} feed_content = {feed_content}")
