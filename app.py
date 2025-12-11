import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# API Key'i ortam değişkeninden al (Güvenlik için en iyi pratik)
API_KEY = os.environ.get("OMDB_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    movie_data = None
    error = None

    if request.method == "POST":
        movie_name = request.form.get("movie_name")
        if movie_name and API_KEY:
            # OMDb API'ye istek atıyoruz
            url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"
            response = requests.get(url)
            data = response.json()

            if data.get("Response") == "True":
                movie_data = data
            else:
                error = "Film bulunamadı veya API hatası!"
        elif not API_KEY:
            error = "API Key eksik! Lütfen ortam değişkeni olarak atayın."

    return render_template("index.html", movie=movie_data, error=error)

if __name__ == "__main__":
    # Docker içinde dışarıya açılması için host='0.0.0.0' olmalı
    app.run(host="0.0.0.0", port=5000)
