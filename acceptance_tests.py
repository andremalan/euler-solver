import problems
import unittest


class ProblemAcceptanceTest(unittest.TestCase):
    def test_problem3(self):
        self.assertEqual(problems.problem3(), 6857)

    def test_problem4(self):
        self.assertEqual(problems.problem4(), 906609)

    def test_problem5(self):
        self.assertEqual(problems.problem5(), 232792560)

    def test_problem7(self):
        self.assertEqual(problems.problem7(), 104743)

    def test_problem8(self):
        self.assertEqual(problems.problem8(), 40824)





if __name__ == '__main__':
    unittest.main()
