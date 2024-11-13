import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner("Усейн", 10)
        self.runner2 = runner_and_tournament.Runner("Андрей", 9)
        self.runner3 = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        temp_dic = {}
        for x, y in cls.all_results.items():
            for key in y:
                temp_dic[key] = y[key].name
            print(temp_dic)



    def test_tournament1(self):
        t1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.all_results[max(self.id().split("."))] = t1.start()
        self.assertTrue("Ник" == self.all_results[max(self.id().split("."))]
        [max(self.all_results[max(self.id().split("."))].keys())])

    def test_tournament2(self):
        t2 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.all_results[max(self.id().split("."))] = t2.start()
        self.assertTrue("Ник" == self.all_results[max(self.id().split("."))]
        [max(self.all_results[max(self.id().split("."))].keys())])

    def test_tournament3(self):
        t3 = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results[max(self.id().split("."))] = t3.start()
        self.assertTrue("Ник" == self.all_results[max(self.id().split("."))]
        [max(self.all_results[max(self.id().split("."))].keys())])


if __name__ == "__main__":
    unittest.main()
