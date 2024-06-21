from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_validate_correct_var_name():
    test_payload = {
        "data": [
            {"var_name": "country", "category": "UK"},
            {"var_name": "age_group", "category": "30-50"}
            ]}
    
    response = client.post("/validate",
                           json=test_payload)
    print(response)
    assert response.status_code == 200
    assert response.json() == {"message": "Both var_name values and Category values are correct."}

def test_validate_incorrect_var_name():
    test_payload = {
        "data": [
            {"var_name": "nation", "category": "UK"},
            {"var_name": "age_group", "category": "30-50"}
            ]}
    
    response = client.post("/validate",
                           json=test_payload)
    correct_msg = {"message": "var_name: var_name has to one of {'age_group', 'country'}. Got nation instead. cat_fields: var_name: nation is not found. var_name has to one of ('country', 'age_group')"}
    actual_msg = response.json()

    assert response.status_code == 200
    assert actual_msg == correct_msg
    
def test_validate_incorrect_category_fields():
    test_payload = {
        "data": [
            {"var_name": "country", "category": "UKUK"},
            {"var_name": "age_group", "category": "30-50"}
            ]}
    
    response = client.post("/validate",
                           json=test_payload)
    print(response)
    assert response.status_code == 200
    assert response.json() == {"message": "var_name: var_name values are correct. cat_fields: The category has to one of (\"UK\", \"Australia\", \"China\", \"Japan\") for country. Got UKUK instead."}

def test_get_factors():
    test_payload = {
        "data": [
            {"var_name": "country", "category": "UK"},
            {"var_name": "age_group", "category": "30-50"}
            ]}
    
    response = client.post("/get_factors",
                           json=test_payload)
    correct_response_json = {
        "results": [
            {
              "var_name": "country",
              "category": "UK",
              "factor": 0.25
            },
            {
              "var_name": "age_group",
              "category": "30-50",
              "factor": 0.33
            }
          ]
        }
    assert response.status_code == 200
    assert response.json() == correct_response_json