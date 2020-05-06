# Django_Formset_Factory

[referred blog](https://narito.ninja/blog/detail/94/)

![formset-factory](formset-factory.gif)

> ## models.py
``` python
from django.db import models

GENDER_CHOICES = [
    ('1', 'female'),
    ('2', 'male'),
]

class Profile(models.Model):
    name = models.CharField('name', max_length=100)
    gender = models.CharField('sex', max_length=1, choices=GENDER_CHOICES)
    yearly_income = models.IntegerField('salary(K)')
    height = models.FloatField('height')
    weight = models.FloatField('weight')
```

> ## admin.py
``` python
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
```

> ## views.py
``` python
from django.db.models import Q
from django.shortcuts import render
from .forms import ProfileSearchFormSet
from .models import Profile


def index(request):
    profile_list = Profile.objects.all()
    formset = ProfileSearchFormSet(request.POST or None)
    if request.method == 'POST':
        # Because all input area are set as required=False, is_valid() should become True
        formset.is_valid()

        # This is a list to store Q Object
        queries = []

        # Creating search condition as Q Object based on input in the form
        for form in formset:
            # {gender: 1, height__gte: 170} → Q(gender=1, height__gte=170)
            q_kwargs = {}
            gender = form.cleaned_data.get('gender')
            if gender:
                q_kwargs['gender'] = gender

            yearly_income = form.cleaned_data.get('yearly_income')
            if yearly_income:
                q_kwargs['yearly_income__gte'] = yearly_income
            # gte means grater than or equal

            height = form.cleaned_data.get('height')
            if height:
                q_kwargs['height__gte'] = height

            weight = form.cleaned_data.get('weight')
            if weight:
                q_kwargs['weight__lte'] = weight
            # lte means lower than or equal
            # If form is empty, q_kwargs remains empty
            if q_kwargs:
                q = Q(**q_kwargs)
                queries.append(q)

        if queries:
            # making filter(Q(...) | Q(...) | Q(...)) dynamically 
            base_query = queries.pop()
            for query in queries:
                base_query |= query
            profile_list = profile_list.filter(base_query)

    context = {
        'profile_list': profile_list,
        'formset': formset,
    }
    return render(request, 'app/profile_list.html', context)
```

> ## urls.py
``` python
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),  
]
```

> ## profile_list.html
``` python
<form action="" method="POST">
    {{ formset.management_form }}
    {% for form in formset %}
        {{ form }}<br>
    {% endfor %}
    {% csrf_token %}
    <button type="submit">Search</button>
</form>
<hr>

{% for profile in profile_list %}
    Name: {{ profile.name }}
    Salary (K): {{ profile.yearly_income }}
    Height (cm): {{ profile.height }}
    Weight (kg): {{ profile.weight }}
    <hr>
{% endfor %}
```
