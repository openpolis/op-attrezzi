from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from .provider import AccessoProvider

urlpatterns = default_urlpatterns(AccessoProvider)
