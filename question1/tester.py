from testbook import testbook

@testbook('./main.ipynb', execute=True)
def test_func(tb):
    func = tb.get('add')
    assert func(1, 2) == 3