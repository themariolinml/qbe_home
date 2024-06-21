import json


# define types
Record = dict[str, str | float]
FactorRequest = dict[str, str]

def validate_var_name(payload: dict[str, list[Record]]) -> dict[str, str]:
    """validate var_name against the data.json"""
    for row in payload["data"]:
        
        curr_var_name = row["var_name"]

        VALID_VAR_NAME = {"country", "age_group"}
        if curr_var_name not in VALID_VAR_NAME:
                return {"message": f"""var_name has to one of {VALID_VAR_NAME}. Got {curr_var_name} instead."""}
    
    return {"message": "var_name values are correct."}

def validate_cat_fields(payload: dict[str, list[Record]]) -> dict[str, str]:
    """validate category fields against the data.json"""
    for row in payload["data"]:
        
        curr_var_name, curr_cat = row["var_name"], row["category"]  
        VALID_VAR_FOR_AGE_GROUP = {"18-30", "30-50", "50+"}
        VALID_VAR_FOR_COUNTRY = {"UK", "Australia", "China", "Japan"}

         # check for country field values
        if curr_var_name == "country":
            if curr_cat not in VALID_VAR_FOR_COUNTRY:
                return {"message": f"""The category has to one of ("UK", "Australia", "China", "Japan") for country. Got {curr_cat} instead."""}
        elif curr_var_name == "age_group": # check for age_group field values
            if curr_cat not in VALID_VAR_FOR_AGE_GROUP:
                return {"message": f"""The category has to one of {"18-30", "30-50", "50+"} for age group. Got {curr_cat} instead."""}
        else:
            return {"message": f"""var_name: {curr_var_name} is not found. var_name has to one of {"country", "age_group"}"""}

    return {"message": "Category values are correct."}

def get_factors_helper(payload: dict[str, list[FactorRequest]]) -> dict[str, list[Record]]:
    """returns the factors for valid var_name and category"""
    
    with open("src/data.json", "rb") as file:
        DB: dict[str, list[Record]] = json.load(file)

    res: dict[str, list[Record]] = {"results": []}
    for payload_row in payload["data"]:
        curr_var_name, curr_cat = payload_row["var_name"], payload_row["category"]

        for record_row in DB["data"]:
            lookup_var_name, lookup_cat = record_row["var_name"], record_row["category"]

            if lookup_var_name == curr_var_name and lookup_cat == curr_cat:
                res["results"].append(record_row)

    return res

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