import requests
from flask import jsonify
from .utils import get_service_url

def route_request(request, path):
    service = path.split('/')[0]
    service_url = get_service_url(service)
    
    if not service_url:
        return jsonify({'error': f'Service {service} not found'}), 404

    url = f"{service_url}/{path}"
    
    try:
        response = requests.request(
            method=request.method,
            url=url,
            headers={key: value for (key, value) in request.headers if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )
        
        return (
            response.content,
            response.status_code,
            response.headers.items()
        )
    except requests.RequestException as e:
        return jsonify({'error': f'Error communicating with {service}: {str(e)}'}), 500
