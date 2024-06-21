from src.helpers import validate_var_name, validate_cat_fields, get_factors_helper
from fastapi import FastAPI


app = FastAPI()

# define types
Record = dict[str, str | float]
FactorRequest = dict[str, str]


@app.post("/validate")
def validate(payload: dict[str, list[Record]]) -> dict[str, str]:
    var_name_res = validate_var_name(payload)
    cat_fields_res = validate_cat_fields(payload)
    print(cat_fields_res)

    if var_name_res["message"] == "var_name values are correct." and cat_fields_res["message"] == "Category values are correct.":
        return {"message": "Both var_name values and Category values are correct."}
    else:
        return {"message": f"var_name: {var_name_res['message']} cat_fields: {cat_fields_res['message']}"}


@app.post("/get_factors")
def get_factors(payload: dict[str, list[FactorRequest]]) -> dict[str, list[Record]]:
    res = get_factors_helper(payload)
    return res

            
if __name__ == "__main__":
    pass