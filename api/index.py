from flask import Flask, request, render_template
import qrcode as qr
import base64
import io

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route("/", methods=["GET", "POST"])
def home():

    img = None

    if request.method == "POST":
        data = request.form['data']
        img = qr.make(data)

        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img = base64.b64encode(buffered.getvalue()).decode()

    return render_template("index.html", data=img)


if __name__ == '__main__':
    app.run(debug=True)