from flask import Flask, request, render_template


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        # This will look for app/templates/index.html
        return render_template("index.html")

    @app.get("/health")
    def health():
        return {"status": "ok"}, 200

    @app.get("/message")
    def message():
        return {"message": "Keep going, your hard work will pay off!"}, 200

    @app.post("/echo")
    def echo():
        data = request.get_json(silent=True) or {}
        return {"received": data}, 200

    return app
