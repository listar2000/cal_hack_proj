from flask import Flask, render_template,  redirect

app = Flask('treeApp')

@app.route('/', methods=['GET'])
def hello():
    return render_template('show_tree.html')
