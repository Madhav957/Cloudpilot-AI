from flask import Flask
from routes.home_routes import home_bp
from routes.health_routes import health_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(health_bp)

if __name__ == "__main__":
    app.run(debug=True)
