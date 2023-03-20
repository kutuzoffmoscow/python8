
from os.path import exists
from CSV_creating import creating
from controller import *

valid = exists('Phonebook.csv')
if not valid:
    creating()

greeting()

choice_todo()