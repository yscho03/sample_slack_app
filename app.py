from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
 
SLACK_SIGNING_SECRET = "<YOUR_SLACK_SIGNING_SECRET>"
SLACK_BOT_TOKEN = "<YOUR_SLACK_BOT_TOKEN>"
SLACK_APP_TOKEN = "<YOUR_SLACK_APP_TOKEN>"
 
app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)
 
@app.event("app_mention")
def message_handler(message, say):   
    say(f"Hello <@{message['user']}>")
 
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
