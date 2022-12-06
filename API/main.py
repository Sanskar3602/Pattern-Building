app_id = "SZGD59D9UR-100"
app_key = "USXY3C26N3"
redirect_url = "http://www.google.com/"

from fyers_api import fyersModel
from fyers_api import accessToken
import os

def get_access_token(): 
    if not os.path.exists("access_token.txt"):
        session=accessToken.SessionModel(client_id=app_id,
        secret_key=app_key,redirect_uri=redirect_url, 
        response_type="code", grant_type="authorization_code") 
        response = session.generate_authcode()
        print("Login URL: ", response) 
        auth_code = input("Enter Auth code: ")
        session.set_token(auth_code)
        access_token = session.generate_token()["access_token"]
        with open("access_token.txt","w") as f:
            f.write(access_token) 
    else:
        with open("access_token.txt","r") as f:
            access_token = f.read() 
    return access_token

fyers = fyersModel.FyersModel(client_id=app_id, token=get_access_token(), log_path="")