from flask import Flask, render_template

# Always use relative import for custom module
from .package.module import MODULE_VALUE

app = Flask(__name__)

@app.route("/")
def index():
    return (
        "Try /hello/Chris for parameterized Flask route.\n"
        "Try /module for module import guidance.\n"
        "Adding a new line for quick testing on azure deployment."
    )

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