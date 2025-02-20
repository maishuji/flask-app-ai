# Flask AI Project with IBM Watson Libraries  

This project is focused on integrating AI functionality into web applications using Embeddable Watson AI libraries. 
## Goal
 - build two AI-based apps
 - learn essential practices like unit testing, static code analysis, and error handling. 

## Requirements

- Python 3.7 or higher
- pip (Python package manager)
- Flask 2.x (installation through requirements.txt)
- IBM Watson SDK




## Installation



After having cloned the repository, create and activate python env:

```bash
python -m venv <myenv>
source ./<myenv>/bin/activate

```
THen install the dependencies:

```bash
pip install -r requirements.txt
```

## Set up IBM Watson API credentials
Add your credentials to an ```.env``` file at the root of the project
```bash
WATSON_API_KEY=your-api-key  
WATSON_URL=your-service-url  
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

This project is licensed under the Apache License. See the LICENSE file for details.
