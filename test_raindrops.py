from raindrops import *


def test_fail():
    assert check_raindrops("bad input") == False


def test_30():
    assert check_raindrops(30) == "PlingPlang"


def test_28():
    assert check_raindrops(28) == "Plong"


def test_34():
    assert check_raindrops(34) == 34

