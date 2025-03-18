from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='client')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def is_admin(self):
        return self.user_type == 'admin'

    def is_client(self):
        return self.user_type == 'client'
    
class Game(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    odds_team_a = models.FloatField()
    odds_team_b = models.FloatField()
    outcome = models.CharField(max_length=20, null=True, blank=True)  # Example: "Team A", "Team B", "draw"

    def __str__(self):
        return f"{self.name} - {self.date.strftime('%Y-%m-%d')}"
    
class Bet(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    choice = models.CharField(max_length=20)  # "Team A", "Team B"
    status = models.CharField(max_length=20, default="pending")  # "pending", "won", "lost"
    payout = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Bet by {self.user.username} on {self.game.name}"


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"
