from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from accounts.models import Collaborator

class NipOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Umożliwia logowanie przy użyciu username lub nip.
        Parametr 'username' może zawierać zarówno username, jak i nip.
        """
        try:
            # Najpierw spróbuj znaleźć użytkownika po username.
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                # Jeśli nie znaleziono, spróbuj znaleźć Collaboratora z danym nipem
                collaborator = Collaborator.objects.get(nip=username)
                user = collaborator.user
            except Collaborator.DoesNotExist:
                return None

        if user.check_password(password):
            return user
        return None
