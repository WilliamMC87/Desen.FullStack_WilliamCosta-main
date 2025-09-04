from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Gerenciador personalizado para o modelo CustomUser.
    Permite criar usuários e superusuários usando email como USERNAME_FIELD.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Cria e salva um usuário regular com email e senha.
        """
        if not email:
            raise ValueError("O email deve ser fornecido")
        email = self.normalize_email(email)
        
        # Certifica que os campos obrigatórios estejam presentes
        required_fields = ['name', 'cpf', 'rg', 'birth_date', 'address_country']
        for field in required_fields:
            if field not in extra_fields or extra_fields[field] is None:
                raise ValueError(f"O campo {field} deve ser fornecido")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Cria e salva um superusuário com email e senha.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser deve ter is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
