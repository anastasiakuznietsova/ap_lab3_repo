from django import forms
from .models import Viewer,Movie,Showtime,Ticket, MovieSession

class ViewerForm(forms.ModelForm):
    class Meta:
        model = Viewer
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'birth_date'
        ]

class ShowtimeForm(forms.ModelForm):
    class Meta:
        model=Showtime
        fields = '__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields = [
            'showtime'
        ]
class MovieSessionForm(forms.ModelForm):
    class Meta:
        model=MovieSession
        fields = ['seat']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie

        fields = '__all__'