from django.contrib.auth.forms import UserCreationForm
from .models import User


# Форма для юзера
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'money', 'username', 'image')
# Сдесь мы дописываем свои филды, и те поля которые мы хотим вводить при регистрации.
