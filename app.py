from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

# Starter data stored in memory. Names reset when the app restarts.
names = [
    {"id": 1, "name": "Anna"},
    {"id": 2, "name": "Ben"},
    {"id": 3, "name": "Carlo"},
]
next_id = 4


@app.route("/", methods=["GET", "POST"])
def index():
    global next_id

    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if not name:
            flash("Please enter a name.", "error")
        elif any(item["name"].casefold() == name.casefold() for item in names):
            flash("That name already exists.", "error")
        else:
            names.append({"id": next_id, "name": name})
            next_id += 1
            flash("Name added successfully.", "success")

        return redirect(url_for("index"))

    return render_template("index.html", names=names, edit_item=None)


@app.route("/edit/<int:name_id>", methods=["GET", "POST"])
def edit(name_id):
    item = next((person for person in names if person["id"] == name_id), None)

    if item is None:
        flash("Name not found.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        updated_name = request.form.get("name", "").strip()

        if not updated_name:
            flash("Please enter a name.", "error")
        elif any(person["id"] != name_id and
                 person["name"].casefold() == updated_name.casefold()
                 for person in names):
            flash("Another entry already uses that name.", "error")
        else:
            item["name"] = updated_name
            flash("Name updated successfully.", "success")
            return redirect(url_for("index"))

    return render_template("index.html", names=names, edit_item=item)


@app.route("/delete/<int:name_id>", methods=["POST"])
def delete(name_id):
    global names
    original_count = len(names)
    names = [person for person in names if person["id"] != name_id]

    if len(names) < original_count:
        flash("Name deleted successfully.", "success")
    else:
        flash("Name not found.", "error")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
