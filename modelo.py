import random
import re
import dataset
from pygments import higlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from common import db, PPP

pastas = db['pastas']

def add_pasta(user, key, code):
    """
    Insert a paste into the db
    Arguments:
    - `user`: author
    - `key`: name of the paste
    - `code`: actual paste
    """
    return pastas.insert({"user": user, "key": key, "code": code})

