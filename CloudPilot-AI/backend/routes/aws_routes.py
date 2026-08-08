from flask import Blueprint, jsonify
from services.aws_service import aws_identity


aws_bp = Blueprint("aws", __name__)


@aws_bp.route("/aws/identity")
def identity():
    data = aws_identity()

    return jsonify(data), 200