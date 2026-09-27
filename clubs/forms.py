from django import forms
from .models import Club,Member,Membership


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ["club_name", "domain", "description"]

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["name", "email"]


class MembershipForm(forms.ModelForm):
    role = forms.ChoiceField(
        choices=[
            ("Member", "Member"),
            ("Chairperson", "Chairperson"),
            ("Vice-Chairperson", "Vice-Chairperson"),],
        initial="Member")
    class Meta:
        model = Membership
        fields = ["member", "club", "role"]
