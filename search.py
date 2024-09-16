import json
import re

def search_json(json_data, search_string):
    results = []
    search_pattern = re.compile(re.escape(search_string), re.IGNORECASE) 
    results = [entry for entry in json_data if re.search(search_pattern, entry['User'])]
    return results