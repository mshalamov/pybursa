# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.db import models
from django import forms

from coaches.models import Coach
from students.models import Student


class Complaint(models.Model):
    theme = models.CharField(max_length=255)
    coach = models.ForeignKey(Coach)
    student = models.ForeignKey(Student)
    body = models.TextField(max_length=255)
    email = models.EmailField()


class ComplaintModelForm(forms.ModelForm):
    class Meta:
        model = Complaint


def complaint(request):
    title = "Complaint"
    if request.method == 'POST':
        form = ComplaintModelForm(request.POST)
        if form.is_valid():
            theme = form.cleaned_data['theme']
            body = form.cleaned_data['body']
            email = form.cleaned_data['email']
            send_mail(theme, body, email, ['max_newmail@gmail.com'])
            messages.success(request, "Message was send.")
            return redirect('complaint')
    else:
        form = ComplaintModelForm()
    return render(request,
                  'complaint.html',
                  {'form': form, 'title': title})