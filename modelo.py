import random
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from common import DB_STRING, PPP
from string import digits
import dataset


try:
    from string import ascii_letters
except ImportError:
    from string import letters as ascii_letters

pastas = dataset.connect(DB_STRING)['pastas']


def add_pasta(user, key, code):
    """
    Insert a paste into the db.

    Arguments:
    - `user`: author
    - `key`: name of the paste
    - `code`: actual paste
    """
    return pastas.insert({"user": user, "key": key, "code": code})


def check_key(user, key):
    """
    Check if the key is in use for the user.

    Arguments:
    - `user`:
    - `key`:
    """
    return (pastas.find_one(user=user, key=key)) is None


def get_pasta(user, key):
    """
    Find some specific pasta

    Arguments:
    - `num_pastas`:
    - `start_from`:
    """
    return pastas.find_one(user=user, key=key)


def get_some_pasta(num_pastas=PPP, start_from=0):
    """

    Arguments:
    - `num_pastas`:
    - `start_from`:
    """
    return pastas.find(_offset=start_from, _limit=start_from+num_pastas)


def get_user_pasta(user):
    """
    Given a user, get his/her pastas

    Arguments:
    - `user`:
    """
    return pastas.find(user=user)


def is_used_key(user, key):
    """
    Arguments:
    - `user`: user who owns the key
    - `key`: key to be tested
    """

    return (get_pasta(user, key) is not None)


def _gen_random():
    """
    Generate a random key
    """
    return "".join(random.sample(ascii_letters + digits, 8))


def gen_key(user, gen_fun=_gen_random):
    """
    Generate a valid & random key for the user
    """

    key = gen_fun()
    count = 5
    while (count > 0 and is_used_key(user, key)):
        key = gen_fun()
        count -= 1
    if count <= 0:
        raise KeyError("gen_fun function wasn't random enough.")
    return key


def pasta_with_sauce(pasta, lexer):
    """
    Get the pasta and paint it with some color
    """
    lex = get_lexer_by_name(lexer)
    return {
        "user": pasta.get("user", None),
        "key": pasta.get("key", None),
        "code": highlight(pasta["code"], lex, HtmlFormatter(linenos=(lexer!="raw"))),
    }


def num_pastas(user=None):
    if user is None:
        return len(pastas)
    else:
        return len(list(pastas.find(user=user)))
