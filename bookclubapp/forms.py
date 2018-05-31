from django import forms
from .models import Profile,Books,Comment,Review,Groups

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name','Email']

class GroupForm(forms.ModelForm):
    class Meta:
        model=Groups
        fields=['Group_name']

    
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['title','Review']

class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=['title','author']