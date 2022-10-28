import flask
import threading
import requests
import time

qveve = []
extractor_threads = 4
server2 = 'http://127.0.0.1:5001/api'

app = flask.Flask(__name__)


@app.post('/api')
def api():
    global qveve
    qveve.append(flask.request.json['counter'])

    print(flask.request.json, flush=True)
    print(qveve, flush=True)
    return flask.jsonify({"status": "success"})

def return_data(thread, server2):
    global qveve
    time.sleep(5)
    while True:
        if len(qveve) > 0:
            ii = qveve.pop()
            requests.post(server2, json={'thread': thread, 'ii':ii})



extractors = [threading.Thread(target=return_data, args=(i, server2)) for i in range(extractor_threads)]


if __name__ == '__main__':
    for extractor in extractors:
        extractor.start()

    app.run(host='127.0.0.1', port=5002)
