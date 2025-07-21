from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Ava", "Smith-Jones") == "Smith-Jones; Ava"
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Marie", "Curie") == "Curie; Marie"
    assert make_full_name("Olivier", "Dupont") == "Dupont; Olivier"

def test_extract_family_name():
    assert extract_family_name("Smith-Jones; Ava") == "Smith-Jones"
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Curie; Marie") == "Curie"
    assert extract_family_name("Dupont; Olivier") == "Dupont"

def test_extract_given_name():
    assert extract_given_name("Smith-Jones; Ava") == "Ava"
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("Curie; Marie") == "Marie"
    assert extract_given_name("Dupont; Olivier") == "Olivier"

pytest.main(["-v", "--tb=line", "-rN", __file__])