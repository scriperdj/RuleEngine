import json
import operator
from datetime import datetime

OPERATORS = {
    "eq": operator.eq,
    "ne": operator.ne,
    "lt": operator.lt,
    "gt": operator.gt,
    "le": operator.le,
    "ge": operator.ge
}

# Load rules in memory
with open("rules.json") as data_file:
    RULES = json.load(data_file)

def get_rule(key):
    try:
        return RULES[key]
    except:
        return ''

# Check if the record is valid as per rules
def check_validity(rec):
    is_invalid = False
    rule = get_rule(rec["signal"] + "_" + rec["value_type"])

    if rule:
        opr = OPERATORS[rule["cond"]]
        if rec["value_type"] == "Datetime":
            left = datetime.now() if rule["value"] == "current" else datetime.strptime(rule["value"], '%Y-%m-%d %H:%M:%S')
            right = datetime.strptime(rec["value"], '%Y-%m-%d %H:%M:%S')
            is_invalid = opr(left,right)
        elif rec["value_type"] == "Integer":
            is_invalid = opr(float(rule["value"]),float(rec["value"]))
        else:
            is_invalid = opr(str(rule["value"]),str(rec["value"]))

    return is_invalid

def check_date_rules(rec):
    valid = True
    return valid

if __name__ == "__main__":
    print("Executing Rules Engine..\n\n")

    # Read raw data from input file
    raw_data=[]
    with open("raw_data.json") as raw_file:
        raw_data = json.load(raw_file)

    # Loop through data & check if it violates any rules
    print("Below are data signals which violates rules.\n")
    for rec in raw_data:
        is_invalid = check_validity(rec)

        if is_invalid:
            print(rec["signal"])

    print("\n\nEnd of execution..")
