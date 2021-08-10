from django.db import models


# Create your models here.
# Id card database table.
class IDCard(models.Model):
    image = models.ImageField(upload_to="images/id-card/")
    id_card_number = models.CharField(max_length=15, blank=True, null=True, default="")
    name = models.CharField(max_length=50, blank=True, null=True, default="")
    dob = models.CharField(max_length=10, blank=True, null=True, default="")
    nationality = models.CharField(max_length=50, blank=True, null=True, default="")
    sex = models.CharField(max_length=10, blank=True, null=True, default="")
    hometown = models.CharField(max_length=200, blank=True, null=True, default="")
    address = models.CharField(max_length=300, blank=True, null=True, default="")
    expires = models.CharField(max_length=20, blank=True, null=True, default="")


# Student card database table.
class Student_Card(models.Model):
    image = models.ImageField(upload_to="images/student-card/")
    student_card_number = models.CharField(max_length=15, blank=True, null=True, default="")
    name = models.CharField(max_length=255, blank=True, null=True, default="")
    major = models.CharField(max_length=255, blank=True, null=True, default="")
    falculty = models.CharField(max_length=255, blank=True, null=True, default="")
    course = models.CharField(max_length=255, blank=True, null=True, default="")

# Driving lisense card card database table.
class Driving_License_Card(models.Model):
    image = models.ImageField(upload_to="images/driving-license/")
    driving_license_number = models.CharField(max_length=15, blank=True, null=True, default="")
    name = models.CharField(max_length=255, blank=True, null=True, default="")
    dob = models.CharField(max_length=10, blank=True, null=True, default="")
    nationality = models.CharField(max_length=50, blank=True, null=True, default="")
    address = models.CharField(max_length=300, blank=True, null=True, default="")
    card_class = models.CharField(max_length=255, blank=True, null=True, default="")
    expires = models.CharField(max_length=20, blank=True, null=True, default="")
