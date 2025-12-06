from flask import Flask, request

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        # You can put anything here (HTML or JSON)
        return {
            "message": "Flask CI/CD demo running on AWS Elastic Beanstalk 🚀",
            "endpoints": ["/health", "/message", "/echo"],
        }, 200

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
