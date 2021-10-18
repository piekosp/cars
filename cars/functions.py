import requests

def check_if_car_exists(make, model):
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json'
    r = requests.get(url)
    response = r.json()

    if response.get('Count'):
        results = response.get('Results')
        for result in results:
            response_model = result.get('Model_Name')
            if response_model is not None:
                if model.upper() == response_model.upper():
                    return True
    return False
