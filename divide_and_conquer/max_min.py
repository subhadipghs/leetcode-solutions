import unittest
"""
    Divide and conquer algorithm generalized
    ----------------------------------------
    DivideAndConquer(a, m, n)
        if(subProblem(a, m, n))
            return(solution(a, m, n))
        else
            p = divide(a, m, n)
            b = DivideAndConquer(a, m, mid)
            c = DivideAndConquer(a, mid+1, n)
            d = combine(b, c)
        return(d)

    Complexity -> T(n) = aT(n/b) + f(n)
"""


class DivideAndConqueryAndCombine:

    def min_using_dnc(self, a, index, l):
        """
            Minimum using divide and conquer
        """
        minimum = 1e10
        if index >= l - 2:
            return a[index] if a[index] < a[index + 1] else a[index + 1]
        minimum = self.min_using_dnc(a, index + 1, l)
        if a[index] < minimum:
            return a[index]
        else:
            return minimum

    def max_using_dnc(self, a, index, l):
        """
            Max finding using divide and conquer method
        """
        maximum = -1
        if index >= l - 2:
            return a[index] if a[index] > a[index+1] else a[index+1]
        maximum = self.max_using_dnc(a, index + 1, l)

        if a[index] > maximum:
            return a[index]
        else:
            return maximum


class Tc(unittest.TestCase):
    def test_something(self):
        dnc = DivideAndConqueryAndCombine()
        result = dnc.max_using_dnc(
            [1223, 1, 48, 4, 399], 0, 5)
        self.assertEqual(result, max([1223, 1, 48, 4, 399]))

    def test_divide_n_conquer(self):
        dnc = DivideAndConqueryAndCombine()
        l = [1, 232, 12, 34, 5]
        result = dnc.min_using_dnc(l, 0, len(l))
        self.assertEqual(result, min(l))


if __name__ == "__main__":
    unittest.main()
