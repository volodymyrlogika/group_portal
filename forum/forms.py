from django import forms
from forum.models import Branch, Comment


class BranchCreate(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ["title", "description"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-2'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {'content': forms.Textarea(attrs={'class': 'form-control mb-2'})}