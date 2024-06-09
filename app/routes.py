from flask import Blueprint, request, jsonify
import requests

bp = Blueprint('routes', __name__)

@bp.route('/api/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    url = f"http://localhost:5001/{path}"  # URL of the user service
    if request.method == 'GET':
        resp = requests.get(url)
    elif request.method == 'POST':
        resp = requests.post(url, json=request.get_json())
    elif request.method == 'PUT':
        resp = requests.put(url, json=request.get_json())
    elif request.method == 'DELETE':
        resp = requests.delete(url)

    return jsonify(resp.json()), resp.status_code
