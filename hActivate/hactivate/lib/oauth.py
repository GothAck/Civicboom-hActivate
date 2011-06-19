import oauth2 as oauth
import httplib
import json

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

def apiCallCheck():
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
        return object
    
def sendSMS(number, text):
    consumer        = oauth.Consumer(key=key, secret=secret)
    token           = oauth.Token(key=token, secret=token_secret)
    
    body = {"smsText": {
            "address":          {"phoneNumber":number},
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
    return status==201