from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove or customize help text for the username field
        self.fields['username'].help_text = 'Enter your username. Letters, numbers, and @/./+/-/_ only.'
        
        # Remove help text for password fields
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
