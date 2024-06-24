from flask import Blueprint, request, jsonify
from .services import route_request

api_gateway_bp = Blueprint('api_gateway', __name__)

@api_gateway_bp.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gateway(path):
    return route_request(request, path)

@api_gateway_bp.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@api_gateway_bp.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500
