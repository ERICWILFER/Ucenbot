import sqlite3
import json

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

sql_query = "SELECT game_details FROM sports_details"

c.execute(sql_query)

intents = c.fetchall()
# print(intents)

tag_list = []
patterns_list = []
responses_list = []

for intent in intents:
    tag_list.append(intent[0])
    patterns_list.append(intent[0])
    # responses_list.append(intent[0])

print(tag_list)
print(patterns_list)
print(responses_list)

conn.close()

for i in range(len(tag_list)):
    with open("intents.json") as file:
        data = json.load(file)

    intent_list = []
    for intent in data["intents"]:
        intent_list.append(intent)
    # print(intent_list)
    intents_template = {
          "tag": "",
          "patterns": [],
          "responses": [],
          "context_set": [""]
        }
    
    getting_tag = tag_list[i]
    getting_pattern = patterns_list[i]
    # getting_response = responses_list[i]

    update_tag = {"tag": getting_tag}
    update_patterns = {"patterns": [str(getting_pattern)]}
    update_responses = {"responses":[str("")]}

    intents_template.update(update_tag)
    intents_template.update(update_patterns)
    intents_template.update(update_responses)
    # print(intents_template)
    # intent_list.append(intents_template)
    # print(intent_list)
    def write_json(new_data, filename='intents.json'):
        with open(filename,'r+') as file:
              # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["intents"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
    write_json(intents_template)