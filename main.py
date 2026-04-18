from flask import Flask, render_template, request, session, flash, redirect
from flask_session import Session
import os

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = "filesystem"
app.secret_key = 'your_secret_key'

Session(app)

file_save_location = "static/images"

@app.route('/')
def homePage():
    if "items" not in session:
        flash("Since this is your first time, Add an item to get started!")
    return render_template("main.html")

@app.route('/itemDisplay')
def displayItems():
    return render_template('itemDisplay.html', items=session.get("items", {}), file_location="/static/images")

@app.route('/addItem')
def addItem():
    return render_template('addItem.html')

@app.route('/addItem', methods=['POST'])
def itemInput():
    item_name = request.form['item']
    boss_name = request.form['boss_name']
    drop_rate = request.form['drop_rate']
    kill_count = request.form['kill_count']
    file = request.files['item_img']
    if file.filename != '':
        save_file_name = os.path.join(file_save_location, file.filename)
        file.save(save_file_name)

    if "items" in session:
        session["items"][item_name] = {'boss_name':boss_name, 'drop_rate':drop_rate, 'kill_count':kill_count, 'img':file.filename}
    else:
        session["items"] = {}
        session["items"][item_name] = {'boss_name': boss_name, 'drop_rate': drop_rate, 'kill_count': kill_count, 'img':file.filename}

    flash(f"{item_name} has been added!!")
    return render_template('itemDisplay.html', items=session["items"], file_location="/static/images")

@app.route('/removeItems')
def removeItemsForm():
    items = session.get('items', {})
    return render_template('removeItems.html', items=items)

@app.route('/removeItems', methods=['POST'])
def removeItems():
    items = session.get('items', {})
    item_name = request.form.get('item_name')

    if item_name and item_name in items:
        items.pop(item_name)
        session['items'] = items
        flash(f"{item_name} has been removed!!")
    else:
        flash('No item was removed.')

    return render_template('removeItems.html', items=items)

if __name__ == "__main__":
    app.run(host='0.0.0.0')