from flask import Flask, request, render_template, redirect, url_for, send_file
from scraper import Scrap
from tts import Tts
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")

        if not url:
            return render_template("index.html", error="Please enter a URL.")
        try:
            return redirect(url_for("loading", url=url))
        except Exception as e:
            return render_template("index.html", error=f"Unexpected error: {e}")
    return render_template("index.html")


@app.route("/loading")
def loading():
    url = request.args.get("url")
    scraper = Scrap(url)

    try:
        article_content = scraper.fetch_article_content()

        if article_content:
            tts = Tts()
            output_file = os.path.join("static", "output.mp3")
            tts.convert_text_to_speech(article_content, output_file=output_file)
            return redirect(url_for("download"))
        else:
            return render_template("index.html", error="Failed to retrieve article content. Please try another URL.")
    except Exception as e:
        return render_template("index.html", error=f"Error processing the URL: {e}")


@app.route("/download")
def download():
    return render_template("download.html")


@app.route("/download_file")
def download_file():
    output_file = os.path.join("static", "output.mp3")
    try:
        return send_file(output_file, as_attachment=True)
    except FileNotFoundError:
        return render_template("index.html", error="Error: The audio file could not be found.")


@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)