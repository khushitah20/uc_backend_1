from django.shortcuts import render, redirect, get_object_or_404
from .models import Club,Member,Membership
from .forms import ClubForm, MemberForm, MembershipForm

# Create your views here.
def home(request):
    return redirect("club_list")

def club_list(request):
    search_query = request.GET.get("search", "")
    if search_query:
        clubs = Club.objects.filter(club_name__icontains=search_query)
    else:
        clubs = Club.objects.all()
    return render(request,"club_list.html",{"clubs": clubs,"search_query": search_query})

def create_club(request):
    if request.method == "POST":
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("club_list")
    else:
        form = ClubForm()
    return render(request, "club_form.html", {"form": form})

def update_club(request, club_id):
    club = get_object_or_404(Club, club_id=club_id)
    if request.method == "POST":
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect("club_list")
    else:
        form = ClubForm(instance=club)
    return render(request,"club_form.html",{"form": form,"club": club})

def delete_club(request, club_id):
    club = get_object_or_404(Club, club_id=club_id)
    if request.method == "POST":
        club.delete()
        return redirect("club_list")
    return render(request,"club_confirm_delete.html",{"club": club})

def club_members(request, club_id):
    club = get_object_or_404(Club, club_id=club_id)
    memberships = Membership.objects.filter(club=club).select_related("member")
    return render(request,"club_members.html",{"club": club, "memberships": memberships})

def member_list(request):
    search_query = request.GET.get("search", "")
    if search_query:
        members = Member.objects.filter(name__icontains=search_query)
    else:
        members = Member.objects.all()
    memberships = Membership.objects.select_related("member", "club")
    return render(request,"member_list.html",{"members": members,"search_query": search_query,"memberships": memberships})

def create_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("member_list")
    else:
        form = MemberForm()
    return render(request,"member_form.html",{"form": form})

def update_member(request, member_id):
    member = get_object_or_404(Member,member_id=member_id)
    if request.method == "POST":
        form = MemberForm(
            request.POST,
            instance=member)
        if form.is_valid():
            form.save()
            return redirect("member_list")
    else:
        form = MemberForm(instance=member)
    return render(request,"member_form.html",{"form": form,"member": member})

def delete_member(request, member_id):
    member = get_object_or_404(Member,member_id=member_id)
    if request.method == "POST":
        member.delete()
        return redirect("member_list")
    return render(request,"member_confirm_delete.html",{"member": member})

def update_member_memberships(request, member_id):
    member = get_object_or_404(Member,member_id=member_id)
    memberships = Membership.objects.filter(member=member)
    if request.method == "POST":
        for membership in memberships:
            role = request.POST.get(
                f"role_{membership.membership_id}")
            membership.role = role
            membership.save()
        club_id = request.POST.get("new_club")
        if club_id:
            club = get_object_or_404(Club,club_id=club_id)
            Membership.objects.create(member=member,club=club,role="Member")
        return redirect("member_list")
    clubs = Club.objects.all()
    return render(request,"membership_update.html",{"member": member,"memberships": memberships,"clubs": clubs})