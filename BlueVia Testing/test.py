'''
Created on 18 Jun 2011

@author: greg
'''

import oauth2 as oauth
import httplib, json
import time

oauthBaseUrl    = "https://api.bluevia.com/services/REST/";

authUrl         = "https://connect.bluevia.com/authorise"

oauthUrls       = {
                   'request' : oauthBaseUrl+'Oauth/getRequestToken',
                   'access'  : oauthBaseUrl+'Oauth/getAccessToken',
                   'sms'     : oauthBaseUrl+'SMS_Sandbox/inbound/445480605/messages'+"?version=v1&alt=json"
                  }

appid           = "468f6918612d54133e8a0dcab2fff79b"
appname         = "FreeHocTest"
key             = "HI11061838986678"
secret          = "QucX67152640"

token           = "1601c3501b79c84c6819cd2b792c087d"
token_secret    = "d9e368e4525b980569e2676b47d55d2e"

mokeyword       = "TESTHOC"
sandkeyword     = "SANDHOC"

sig_hmac        = oauth.SignatureMethod_HMAC_SHA1()

consumer        = oauth.Consumer(key=key, secret=secret)

token           = oauth.Token(key=token, secret=token_secret)

request         = oauth.Request.from_consumer_and_token(consumer, token, "GET", oauthUrls['sms'])#, parameters={'version':'v1', 'alt':'json'})

request.sign_request(sig_hmac, consumer, token)

print sig_hmac.check(request, consumer, token, request.get_parameter('oauth_signature'))

#assert False

connection = httplib.HTTPSConnection("api.bluevia.com")
connection.request("GET", oauthUrls['sms'], headers=request.to_header(realm="https://api.bluevia.com"))

resp = connection.getresponse()
print  resp.read()
