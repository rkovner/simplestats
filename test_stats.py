from stats import mean
from nose.tools import assert_equal
def test_mean():
    assert_equal(mean([2,4]), 3)
#test_mean()

def test_float_mean():
    assert_equal(mean([1,2]),1.5)
#test_float_mean()

def test_negative_mean():
    assert_equal(mean([-4, -2]),-3)
#test_negative_mean()

def test_float_mean():
    assert_equal(mean([3, 6]), 4.5)
#test_negative_mean()
