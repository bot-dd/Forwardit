from flask import Flask

class Bot:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def home():
            return "🤖 Bot is Running!"

        @self.app.route('/status')
        def status():
            return {
                "status": "running",
                "bot": "MyBot",
                "developer": "Rahat",
                "powered_by": "RM Movie Flix"
            }

    def run(self):
        self.app.run(host="0.0.0.0", port=8080)

# Run the Bot
if __name__ == "__main__":
    app = Bot()
    app.run()
