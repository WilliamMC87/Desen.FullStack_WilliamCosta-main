from rest_framework import viewsets, permissions
from .models import CustomUser, Token, Account, AccountToken, Transaction, Bet
from .serializers import (
    CustomUserSerializer, TokenSerializer, AccountSerializer,
    AccountTokenSerializer, TransactionSerializer, BetSerializer
)


# ---------- USER VIEWSET ----------
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Somente usuários logados podem acessar


# ---------- TOKEN VIEWSET ----------
class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------- ACCOUNT VIEWSET ----------
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------- ACCOUNT TOKEN VIEWSET ----------
class AccountTokenViewSet(viewsets.ModelViewSet):
    queryset = AccountToken.objects.all()
    serializer_class = AccountTokenSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------- TRANSACTION VIEWSET ----------
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------- BET VIEWSET ----------
class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = [permissions.IsAuthenticated]

