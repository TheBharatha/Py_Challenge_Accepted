def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        emp_array = []
        return emp_array

class TestDataUniqueValues(object):
    unique = list()

    @staticmethod
    def get_array():
        import random
        upto = random.randrange(3,25,1)
        for i in range(upto):
            TestDataUniqueValues.unique.append(i)
        random.shuffle(TestDataUniqueValues.unique)
        return(TestDataUniqueValues.unique)

    @staticmethod
    def get_expected_result():
        small = min(TestDataUniqueValues.unique)
        return(TestDataUniqueValues.unique.index(small))

class TestDataExactlyTwoDifferentMinimums(object):
    two_unique = list()

    @staticmethod
    def get_array():
        for i in range(3):
            TestDataExactlyTwoDifferentMinimums.two_unique.append(i)
        TestDataExactlyTwoDifferentMinimums.two_unique[0] = TestDataExactlyTwoDifferentMinimums.two_unique[1]
        return(TestDataExactlyTwoDifferentMinimums.two_unique)

    @staticmethod
    def get_expected_result():
        small = min(TestDataExactlyTwoDifferentMinimums.two_unique)
        return(TestDataExactlyTwoDifferentMinimums.two_unique.index(small))

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False

def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
