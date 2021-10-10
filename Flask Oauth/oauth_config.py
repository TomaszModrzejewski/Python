"""
google https://developers.google.com/identity/protocols/OAuth2WebServer
naver https://developers.naver.com/docs/login/api/
kakao https://developers.kakao.com/docs/restapi/user-management
facebook https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow
twitch https://dev.twitch.tv/docs/authentication/getting-tokens-oidc#oidc-authorization-code-flow
"""

import settings


def gen_oauth_scope(provider, scopes):
    if type(scopes) == str:
        pass
    elif type(scopes) == list:
        if provider == 'google':
            scopes = ' '.join(scopes)
        elif provider == 'kakao':
            scopes = ','.join(scopes)
        elif provider == 'twitch':
            scopes = ''  # FIXME
        else:
            scopes = ''.join(scopes)
    return scopes


oauth_config = {
    'google': {
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://oauth2.googleapis.com/token',
        'me_uri': 'https://www.googleapis.com/oauth2/v1/userinfo',
        'auth_params': {
            'state': '',
            'redirect_uri': '',
            'client_id': settings.google_client_id,
            'scope': gen_oauth_scope('google', ['https://www.googleapis.com/auth/userinfo.profile',
                                                'https://www.googleapis.com/auth/userinfo.email',
                                                # 'https://www.googleapis.com/auth/youtube.force-ssl',
                                                # 'https://www.googleapis.com/auth/drive.metadata.readonly',
                                                ]),
            'access_type': 'offline',
            'include_granted_scopes': 'true',
            'response_type': 'code'
        },
        'token_params': {
            'code': '', 'scope': '', 'state': '',  # from request.args
            'redirect_uri': '',
            'client_id': settings.google_client_id,
            'client_secret': settings.google_client_secret,
            'grant_type': 'authorization_code'
        }
    },
    'kakao': {
        'auth_uri': 'https://kauth.kakao.com/oauth/authorize',
        'token_uri': 'https://kauth.kakao.com/oauth/token',
        'me_uri': 'https://kapi.kakao.com/v1/user/me',
        'auth_params': {
            'state': '',
            'redirect_uri': '',
            'client_id': settings.kakao_client_id,
            'response_type': 'code',
            'encode_state': 1,
        },
        'token_params': {
            'code': '',
            'redirect_uri': '',
            'client_id': settings.kakao_client_id,
            'client_secret': settings.kakao_client_secret,
            'grant_type': 'authorization_code',
        }
    },
    'naver': {
        'auth_uri': 'https://nid.naver.com/oauth2.0/authorize',
        'token_uri': 'https://nid.naver.com/oauth2.0/token',
        'me_uri': 'https://openapi.naver.com/v1/nid/me',
        'auth_params': {
            'scope': gen_oauth_scope('naver', ''),
            'redirect_uri': '',
            'client_id': settings.naver_client_id,
            'state': '',
            'response_type': 'code',
        },
        'token_params': {
            'code': '', 'state': '',
            'client_id': settings.naver_client_id,
            'client_secret': settings.naver_client_secret,
            'grant_type': 'authorization_code',
        }
    },
    'facebook': {
        'auth_uri': 'https://graph.facebook.com/oauth/authorize',
        'token_uri': 'https://graph.facebook.com/oauth/access_token',
        'me_uri': 'https://graph.facebook.com/me',
        'auth_params': {
            'state': '',
            'redirect_uri': '',
            'client_id': settings.facebook_client_id,
            'scope': gen_oauth_scope('facebook', []),
            'response_type': 'code',
        },
        'token_params': {
            'code': '', 'scope': '', 'state': '',
            'redirect_uri': '',
            'client_id': settings.facebook_client_id,
            'client_secret': settings.facebook_client_secret,
            'grant_type': 'authorization_code',
        }
    },
    'twitch': {
        'auth_uri': 'https://id.twitch.tv/oauth2/authorize',
        'token_uri': 'https://id.twitch.tv/oauth2/token',
        'me_uri': '',
        'auth_params': {
            'state': '',
            'redirect_uri': '',
            'client_id': settings.twitch_client_id,
            'scope': gen_oauth_scope('twitch', []),
            'response_type': 'code',
        },
        'token_params': {
            'code': '', 'scope': '', 'state': '',
            'redirect_uri': '',
            'client_id': settings.twitch_client_id,
            'client_secret': settings.twitch_client_secret,
            'grant_type': 'authorization_code',
        }
    }
}
