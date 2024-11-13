import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner("Усейн", 10)
        self.runner2 = runner_and_tournament.Runner("Андрей", 9)
        self.runner3 = runner_and_tournament.Runner("Ник", 3)


    @classmethod
    def setUpClass(cls):
        TournamentTest.all_results = []

    @classmethod
    def tearDownClass(cls):
        temp_dic = {}
        for item in TournamentTest.all_results:
            for x, y in item.items():
                temp_dic[x] = y.name
            print(temp_dic)



    def test_tournament1(self):
        t1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_results.append(t1.start())

    def test_tournament2(self):
        t2 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_results.append(t2.start())

    def test_tournament3(self):
        t2 = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_results.append(t2.start())

if __name__ == "__main__":
    unittest.main()

