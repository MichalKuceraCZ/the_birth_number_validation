from main import rodne_cislo
from main import rodne_cislo1


def test_rodne_cislo_negative():
    f = rodne_cislo(cislo="123654/789")
    assert f is False


def test_rodne_cislo_positive():
    f = rodne_cislo(cislo="123654/7890")
    assert f is True


def test_rodne_cislo1_negative():
    f = rodne_cislo1(cislo="123654/789")
    assert f is False


def test_rodne_cislo1_positive():
    f = rodne_cislo1(cislo="123654/7890")
    assert f is True
