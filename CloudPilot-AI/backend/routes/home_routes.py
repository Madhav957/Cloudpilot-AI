from flask import Blueprint, jsonify

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    return jsonify({
        "project": "CloudPilot-AI",
        "version": "0.1.0",
        "status": "Running"
    })
