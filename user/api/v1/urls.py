from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter, SimpleRouter
from user.api.v1.viewsets import UserRegistrationView, LoginTokenObtainView, ResetPasswordConfirmViewSet, \
    ChangePasswordViewSet, FacebookLogin, TwitterLogin, ToDoTaskView

router = SimpleRouter()
router.register('to_do_task', ToDoTaskView)
urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name="signup"),
    path('login/', LoginTokenObtainView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('reset_password_confirm/', ResetPasswordConfirmViewSet.as_view({"post": "create"}),
         name='reset_password_confirm'),  # use it when frontend need two password fields in payload
    path('change_password/', ChangePasswordViewSet.as_view({"post": "create"})),
    path('accounts/', include('allauth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('dj-rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),

]

urlpatterns += router.urls
