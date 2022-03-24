import pytest

from Utility import BrowserOperation


@pytest.fixture(scope="function")
def test_file2_method12():
	print("Start")

@pytest.mark.skip(reason="no way of currently testing this")
def test_B(test_file2_method12):
    print("b")

@pytest.mark.skip(reason="no way of currently testing this")
def test_A():
    print("a")

def test_C():
    print("c")

