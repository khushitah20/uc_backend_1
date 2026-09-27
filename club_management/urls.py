"""
URL configuration for club_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clubs import views

from django.contrib import admin
from django.urls import path

from clubs import views as club_views
from events import views as event_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", club_views.home, name="home"),
    path("clubs/", club_views.club_list, name="club_list"),
    path("clubs/create/", club_views.create_club, name="create_club"),
    path("clubs/update/<int:club_id>/", club_views.update_club, name="update_club"),
    path("clubs/delete/<int:club_id>/", club_views.delete_club, name="delete_club"),
    path("clubs/<int:club_id>/members/", club_views.club_members, name="club_members"),
    path("members/", club_views.member_list, name="member_list"),
    path("members/create/", club_views.create_member, name="create_member"),
    path("members/update/<int:member_id>/", club_views.update_member, name="update_member"),
    path("members/delete/<int:member_id>/", club_views.delete_member, name="delete_member"),
    path("memberships/update/<int:member_id>/", club_views.update_member_memberships, name="update_member_memberships"),
    path("events/", event_views.event_list, name="event_list"),
    path("events/create/", event_views.create_event, name="create_event"),
    path("events/update/<int:event_id>/", event_views.update_event, name="update_event"),
    path("events/delete/<int:event_id>/", event_views.delete_event, name="delete_event"),
]
