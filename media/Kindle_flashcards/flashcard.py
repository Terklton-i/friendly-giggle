import json
import requests


loading = 0


def get_api(word):

    root_dict = requests.get(
        "https://www.dictionaryapi.com/api/v3/references/collegiate/json/{}?key=94e310ef-372f-40db-832a-adc772bb7824".format(word))

    return root_dict.text


with open("/Users/igorparshkin/Python_extravaganza/python_virtual_env/portfolio/mysite/media/test.json") as lookups_log:

    json_array = json.load(lookups_log)
    with open("/Users/igorparshkin/Python_extravaganza/python_virtual_env/portfolio/mysite/projects/templates/projects/test.html", "w") as file:

        file.write("""{% extends "projects/base.html" %}""")
        file.write("\n")
        file.write("{% block content %}")
        file.write("\n")

        for item in json_array:
            word = item["word_key"].split(":")[1]
            context = item["usage"]

            root_dict = get_api(word)

            json_array_2 = json.loads(root_dict)

            for i in json_array_2:
                try:
                    word_updated = i["meta"]["id"]
                    definition = i["shortdef"][0]

                    if ":" in word_updated:
                        word_updated = word_updated.split(":")[0]
                    file.write("<p>")
                    file.write("\n")
                    file.write(word_updated)

                    file.write(":\t")

                    file.write(definition)
                    file.write("\n")
                    file.write("</p>")
                    file.write("\n")
                except (IndexError, TypeError):
                    print("Failed to define the word ", word)
                    break
                break

            loading += 1
            print("Have processed ", loading,
                  " words." " Last word processed is", word_updated)

            file.write("\n")

        file.write("{% endblock content %}")
print("All Done")
