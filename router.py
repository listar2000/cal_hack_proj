from flask import Flask, render_template, redirect, request, url_for

app = Flask('treeApp')

@app.route('/', methods=['GET'])
def index():
    return render_template('show_tree.html')

@app.route('/search_tree', methods = ['POST'])
def search_tree():
    tree_search_id = request.form['tree_number']
    print(tree_search_id)
    return redirect(url_for('index'))