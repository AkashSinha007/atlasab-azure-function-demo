from flask import Flask, render_template
import requests

# Always use relative import for custom module
from .package.module import MODULE_VALUE

app = Flask(__name__)


# Got url infor mation after following uniport from atlas antibodies website:
# Link where atlas antibodies mentioned about UniProt :  
# Link to Uniprot where I got the below URL: https://www.uniprot.org/help/api_queries
URL_TO_FETCH_PROTEIN_INTERACTIONS_FROM_UNIPROT = "https://rest.uniprot.org/uniprotkb/search?fields=accession%2Ccc_interaction&format=json&query=Insulin%20AND%20%28reviewed%3Atrue%29&size=10"

@app.route("/")
def index():
    # return (
    #     "Try /hello/Chris for parameterized Flask route.\n"
    #     "Try /module for module import guidance.\n"
    #     "Adding a new line for quick testing on azure deployment."
    # )
    try:
        response = requests.get(URL_TO_FETCH_PROTEIN_INTERACTIONS_FROM_UNIPROT)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        data = {"error": "Failed to fetch data"}

    return render_template("index.html", data=data)

@app.route("/hello/<name>", methods=['GET'])
def hello(name: str):
    # return f"hello {name}"
    html_content = "Hello World"
    return render_template('index.html', content=html_content)

@app.route("/module")
def module():
    return f"loaded from FlaskApp.package.module = {MODULE_VALUE}"

if __name__ == "__main__":
    app.run()