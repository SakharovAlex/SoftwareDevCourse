from flask import Flask, request
import logging
import os

app = Flask(__name__)

log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=log_level)

open('/app/logs/app.log', 'a').close()

@app.route('/', methods=['GET'])
def greetings():
    logging.info("I am in \"/\" endpoint")
    return "Welcome to the custom app\n", 200

@app.route('/status', methods=['GET'])
def status():
    logging.info("I am in \"/status\" endpoint")
    return {"status": "ok"}, 200

@app.route('/log', methods=['POST'])
def add_log():
    logging.info("I am in \"/log\" endpoint")
    with open('/app/logs/app.log', 'a', encoding='utf-8') as file:
        file.write(data['message'] + '\n')
    return {}, 200

@app.route('/logs', methods=['GET'])
def get_logs():
    logging.info("I am in \"/logs\" endpoint")
    with open('/app/logs/app.log', 'r', encoding='utf-8') as file:
        result = file.read()
    return result, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get('PORT', 8080))
