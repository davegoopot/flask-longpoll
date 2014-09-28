from flask import Flask, Response
import time

app = Flask(__name__)

@app.route("/")
def hello():
    def reply_slowly():
        yield "Please be patient.  I'm counting up to 20\n"
        for i in range(1,21):
            time.sleep(1)
            yield str(i) + "\n"
    return Response(reply_slowly(), mimetype="text/plain")
            
    

if __name__ == "__main__":
    app.run('0.0.0.0')