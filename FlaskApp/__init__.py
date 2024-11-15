from flask import Flask, render_template , redirect
import requests
import logging

# Always use relative import for custom module
from .package.module import MODULE_VALUE

app = Flask(__name__)


# Got url infor mation after following uniport after reseraching about atlas antibodies website:
# Link where protein atlas mentioned about UniProt :  https://www.proteinatlas.org/humanproteome/proteinevidence
# Link to Uniprot where I got the below URL: https://www.uniprot.org/help/api_queries
URL_TO_FETCH_PROTEIN_INTERACTIONS_FROM_UNIPROT = "https://rest.uniprot.org/uniprotkb/search?fields=accession%2Ccc_interaction&format=json&query=Insulin%20AND%20%28reviewed%3Atrue%29&size=10"

@app.route("/")
def index():
    # return (
    #     "Try /hello/Chris for parameterized Flask route.\n"
    #     "Try /module for module import guidance.\n"
    #     "Adding a new line for quick testing on azure deployment."
    # )
    logging.info("Displaying Protein Interactions data")
    try:
        response = requests.get(URL_TO_FETCH_PROTEIN_INTERACTIONS_FROM_UNIPROT)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        data = {"error": "Failed to fetch data"}

    return render_template("index.html", data=data)

@app.route("/hello/<name>", methods=['GET'])
def hello(name: str):
    return f"hello {name}"

@app.route("/module")
def module():
    return f"loaded from FlaskApp.package.module = {MODULE_VALUE}"

@app.route("/atlas")
def atlas():
    logging.info("redirecting to atlas antibodies FAQ page")
    return redirect("https://www.atlasantibodies.com/knowledge-hub/faq-antibody-technologies/?language=en")

if __name__ == "__main__":
    app.run()