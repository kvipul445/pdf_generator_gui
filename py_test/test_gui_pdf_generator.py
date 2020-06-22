import pytest

def selected_files(name):
    name = 'file'
    return name

a = selected_files('file')

assert a == 'file'