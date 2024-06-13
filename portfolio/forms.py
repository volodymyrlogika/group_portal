from django import forms

from portfolio import models


class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'description', 'screenshot', 'links', 'files']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })
