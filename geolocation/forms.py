# coding=utf-8
from django import forms
from .models.points import GeoPoint


class GeoPointForm(forms.ModelForm):
    """
        Form to handle geolocation for any entity
    """
    class Meta:
        model = GeoPoint
        fields = (
            'latitude', 'longitude'
        )
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput()
        }

    def save(self, commit=True):
        longitude = self.cleaned_data['longitude']
        latitude = self.cleaned_data['latitude']
        self.instance.coords = "POINT(%s %s)" % (longitude, latitude)
        return super(GeoPointForm, self).save(commit)





