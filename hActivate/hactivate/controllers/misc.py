from hactivate.lib.base import *
import oauth2 as oauth
import httplib
import json

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

class MiscController(BaseController):
    """
    """
    def titlepage(self):
        return render("titlepage.mako")
    
    def test(self):
        return render("test.mako")
    
    def apiCallCheck(self):
        consumer        = oauth.Consumer(key=key, secret=secret)
        token           = oauth.Token(key=token, secret=token_secret)
        request         = oauth.Request.from_consumer_and_token(consumer, token, "GET", oauthUrls['sms'])#, parameters={'version':'v1', 'alt':'json'})
        request.sign_request(sig_hmac, consumer, token)
        connection = httplib.HTTPSConnection("api.bluevia.com")
        connection.request("GET", oauthUrls['sms'], headers=request.to_header(realm="https://api.bluevia.com"))
        resp = connection.getresponse()
        data = resp.read()
        
        if data:
            object = json.load(data)
            for obj in object.get('receivedSMS', {}).get('receivedSMS', []):
                pass
            
        
        