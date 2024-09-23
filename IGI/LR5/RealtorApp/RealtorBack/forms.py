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


class DiscountForm(forms.Form):
    discount = forms.CharField(max_length=15, required=False)


# class OfferImmForm(forms.Form):
#     options = forms.ChoiceField(
#         choices=[(j.id, j.text + ' Тип недвижимости:' + str(j.ntype) + ' ' + str(j.cost) + '$') for j in Immovables.objects.all()],
#         widget=forms.RadioSelect,
#         required=True
#     )
#     discount = forms.CharField(max_length=15, required=False)


