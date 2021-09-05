from django import forms
from senior.models import Qna, Review

class QnaForm(forms.ModelForm):
    class Meta:
        model = Qna
        fields = ["title","picture","writer","desc"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["message"]