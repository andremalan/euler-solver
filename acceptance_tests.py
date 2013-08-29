import problems
import unittest


class ProblemAcceptanceTest(unittest.TestCase):
    def test_problem3(self):
        self.assertEqual(problems.problem3(), 6857)

    def test_problem4(self):
        self.assertEqual(problems.problem4(), 906609)

if __name__ == '__main__':
    unittest.main()
