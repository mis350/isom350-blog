from django import forms

from .models import Post, Comment

from bootstrap_datepicker_plus import DateTimePickerInput

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ["title", "body", "status", "publish_on"]
    widgets = {
      "publish_on": DateTimePickerInput(),
    }

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ["comment", "author", "email", "post"]
    widgets = {
      "post": forms.HiddenInput(),
    } 
    