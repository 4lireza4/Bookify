from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, username):
        if not phone_number:
            raise ValueError('Phone number must be set')
        if not username:
            raise ValueError('Username must be set')

        user = self.model(phone_number=phone_number, username=username)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, username, password):
        user = self.create_user(phone_number, username, password)
        user.is_admin = True
        user.is_superuser= True
        user.is_active = True
        user.set_password(password or 'admin')
        user.save(using=self._db)
        return user

