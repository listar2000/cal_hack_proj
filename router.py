from flask import Flask, render_template, redirect, request, url_for
from helper import *
from tree import tree

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('show_tree.html')

@app.route('/search_tree', methods = ['POST'])
def search_tree():
    tree_search_id = request.form['tree_number']
    print(tree_search_id)
    return redirect(url_for('show_tree', tree_id = tree_search_id))

@app.route('/show/<tree_id>')
def show_tree(tree_id):
    tree_results = select_tree(tree_id)
    trees = [tree(data) for data in tree_results] # construct trees
    print('hello', trees)
    if trees:
        return render_template('labeled.html', trees=trees)
    else:     
        return render_template('error.html')

if __name__ == '__main__':
	app.run(debug = True)