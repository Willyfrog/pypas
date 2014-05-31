import modelo as m


def test_random_size():
    assert 8 == len(m._gen_random())
