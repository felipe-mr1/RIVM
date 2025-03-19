from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, BetViewSet, TransactionViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'bets', BetViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),  # API routes for games, bets, transactions
    path('register/', RegisterView.as_view(), name="register"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
