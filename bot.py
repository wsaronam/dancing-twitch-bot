import time
import socket
import re

from oauth import refreshTokenIfNeeded




TWITCH_SERVER = "irc.chat.twitch.tv"
TWITCH_SERVER_PORT = 6667

botUsername = "ENTER_BOT_USERNAME_HERE"
botPassword = "oauth:ENTER_BOT_PASSWORD_HERE" # there might be a better way for this
channelToJoin = "#ENTER_CHANNEL_HERE" # this is the channel the bot will listen to (comments)

# these are the emotes that the bot will copy and paste in the chat when it comes up
EMOTES_TO_COPY = ["catJam", "catJAM", "ratJAM", "AYAYAjam", "dogJAM", "batJAM", "babyJAM", 
                  "xddJAM", "hoganJAM", "lebronJAM", "Jamgie", "Jammies", "garfJam", "kittyJam",
                  "AlienPls3", "dancepls", "vibePls", "SussyPls", "AlienPls", "PartyPls", "widetime",
                  "widetimepls", "SEXO", "WIDESEXO", "pepeD", "headBang", "blobDance", "PepoDance",
                  "catDisco", "duckDisco", "hamsterDance", "wideVIBE", "RaveDance", "xddtime", "CatTime"]




def sendMessage(sock, message):
    message_temp = f"PRIVMSG {channelToJoin} :{message}\r\n"
    sock.send(message_temp.encode("utf-8"))


def connectToChannel(sock) -> bool:
    try:
        sock.connect((TWITCH_SERVER, TWITCH_SERVER_PORT))
        sock.send(f"PASS {botPassword}\r\n".encode("utf-8"))
        sock.send(f"NICK {botUsername}\r\n".encode("utf-8"))
        sock.send(f"JOIN {channelToJoin}\r\n".encode("utf-8"))

        print(f"Connected to {channelToJoin} as {botUsername}")
        return True
    
    except:
        return False
    

# This function will check if the server responds with a ping or something else.
# If it's a ping, we will tell the server the bot is still here
def checkPing(sock, response) -> bool:
    if response.startswith("PING"):
        sock.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        return True
    else:
        return False





def main():

    sock = socket.socket()
    connected = connectToChannel(sock)

    while connected:
        refreshTokenIfNeeded() # check if the token needs to be refreshed and will refresh it if needed

        response = sock.recv(2048).decode("utf-8")
        
        # if the response from Twitch is a ping, skip current iteration
        if checkPing(sock, response):
            continue

        # this will look for IRC messages sent by users in the chat.  This will get the ENTIRE IRC response (doesn't look exactly like a chat message)
        foundChatMessage = re.search(r"PRIVMSG #[^\s]+ :(.*)", response)
        if foundChatMessage:
            message = foundChatMessage.group(1) # this makes the IRC response more like a chat message
            for emote in EMOTES_TO_COPY:
                if emote in message:
                    print(f"copying emote: {emote}")
                    sendMessage(sock, emote)
                    time.sleep(10)
                    break



if __name__ == "__main__":
    main()