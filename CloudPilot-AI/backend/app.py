from flask import Flask
from routes.home_routes import home_bp
from routes.health_routes import health_bp
from routes.aws_routes import aws_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(health_bp)
app.register_blueprint(aws_bp)

if __name__ == "__main__":
    app.run(debug=True)
