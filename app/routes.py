from flask import jsonify, request
from app import create_app
import requests

app = create_app()
app.config.from_object('app.config.Config')

@app.route('/graphql', methods=['POST'])
@jwt_required
def graphql_proxy():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({"message": "Unauthorized"}), 401

    service = request.json.get('service')
    if not service:
        return jsonify({"message": "Service parameter is required"}), 400

    data = request.json
    headers = {'Authorization': request.headers.get('Authorization')}

    if service == 'user':
        url = app.config['USER_SERVICE_URL']
    elif service == 'menu':
        url = app.config['MENU_SERVICE_URL']
    elif service == 'order':
        url = app.config['ORDER_SERVICE_URL']
    elif service == 'payment':
        url = app.config['PAYMENT_SERVICE_URL']
    elif service == 'notification':
        url = app.config['NOTIFICATION_SERVICE_URL']
    elif service == 'service_discovery':
        url = app.config['SERVICE_DISCOVERY_URL']
    else:
        return jsonify({"message": "Invalid service"}), 400

    response = requests.post(url, json=data, headers=headers)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
