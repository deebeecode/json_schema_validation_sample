import jsonschema, json

    
with open('user_schema.json') as schema_file, open('user.json') as json_file:
    json_schema = json.load(schema_file)
    json_object = json.load(json_file)
    jsonschema.validate(instance=json_object, schema=json_schema)    