import json
from flask import Flask
import dataset
try:
    with open("config.json") as jfile:
        try:
            json_config = json.load(jfile)
        except Exception as e:
            json_config = {}
            print("no config loaded from config.json due to errors: %s" % e)
except IOError:
    print("no config provided, running on default values.")
    json_config = {}

app = Flask("__main__")
app.secret_key = json_config.get("secretkey", "replacemeforsomethingunique")

debug = bool(json_config.get("debug", False))

db = dataset.connect(json_config.get("dbstring", "sqlite:///memory"))

PPP = json_config.get("PPP", 20)

lexer_list = json_config.get("lexer_list", [("python", "Python"),
                                            ("raw", "Raw"),
                                            ("clj", "Clojure"),
                                            ("php", "PHP"),
                                            ("html", "HTML"), ])
