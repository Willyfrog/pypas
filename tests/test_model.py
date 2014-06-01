try:
    from unittest.mock import MagicMock, patch
except ImportError:
    from mock import MagicMock, patch

from nose.tools import ok_, eq_, raises

import modelo

def test_random_size():
    assert 8 == len(modelo._gen_random())

def test_insert():
    with patch('modelo.pastas.insert') as p:
        modelo.add_pasta(1,2,3)
        p.assert_called_with({"user":1, "key":2,"code":3})

def test_check_key_exist():
    with patch('modelo.pastas.find_one') as p:
        p.return_value=1  # not none
        eq_(modelo.check_key(1,2), False)
        
def test_check_key_not_exist():
    with patch('modelo.pastas.find_one') as p:
        p.return_value=None
        eq_(modelo.check_key(1,2), True)

def test_get_pasta():
    with patch('modelo.pastas.find_one') as p:
        modelo.get_pasta(1,2)
        p.assert_called_with(user=1, key=2)

def test_get_some_pasta():
    with patch('modelo.pastas.find') as p:
        modelo.get_some_pasta(1,2)
        p.assert_called_with(_offset=2, _limit=3)

def test_get_user_pasta():
    with patch('modelo.pastas.find') as p:
        modelo.get_user_pasta(1)
        p.assert_called_with(user=1)

def test_is_used_key_isnot():
    with patch('modelo.pastas.find_one') as p:
        p.return_value=None
        eq_(modelo.is_used_key(1,2), False)

def test_is_used_key_itis():
    with patch('modelo.pastas.find_one') as p:
        p.return_value=1
        eq_(modelo.is_used_key(1,2), True)

def test_gen_key():
    with patch('modelo.pastas.find_one') as p:
        p.return_value=None
        something_random = "something_random"
        eq_(modelo.gen_key("me", lambda:something_random), something_random)

@raises(KeyError)
def test_gen_key_error():
    with patch('modelo.pastas.find_one') as p:
        p.return_value=1
        something_random = "somethin_random"
        modelo.gen_key("me", lambda:something_random)


