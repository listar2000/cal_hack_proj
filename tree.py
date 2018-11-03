# This is the model class for a Tree instance from Omnisci API
from datetime import date
from helper import *

class tree(object):
    tree_id = '10086' # number 1
    zipcode = '00001' # number 26
    created_at = date(2018, 8, 8) # number 0
    health = '0' # number 8

    def __init__(self, data):
        self.parse_data(data)
    
    def parse_data(self, data):
        self.tree_id = data[1]
        self.zipcode = data[26]
        self.created_at = data[0]
        self.health = data[8]

def create_random_tree():
    return tree(random_tree())
