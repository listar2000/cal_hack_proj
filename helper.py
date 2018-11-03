from connect_tool import get_cursor

cursor = get_cursor()

SELECT_QUERY = "SELECT {0} FROM nyc_trees_2015_683k WHERE {1} = {2} LIMIT {3}"
ALL_QUERY = "SELECT * FROM nyc_trees_2015_683k LIMIT 100"

cache = None

def select_tree(attr_name = 'tree_id', value = 169787, ret_item = '*', limit = 20, type = str):
    if type is str:
        value = "{}".format(str(value))
    query = SELECT_QUERY.format(ret_item, attr_name, value, limit)
    return cursor.execute(SELECT_QUERY.format(tree_id)).fetchall()

def random_tree(): # generate a random tree from ALL_QUERY into the database
    global cache
    if not cache:
        cache = cursor.execute(ALL_QUERY)
    return cache.fetchone()
