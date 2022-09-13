from flask import Flask, request
app = Flask(__name__)

@app.route("/result", methods=["POST", "GET"])
def hello():
    output = request.get_json()
    if len(output.keys()) < 2:
        return {"Status":"Bad response"}

    num1 = int(output['num1'])
    num2 = int(output['num2'])
    cal={}
    cal['addition'] = num1+num2
    return (cal)

if __name__ == "__main__":
    app.run(debug=True, port=2000)
