from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm

# Create your views here.

def event_list(request):
    search_query = request.GET.get("search", "")
    if search_query:
        events = Event.objects.filter(event_name__icontains=search_query)
    else:
        events = Event.objects.all()
    return render(request,"event_list.html",{"events": events,"search_query": search_query})

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("event_list")
    else:
        form = EventForm()
    return render(request,"event_form.html",{"form": form})

def update_event(request, event_id):
    event = get_object_or_404(Event,event_id=event_id)
    if request.method == "POST":
        form = EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect("event_list")
    else:
        form = EventForm(instance=event)
    return render(request,"event_form.html",{"form": form,"event": event})

def delete_event(request, event_id):
    event = get_object_or_404(Event,event_id=event_id)
    if request.method == "POST":
        event.delete()
        return redirect("event_list")
    return render(request,"event_confirm_delete.html",{"event": event})