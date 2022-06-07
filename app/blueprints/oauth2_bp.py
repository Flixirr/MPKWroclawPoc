import os
from flask import Response, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

client_id = os.getenv('GOOGLE_CLIENT_ID')
client_secret = os.getenv('GOOGLE_CLIENT_SECRET')

oauth2_bp = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    reprompt_consent=True,
    scope=["profile", "email"]
)

@oauth2_bp.route('/')
def sso_check():
    data_from_auth = None

    user_info_endpoint="/oauth2/v2/userinfo"

    if google.authorized:
        data_from_auth = google.get(user_info_endpoint).json()

        return Response({'Authorized'}, status=200)
    
    return Response({'Not authorized'}, status=400)

@oauth2_bp.route('/login')
def sso():
    return redirect(url_for('google.login'))