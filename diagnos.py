from flask import Flask, render_template

app = Flask("diagnos")


@app.route("/")
def home():
	return "Hello world!" 


if __name__ == "__main__":
	app.run()