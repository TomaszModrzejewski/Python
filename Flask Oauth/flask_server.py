import time
import requests
from urllib.parse import urlencode

from flask import Flask, request, url_for, jsonify, abort, redirect

from oauth_config import oauth_config

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return f'''
    <h1>OAuth</h1>
    <h2><a href="{url_for('.oauth_login', provider='google')}">Google</a></h2>
    <h2><a href="{url_for('.oauth_login', provider='facebook')}">Facebook</a></h2>
    <h2><a href="{url_for('.oauth_login', provider='naver')}">Naver</a></h2>
    <h2><a href="{url_for('.oauth_login', provider='kakao')}">Kakao</a></h2>
    <h2><a href="{url_for('.oauth_login', provider='twitch')}">Twitch</a></h2>
    
    <h1>OIDC</h1>
    <h2><a href="{url_for('.oidc_login', provider='twitch')}">Twitch</a></h2>
    '''


@app.route('/login/<provider>')
def oauth_login(provider):
    try:
        auth_uri = oauth_config[provider]['auth_uri']
        params = oauth_config[provider]['auth_params']

        params.update({'state': str(time.time()),
                       'redirect_uri': url_for('.oauth_login_callback', provider=provider, _external=True)})
        qs = urlencode(params)

        login_url = auth_uri + '?' + qs
        return redirect(login_url)
    except KeyError:
        abort(404)


@app.route('/login/<provider>/callback')
def oauth_login_callback(provider):
    try:
        token_uri = oauth_config[provider]['token_uri']
        params = oauth_config[provider]['token_params']
        params.update({'code': request.args.get('code'),
                       'state': request.args.get('state', ''),
                       'scope': request.args.get('scope', ''),
                       'redirect_uri': url_for('.oauth_login_callback', provider=provider, _external=True)})

        resp = requests.post(token_uri, data=params)
        data = resp.json()

        return jsonify(data)
    except KeyError:
        abort(404)


@app.route('/oauth/<provider>/me')
def oauth_me(provider):
    access_token = request.args.get('access_token')
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        me_uri = oauth_config[provider]['me_uri']
        resp = requests.get(me_uri, headers=headers)
        me_resp = resp.json()
        return jsonify(me_resp)
    except KeyError:
        abort(404)


@app.route('/login/oidc/<provider>')
def oidc_login(provider):
    try:
        auth_uri = oauth_config[provider]['auth_uri']
        params = {
            # 'response_type': 'token+id_token',
            'response_type': 'token',
            'client_id': oauth_config[provider]['token_params']['client_id'],
            'redirect_uri': url_for('oidc_login_callback', provider=provider, _external=True),
            'scope': '+'.join(['openid'])
        }

        login_url = auth_uri + '?' + '&'.join([f'{k}={v}' for k, v in params.items()])
        return redirect(login_url)
    except KeyError:
        abort(404)


@app.route('/login/oidc/<provider>/callback')
def oidc_login_callback(provider):
    print(request.url)
    print(request.pragma)
    print(request.full_path)
    print(request.path)

    return str(request.url)


if __name__ == '__main__':
    app.run(debug=True)
