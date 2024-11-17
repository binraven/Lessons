import rt_with_exceptions_12_4
import unittest
import logging

class RunnerTest(unittest.TestCase):

    def test_wolk(self):
        try:
            wolk_ = rt_with_exceptions_12_4.Runner("Test wolk", 5)
            logging.info("Test wolk пройден успешно")
            for _ in range(1, 11):
                wolk_.walk()
            self.assertEqual(wolk_.distance, 50)
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=err)

    def test_run(self):
        try:
            run_ = rt_with_exceptions_12_4.Runner("Test run")
            logging.info("Test run пройден успешно")
            for _ in range(1, 11):
                run_.run()
            self.assertEqual(run_.distance, 100)
        except TypeError as err:
            logging.warning("Неверный типа данных для объекта Runner", exc_info=err)

    def test_challenge(self):
        wolk_2 = rt_with_exceptions_12_4.Runner("Test wolk")
        run_2 = rt_with_exceptions_12_4.Runner("Test run")
        for _ in range(1, 11):
            run_2.run()
            wolk_2.walk()
        self.assertNotEqual(run_2, wolk_2)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", encoding="UTF-8", filename="runner_tests1.log",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    unittest.main()
