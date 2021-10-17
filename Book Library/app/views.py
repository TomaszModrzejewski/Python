from flask import Flask, render_template, request, redirect, url_for
from .models import Books, convert_to_https
from app import app

# Views


@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    return render_template("index.html")


@app.route('/query')
def query():
    """Display search requests and pagination via GET"""
    if not request.args.get("search"):
        return redirect(url_for("index"))

    if request.args.get("start") is None or int(request.args.get("start")) < 0:
        start = 0
    else:
        start = int(request.args.get("start"))

    query = request.args.get('search')
    https = True if app.env != "development" else False
    book_list_parsed = Books(query, start, https=https).parse()

    if len(book_list_parsed["items"]) > 0:
        return render_template("search.html", start=start+1, count=start + len(book_list_parsed["items"]), search=query, data=book_list_parsed)
    else:
        return redirect(url_for("index"))

    @app.errorhandler(404)
    def page_not_found(error):
        """Return 404 for incorrect HTTP queries"""
        return "404 - Page Not Found!", 404

    return app
