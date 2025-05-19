from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["teste"]         # nome do banco
collection = db["submissoes"]   

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "date": request.form["date"],
            "local": request.form["localShow"]
        }
        collection.insert_one(form_data)

        print("Dados enviados:", form_data)
        return redirect("/")
        # Aqui você pode salvar no banco de dados ou enviar para uma API
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
