from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

# CustomUser model so that it can be integrated into new CustomUserCreationForm and CustomUserChangeForm classes.


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("name",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
