from flask import Blueprint, jsonify
from services.health_service import get_health

health_bp = Blueprint("health", __name__)

@health_bp.route("/health")
def health():
    data = get_health()
    return jsonify(data), 200
