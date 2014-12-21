# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django import forms


class Coach(models.Model):
    COACH_TYPES = (('C', 'Coach'), ('A', 'Assistant'))

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    coach_type = models.CharField(choices=COACH_TYPES,
                                  max_length=1)
    user = models.ForeignKey(User)
#    dossier = models.OneToOneField('students.Dossier', blank=True, null=True)

    def __unicode__(self):
        return "%s %s (%s)" % (self.first_name,
                               self.last_name,
                               self.coach_type)


class CoachForm(forms.Form):
    COACH_TYPES = (('C', 'Coach'), ('A', 'Assistant'))
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    coach_type = forms.ChoiceField(choices=COACH_TYPES,
                                   widget=forms.RadioSelect)


class CoachModelForm(forms.ModelForm):
    class Meta:
        model = Coach
        widgets = {'coach_type': forms.RadioSelect}
