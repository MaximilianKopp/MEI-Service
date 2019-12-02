from flask import Flask, jsonify, request
import verovio
import sys; sys.path.insert(0, "/usr/local/lib/python3.7/site-packages")
print(sys.path)

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"status": "service started"})


tk = verovio.toolkit()


class Rendering:
    tk = verovio.toolkit()

    def pae_to_mei(self, clef, keysig, timesig, score):
        data = "@clef:" + clef + "\n" + "@keysig:" + keysig + "\n" + "@timesig:" + timesig + "\n" + "@data:" + score
        self.tk.loadData(data)
        return self.tk.getMEI()

    pass


@app.route("/test", methods=['POST'])
def send_mei():
    req_data = request.get_json()
    clef = req_data['clef']
    keysig = req_data['keysig']
    timesig = req_data['timesig']
    score = req_data['score']

    mei_response = Rendering.pae_to_mei(Rendering(), clef, keysig, timesig, score)

    return mei_response


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5000)
