# Flask Hello World Application

This is a basic "Hello, World!" web application built with Flask, a lightweight web framework for Python.

## Requirements

- Python 3.7 or higher
- pip (Python package manager)

## Installation

After having cloned the repository, install the dependencies using :
```bash
pip install -r requirements.txt
```

## Usage

Run the flask server
```bash
flask --app server --debug run
```

Open the browser (localhost:5000) or use curl:
```bash
# -x to specify the GET command,
# -i to displays the header from the response
curl -X GET -i -w '\n' localhost:5000
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.