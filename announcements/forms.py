from django import forms

from announcements import models


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = models.Announcement
        fields = ['title', 'content', 'image',]

    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })