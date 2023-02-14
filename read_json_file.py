import json
import jsonschema


def validate_file(file):
    provided_schema = {
        "firstName": str,
        "secondName": str,
        "ageInYears": int,
        "address": str,
        "creditScore": float
    }
    data = json.loads(file.read())
    try:
        jsonschema.validate(data, provided_schema)
    except jsonschema.exceptions.ValidationError as e:
        return False, e.message
    return True, "Jsonschema Mass"
