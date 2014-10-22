from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class AccessoAccount(ProviderAccount):

    def get_profile_url(self):
        return self.account.extra_data.get('profile_url', '')

    def get_avatar_url(self):
        return self.account.extra_data.get('photo_image', '')

    def to_str(self):
        dflt = super(AccessoAccount, self).to_str()
        name = self.account.extra_data.get('name', dflt)
        first_name = self.account.extra_data.get('first_name', None)
        last_name = self.account.extra_data.get('last_name', None)
        if first_name and last_name:
            name = first_name + ' ' + last_name
        return name


class AccessoProvider(OAuth2Provider):
    id = 'accesso'
    name = 'Accesso'
    package = 'attrezzi.accesso'
    account_class = AccessoAccount

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(email=data.get('email'),
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'))

    def get_default_scope(self):
        return ['read', ]

providers.registry.register(AccessoProvider)

