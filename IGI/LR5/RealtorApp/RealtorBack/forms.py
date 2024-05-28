from django import forms
from django.contrib.auth.models import User
from .models import Comment, Rent, Immovables


class CommentForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    mark = forms.IntegerField(min_value=0, max_value=10)


    def save(self, user, commit=True):
        if commit:
            Comment.objects.create(
                user=user,
                text=self.cleaned_data['text'],
                mark=self.cleaned_data['mark']
            )
        return user


class OfferRentForm(forms.Form):
    options = forms.MultipleChoiceField(
        choices=[(i, j.text + ' ' + str(j.cost) + '$') for i, j in enumerate(Rent.objects.all(), start=1)],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )


class OfferImmForm(forms.Form):
    options = forms.MultipleChoiceField(
        choices=[(i, j.text + ' ' + str(j.cost) + '$') for i, j in enumerate(Immovables.objects.all(), start=1)],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )