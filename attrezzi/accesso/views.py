import requests
from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
                                                          OAuth2LoginView,
                                                          OAuth2CallbackView)

from .provider import AccessoProvider
from ..settings import attrezzi_settings


class AccessoAdapter(OAuth2Adapter):
    provider_id = AccessoProvider.id
    access_token_url = attrezzi_settings.ACCESSO_ACCESS_TOKEN_URL
    authorize_url = attrezzi_settings.ACCESSO_AUTHORIZE_URL
    profile_url = attrezzi_settings.ACCESSO_PROFILE_URL
    supports_state = False

    def complete_login(self, request, app, token, **kwargs):
        extra_data = self.get_user_info(token)
        return self.get_provider().sociallogin_from_response(request, extra_data)

    def get_user_info(self, token):
        url = self.profile_url + '?format=json'
        resp = requests.get(url, headers={'Authorization': 'Bearer %s' % token.token})
        return resp.json()

oauth2_login = OAuth2LoginView.adapter_view(AccessoAdapter)
oauth2_callback = OAuth2CallbackView.adapter_view(AccessoAdapter)
