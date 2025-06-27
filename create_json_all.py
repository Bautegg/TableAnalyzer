import json
import table_analyzer

method_list = list(table_analyzer.UTA.__dict__.keys())
working_list = []
dicts_elements = {}

for method in method_list:
    if method[:2] == "__":
        print(f"skip {method}")
        continue
    working_list.append(method)
    # working_str = "".join(f"method: {method}")

print(working_list)
 
list_to_json = ['{\n"run_this": [\n']
# list_to_json = []
for i in working_list:
    list_to_json.append(f'{{"method": "{i}"}}\n,')
    
list_to_json[-1] = list_to_json[-1].replace(",", "")
str_to_json = "".join(list_to_json)
    
str_to_json = str_to_json + "]\n}"

with open("config.json", "w+") as f:
    f.write(str(str_to_json))
     

print(list_to_json)
print(str_to_json)