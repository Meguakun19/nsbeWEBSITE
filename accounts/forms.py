from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username','email_address', 'phone_number','date_joined_nsbe','dues_paid','eboard_member','classification','grade_point_average')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email_address', 'phone_number','date_joined_nsbe','dues_paid','eboard_member','classification','grade_point_average')