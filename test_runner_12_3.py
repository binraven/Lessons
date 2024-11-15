import Runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_wolk(self):
        wolk_ = Runner.Runner("Test wolk")
        for _ in range(1, 11):
            wolk_.walk()
        self.assertEqual(wolk_.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        run_ = Runner.Runner("Test run")
        for _ in range(1, 11):
            run_.run()
        self.assertEqual(run_.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        wolk_2 = Runner.Runner("Test wolk")
        run_2 = Runner.Runner("Test run")
        for _ in range(1, 11):
            run_2.run()
            wolk_2.walk()
        self.assertNotEqual(run_2, wolk_2)


if __name__ == "__main__":
    unittest.main()
