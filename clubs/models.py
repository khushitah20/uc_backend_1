from django.db import models

# Create your models here.
class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=100)
    domain = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.club_name


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Membership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    joined_at = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=50,default="Member")

    class Meta:
        constraints = [models.UniqueConstraint(fields=["member", "club"],
                                               name="unique_member_club")]

    def __str__(self):
        return f"{self.member.name} - {self.club.club_name}"