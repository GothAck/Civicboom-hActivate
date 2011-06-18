'''
Created on 18 Jun 2011

@author: greg
'''

import oauth2 as oauth
import time

oauthBaseUrl    = "https://api.bluevia.com/services/REST/";

authUrl         = "https://connect.bluevia.com/authorise"

oauthUrls       = {
                   'request' : oauthBaseUrl+'Oauth/getRequestToken',
                   'access'  : oauthBaseUrl+'Oauth/getAccessToken',
                   'sms'     : oauthBaseUrl+'SMS_Sandbox/inbound/524040/messages?version=v1&alt=json'
                  }

appid           = "468f6918612d54133e8a0dcab2fff79b"
appname         = "FreeHocTest"
key             = "HI11061838986678"
secret          = "QucX67152640"

token           = "4f57ee917d8be4a1a77012d22141c5b4"
token_secret    = "4dbc8d7c994ab84e0cf76ef3e73c23e3"

mokeyword       = "TESTHOC"
sandkeyword     = "SANDHOC"

sig_hmac        = oauth.SignatureMethod_HMAC_SHA1()

params          = {
                   "realm"                  : "https://api.bluevia.com",
                   "oauth_version"          : "1.0",
                   "oauth_nonce"            : oauth.generate_nonce(),
                   "oauth_timestamp"        : int(time.time()),
                   "oauth_signature_method" : "HMAC-SHA1",
                   "oauth_token"            : token,
                   "oauth_consumer_key"     : key,
                  }

consumer        = oauth.Consumer(key=key, secret=secret)

token           = oauth.Token(key=token, secret=token_secret)

request         = oauth.Request.from_consumer_and_token(consumer, token, "GET", oauthUrls['sms'])

request.sign_request(sig_hmac, consumer, token)

client          = oauth.Client(consumer)

resp, content   = client.request(oauthUrls['sms'], "GET", headers=request.to_header(realm=params['realm']))

print resp, content
