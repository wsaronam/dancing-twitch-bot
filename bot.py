import time




botUsername = "ENTER_BOT_USERNAME_HERE"
botPassword = "ENTER_BOT_PASSWORD_HERE" # there might be a better way for this
focusChannel = "ENTER_CHANNEL_HERE" # this is the channel the bot will listen to (comments)

# these are the emotes that the bot will copy and paste in the chat when it comes up
EMOTES_TO_COPY = ["Kappa"]



def sendMessage():
    return

def connectToChannel():
    return False




def main():

    connected = connectToChannel()

    while connected:
        message = "Hello, World!"  # we need to grab the chat messages here
        for emote in EMOTES_TO_COPY:
            if emote in message:
                pass
                #sendMessage()
                #time.sleep(10)

        print("helo, world!")



if __name__ == "__main__":
    main()