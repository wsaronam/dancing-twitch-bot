import requests
import time

client_id = "CLIENT_ID" # find this in your Authorized Apps in the bot (after you made an authorized app)
client_secret = "CLIENT_SECRET" # this is also found in the authorized app
refresh_token = "REFRESH_TOKEN" #
code = "CODE_FROM_URL" # this code will be found after running the twitch link posted below
expiration_time = int(time.time()) + 3600  # token to refresh every hour
redirect_uri = "http://localhost"

# Below is the link you will need to use to find the code for the above section.
# Replace the YOUR_CLIENT_ID with the client_id
# If your redirect URI is different, that will need to be changed too.  My bot is hosted on my own machine.
# https://id.twitch.tv/oauth2/authorize?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost&scope=chat:read+chat:edit


url = "https://id.twitch.tv/oauth2/token"

params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "code": code,
    "grant_type": "authorization_code",
    "redirect_uri": redirect_uri
}

# Call this function to get your OAuth password (one-time)
def getOAuthPassword():
    response = requests.post(url, params=params)
    print(response.json())

getOAuthPassword()


# This function currently is not being used.  
# def refreshToken():
#     params_refresh = {
#         "grant_type": "refresh_token",
#         "refresh_token": refresh_token,
#         "client_id": client_id,
#         "client_secret": client_secret
#     }

#     response = requests.post(url, params=params_refresh)
#     data = response.json()

#     if "access_token" in data:
#         print("Token refreshed")
#         print("New access_token:", data["access_token"])
#         print("New refresh_token:", data.get("refresh_token", "N/A"))
#         return data["access_token"]
#     else:
#         print("Failed to refresh:", data)
#         return None


def refreshTokenIfNeeded():
    global access_token, refresh_token, expiration_time

    # this will refresh the token when we're at 60 seconds remaining
    if time.time() >= expiration_time - 60:
        print("Token expiring in approximately 60 seconds.  Refreshing now.")
        params_refresh = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": client_id,
            "client_secret": client_secret
        }

        response = requests.post(url, params=params_refresh)
        data = response.json()

        if "access_token" in data:
            access_token = data["access_token"]
            refresh_token = data.get("refresh_token", refresh_token)
            expiration_time = int(time.time()) + data.get("expires_in", 3600)
            print("Token refreshed!")
        else:
            print("Token refresh failed:", data)
            exit()