import unittest
import test_runner_12_3
import test_runner_and_tournament_12_3

testRaT = unittest.TestSuite()


testRaT.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner_and_tournament_12_3.TournamentTest))
testRaT.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testRaT)

