from flask import Flask, request

app = Flask(__name__)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    return f"🎉 인증 성공! 받은 code: {code}"

if __name__ == "__main__":
    app.run()
