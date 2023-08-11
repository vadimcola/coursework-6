from django import forms

from mailing.models import Setting, Client, Message


class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ('client', 'message', 'mailing_time', 'frequency_mailing')

    def _init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_name', 'email', 'comment')

    def _init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject_message', 'message')

    def _init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
