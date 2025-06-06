import configparser
import json
import os
from flask import Flask, jsonify

app = Flask(__name__)
config_data = {}

def parse_config(file_path):
    global config_data
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        config_data = {section: dict(config.items(section)) for section in config.sections()}

        # Save to JSON file
        with open('config_output.json', 'w') as f:
            json.dump(config_data, f, indent=4)

    except FileNotFoundError:
        print("❌ Configuration file not found.")
    except Exception as e:
        print(f"❌ Error reading configuration: {e}")

@app.route("/config", methods=["GET"])
def get_config():
    return jsonify(config_data)

if __name__ == "__main__":
    parse_config("config.ini")
    app.run(debug=True, port=5000)
