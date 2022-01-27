"""Route declaration."""
from flask import current_app as app
from flask import (url_for,render_template,redirect,make_response)

from .forms import ContactForm

@app.route("/")
def home():
    """Landing page."""
    nav = [
        {'name': 'Home', 'url': 'https://example.com/1'},
        {'name': 'About', 'url': 'https://example.com/2'},
        {'name': 'Pics', 'url': 'https://example.com/3'}
    ]

    return render_template(
        'index.html',
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja."
    )

@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.html",
        form=form,
        template="form-template"
    )

@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(
        render_template("404.html"),
         404
    )

@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return make_response(
        render_template("500.html"),
        500
    )
  