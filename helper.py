from link_demo import get_cursor

cursor = get_cursor()

SELECT_QUERY = "SELECT * FROM nyc_trees_2015_683k WHERE tree_id = '{}'"

def select_tree(tree_id = 169787):
    return cursor.execute(SELECT_QUERY.format(tree_id)).fetchall()