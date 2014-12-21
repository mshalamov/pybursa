# -*- coding: utf-8 -*-
from django.db import models
from django import forms

from address.models import Address
from courses.models import Course


class Student(models.Model):
    PACKAGE_CHOICES = (
        ('s', 'Standard'),
        ('g', 'Gold'),
        ('p', 'Platinum')
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13, blank=True)
    courses = models.ManyToManyField(Course, blank=True)
    package = models.CharField(max_length=1, choices=PACKAGE_CHOICES,
                               default='s')
    dossier = models.OneToOneField('students.Dossier', blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Dossier(models.Model):
    COLORS = (
        ('RED', 'red'),
        ('WHITE', 'white'),
        ('BLACK', 'black'),
        ('GREEN', 'green'),
        ('YELLOW', 'yellow')
    )
    address = models.ForeignKey(Address)
    like_color = models.CharField(max_length=35, choices=COLORS)
    unlike_course = models.ManyToManyField(Course, blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.address, self.like_color)


class StudentForm(forms.Form):
    PACKAGE_CHOICES = (
        ('s', 'Standard'),
        ('g', 'Gold'),
        ('p', 'Platinum')
    )
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    package = forms.ChoiceField(choices=PACKAGE_CHOICES,
                                widget=forms.RadioSelect)


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        widgets = {'package': forms.RadioSelect}