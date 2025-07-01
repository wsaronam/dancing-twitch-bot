import requests

client_id = "CLIENT_ID" # find this in your Authorized Apps in the bot (after you made an authorized app)
client_secret = "CLIENT_SECRET" # this is also found in the authorized app
refresh_token = "REFRESH_TOKEN" #
code = "CODE_FROM_URL" # this code will be found after running the twitch link posted below
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

response = requests.post(url, params=params)
print(response.json())



def refreshToken():
    params_refresh = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, params=params_refresh)
    data = response.json()

    if "access_token" in data:
        print("Token refreshed")
        print("New access_token:", data["access_token"])
        print("New refresh_token:", data.get("refresh_token", "N/A"))
        return data["access_token"]
    else:
        print("Failed to refresh:", data)
        return None