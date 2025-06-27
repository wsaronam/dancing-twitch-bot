import requests

client_id = "YOUR_CLIENT_ID" # find this in your Authorized Apps in the bot (after you made an authorized app)
client_secret = "YOUR_CLIENT_SECRET" # this is also found in the authorized app
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