from flask import Flask, request
from curl_cffi import requests

app = Flask(__name__)

@app.route('/')
def hello_http():    
    request_args = request.args

    if request_args and 'url' in request_args:
        url = request_args['url']
    else:
        return "Error: No URL provided in the GET request", 400

    # add an impersonate parameter
    response = requests.get(
        url,
        impersonate="chrome"
    )

    # verify response status
    if response.status_code != 200:
        return f"An error occurred with status {response.status_code}", response.status_code
    else:
        # return the website's HTML if the response status is okay  
        return response.text, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
