from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    ROLE_CHOICES = [
        ('admin', 'Admin/Researcher'),
        ('user', 'Regular User'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.profile.role = self.cleaned_data['role']
        user.profile.save()
        return user
