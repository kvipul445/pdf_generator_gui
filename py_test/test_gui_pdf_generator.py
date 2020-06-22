import pytest

@pytest.mark.parametrize('name','file')
def test_selected_files(name):
    return name

a = test_selected_files('file')

assert a == 'file'