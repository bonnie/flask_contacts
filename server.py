from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)

# global to store contacts list
# this would be better done in a database!
contacts = {}

@app.route("/")
def index():
    """Return page with form to add contact."""

    return render_template("index.html", contact_count=contacts.length)


@app.route("/add_contact", methods=['POST'])
def add_contact():
    """Add a contact to the contact dict and reroute to contact list."""


    email = request.form.get('email')
    name = request.form.get('name')
    address = request.form.get('address')
    color = request.form.get('color')
    contacts.append({'email': email, 'name': name, 'address': address, 'color': color})

    return redirect("/contacts")


@app.route("/contacts")
def show_contacts():
    """Show list of contacts."""

    return render_template("contacts.html", contacts=contacts)


@app.route("/contacts/<contact_id>")
def show_contact_info(id:int):
    """Show info for individual contact."""

    return render_template("contact_info", contact_id=contact_id, contacts=contacts)
