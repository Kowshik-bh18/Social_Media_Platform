from .models import Posts,Comment
from django import forms

class Postcreateform(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title','image','caption')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body','posted_by']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Write a comment...',
                'class': 'w-full px-3 py-2 border rounded text-sm'
            })
        }


