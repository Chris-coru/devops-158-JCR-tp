from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "A Warrior acts as if he knows what he is doing - version webhook OK."


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)


