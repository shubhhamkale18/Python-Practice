# The user details get print in the console.
# so you can do whatever you want to do instead
# of printing it
import flask
from flask import Flask, render_template, url_for, redirect
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O/xd5\xa2\xa0\x9fR"\xa1\xa8'

'''
	Set SERVER_NAME to localhost as twitter callback
	url does not accept 127.0.0.1
	Tip : set callback origin(site) for facebook and twitter
	as http://domain.com (or use your domain name) as this provider
	don't accept 127.0.0.1 / localhost
'''

app.config['SERVER_NAME'] = 'localhost:5000'
oauth = OAuth(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/google/')
def google():

	# Google Oauth Config
	# Get client_id and client_secret from environment variables
	# For developement purpose you can directly put it here inside double quotes
	GOOGLE_CLIENT_ID = os.environ.get('896942489996-iahuugduvdgq41019hpk47lmq8cbof7n.apps.googleusercontent.com')
	GOOGLE_CLIENT_SECRET = os.environ.get('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')
	CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
	oauth.register(
		name='google',
		client_id=GOOGLE_CLIENT_ID,
		client_secret=GOOGLE_CLIENT_SECRET,
		server_metadata_url=CONF_URL,
		client_kwargs={
			'scope': 'openid email profile'
		}
	)
	
	# Redirect to google_auth function
	redirect_uri = url_for('google_auth', _external=True)
	return oauth.google.authorize_redirect(redirect_uri)

@app.route('/google/auth/')
def google_auth():
	token = oauth.google.authorize_access_token()
	user = oauth.google.parse_id_token(token)
	print(" Google User ", user)
	return redirect('/')

@app.route('/twitter/')
def twitter():

	# Twitter Oauth Config
	TWITTER_CLIENT_ID = os.environ.get('UHlRsI9H3GYngqK9APrbMac8c')
	TWITTER_CLIENT_SECRET = os.environ.get('kGQ8GjXZQV197FFYxVHESz9mAYCqn81blwZXqOsbCGuNktfgxl')
	oauth.register(
		name='twitter',
		client_id=TWITTER_CLIENT_ID,
		client_secret=TWITTER_CLIENT_SECRET,
		request_token_url='https://api.twitter.com/oauth/request_token',
		request_token_params=None,
		access_token_url='https://api.twitter.com/oauth/access_token',
		access_token_params=None,
		authorize_url='https://api.twitter.com/oauth/authenticate',
		authorize_params=None,
		api_base_url='https://api.twitter.com/1.1/',
		client_kwargs=None,
	)
	redirect_uri = url_for('twitter_auth', _external=True)
	return oauth.twitter.authorize_redirect(redirect_uri)

@app.route('/twitter/auth/')
def twitter_auth():
	token = oauth.twitter.authorize_access_token()
	resp = oauth.twitter.get('account/verify_credentials.json')
	profile = resp.json()
	print(" Twitter User", profile)
	return redirect('/')

@app.route('/facebook/')
def facebook():

	# Facebook Oauth Config
	FACEBOOK_CLIENT_ID = os.environ.get('1002915717017275')
	FACEBOOK_CLIENT_SECRET = os.environ.get('a7df30c11005103bd208b12798513805')
	oauth.register(
		name='facebook',
		client_id=FACEBOOK_CLIENT_ID,
		client_secret=FACEBOOK_CLIENT_SECRET,
		access_token_url='https://graph.facebook.com/oauth/access_token',
		access_token_params=None,
		authorize_url='https://www.facebook.com/dialog/oauth',
		authorize_params=None,
		api_base_url='https://graph.facebook.com/',
		client_kwargs={'scope': 'email'},
	)
	redirect_uri = url_for('facebook_auth', _external=True)
	return oauth.facebook.authorize_redirect(redirect_uri)

@app.route('/facebook/auth/')
def facebook_auth():
	token = oauth.facebook.authorize_access_token()
	resp = oauth.facebook.get(
		'https://graph.facebook.com/me?fields=id,name,email,picture{url}')
	profile = resp.json()
	print("Facebook User ", profile)
	return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)
