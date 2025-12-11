import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)


API_KEY = "86a9f482"  

@app.route("/", methods=["GET", "POST"])
def index():
    movie_data = None
    error = None

    if request.method == "POST":
        movie_name = request.form.get("movie_name")
        
        if movie_name:
            # OMDb API isteği
            url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"
            try:
                response = requests.get(url)
                data = response.json()

                if data.get("Response") == "True":
                    movie_data = data
                else:
                    error = "Film bulunamadı! (İsmi doğru yazdınız mı?)"
            except:
                error = "API'ye ulaşılamadı, internet bağlantınızı kontrol edin."
                
    return render_template("index.html", movie=movie_data, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
