import flask
import requests
import time, random
import threading

app = flask.Flask(__name__)

generator_threads = 6
extractor_threads = 2

counter = 0
server2 = 'http://127.0.0.1:5002/api'

qveve = []

@app.post('/api')
def api():
    global qveve
    qveve.append(flask.request.json)
    print(qveve, flush=True)
    return flask.jsonify({"status": "success"})


def data_producer():
    time.sleep(random.randint(0, 10))
    global counter
    counter += 1
    return counter


def send_data(thread, server2):
    while True:
        requests.post(server2, json={'thread': thread, 'counter':data_producer()})



generators = [threading.Thread(target=send_data, args=(i, server2)) for i in range(generator_threads)]

if __name__ == '__main__':
    for thread in generators:
        thread.start()
    
    app.run(host='127.0.0.1', port=5001)
