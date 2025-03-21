from django.contrib import admin
from .models import Game, Bet, UserProfile, Transaction

admin.site.register(Game)
admin.site.register(Bet)
admin.site.register(UserProfile)
admin.site.register(Transaction)
