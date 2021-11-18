from django import forms

class LoginForm(forms.Form):
    userid = forms.CharField(max_length=100)
    
    def clean_userid(self):
        data = self.cleaned_data['userid']

        '''
        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        '''
        # Remember to always return the cleaned data.
        return data