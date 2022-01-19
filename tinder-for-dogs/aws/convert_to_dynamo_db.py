import os
import re
import json


def convert_json(
    table_name="dog_table_test_melatonin_2357111317", file_name="./db/dog_metadata.json"
):
    result = {table_name: []}

    records = json.load(open(file_name, "r"))
    for record in records:
        new_record = {"PutRequest": {"Item": dict()}}
        for k, v in record.items():
            if k == "Name":
                new_record["PutRequest"]["Item"]["Name"] = {"S": v}
            else:
                # Still needs to be parsed into a string...
                new_record["PutRequest"]["Item"][k] = {"N": str(v)}
        result[table_name].append(new_record)

    new_file_name = re.sub(
        r"(.*)?/(.*)?\.json", r"\g<1>/\g<2>_dynamodb.json", file_name
    )

    json.dump(result, open(new_file_name, "w+"))


convert_json("dog_table_test_melatonin_2357111317", "./db/dog_metadata.json")
convert_json("user_table_test_melatonin_2357111317", "./db/test_user_metadata.json")
