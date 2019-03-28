from papis_dmenu.dmenu import pick


def test_simple():
    assert(pick([]) == '')
    assert(pick(['test']) == 'test')
