from pathlib import Path
import json


DATA_DIR = Path("Data")
DATA_FILE = DATA_DIR/ ".json"


def load_data():
    if DATA_DIR.exists():
        with open(DATA_FILE , "r") as f :
             content = f.read()
             if content.strip():
                 return json.loads(content)
    return []

def save_data(data):
    DATA_DIR.mkdir(parents=True , exist_ok=True) #to create the directory
    with open(DATA_FILE , "w") as f: 
        json.dump(data , f , indent = 2)
