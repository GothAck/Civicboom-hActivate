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
                   'sms'     : oauthBaseUrl+'SMS_Sandbox/inbound/445480605/messages'+"?version=v1&alt=json",
                   'smsSend' : oauthBaseUrl+'SMS/outbound/requests'+"?version=v1",
                  }

appid           = "468f6918612d54133e8a0dcab2fff79b"
appname         = "FreeHocTest"
key             = "HI11061838986678"
secret          = "QucX67152640"

token           = "1cff2685c6ef5e4c7f58360077d21694"
token_secret    = "ac28ce7e496326ea66a030551cbb5e31"

mokeyword       = "TESTHOC"
sandkeyword     = "SANDHOC"

sig_hmac        = oauth.SignatureMethod_HMAC_SHA1()

consumer        = oauth.Consumer(key=key, secret=secret)

token           = oauth.Token(key=token, secret=token_secret)


#assert False

body = {"smsText": {
            "address":          {"phoneNumber":"447928065717"},
            "message":          "Message here",
            "originAddress":    {"alias": token.key},
            },
        }

request         = oauth.Request.from_consumer_and_token(consumer, token, "POST", oauthUrls['smsSend'])#, parameters={'version':'v1', 'alt':'json'})
request.sign_request(sig_hmac, consumer, token)    

body = json.dumps(body)
connection = httplib.HTTPSConnection("api.bluevia.com")

headers = request.to_header(realm="https://api.bluevia.com")

headers.update({'Content-Type': 'application/json'});

connection.request("POST", oauthUrls['smsSend'],headers=headers, body=body)

resp = connection.getresponse()
data = resp.read()

print data, resp.status, resp.reason
