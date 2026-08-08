from flask import Blueprint, jsonify
from services.ec2_service import get_instances, get_instance_details

ec2_bp = Blueprint("ec2", __name__)


@ec2_bp.route("/aws/ec2/instances/<instance_id>", methods=["GET"])
def instance_details(instance_id):
    data = get_instance_details(instance_id)

    if data is None:
        return jsonify({
            "success": False,
            "error": "Instance not found"
        }), 404

    return jsonify({
        "success": True,
        "instance": data
    }), 200