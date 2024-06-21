import json


def create_json(data=None):
    """create required json and saved to a local file"""
    if not data:
        data = {
                "data": [
                    {"var_name": "country", "category": "UK", "factor": 0.25},
                    {"var_name": "country", "category": "Australia", "factor": 0.25},
                    {"var_name": "country", "category": "China", "factor": 0.25},
                    {"var_name": "country", "category": "Japan", "factor": 0.25},
                    {"var_name": "age_group", "category": "18-30", "factor": 0.33},
                    {"var_name": "age_group", "category": "30-50", "factor": 0.33},
                    {"var_name": "age_group", "category": "50+", "factor": 0.34}
                ]
            }
    
    with open("data.json", "w") as f:
        json.dump(data, f)