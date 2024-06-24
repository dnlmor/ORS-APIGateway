import requests
from config import Config

def get_service_url(service_name):
    try:
        response = requests.get(f"{Config.SERVICE_DISCOVERY_URL}/graphql", json={
            'query': '''
            query ($name: String!) {
                listServices(name: $name) {
                    host
                    port
                }
            }
            ''',
            'variables': {
                'name': service_name
            }
        })
        response.raise_for_status()
        data = response.json()
        services = data['data']['listServices']
        if services:
            service = services[0]
            return f"http://{service['host']}:{service['port']}"
    except requests.RequestException as e:
        print(f"Error fetching service URL: {str(e)}")
    return None
