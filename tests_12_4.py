'''
Задача "Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.

Дополните методы тестирования в классе RunnerTest следующим образом:
test_walk:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте отрицательное значение в speed.
В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
test_run:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте что-то кроме строки в name.
В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
Пример результата выполнения программы:

'''
import unittest
from unittest import TestCase
import random
import runner_and_tournament as rat

import logging

class RunnerTest(unittest.TestCase):
    #@unittest.skipIf(random.choice([True, False]), 'Не повезло,Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner1=rat.Runner('бегун 1',-10)
            if runner1.speed>0:
                logging.info(f'"test_walk" выполнен успешно')
                for i in range(10):
                    runner1.walk()
                self.assertEqual(runner1.distance, 50)
                logging.info(f'"test_walk" выполнен успешно')
            else:
                raise Exception(f'Отрицательная скорость: {runner1.speed}')
        except Exception as ex:
            logging.warning(f"Неверная скорость для Runner, тип ошибки {ex}")


    #@unittest.skipIf(random.choice([True, False]), 'Не повезло,Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner2 = rat.Runner(134)
            if  isinstance(runner2.name,str):
                for i in range(10):
                    runner2.run()
                self.assertEqual(runner2.distance, 100)
                logging.info(f'"test_run" выполнен успешно')
            else:
                raise TypeError(f'TypeError, передан {type(runner2.name)}')
        except TypeError as ex:
            logging.warning(f"Неверный тип данных для объекта Runner, тип ошибки {ex}")
    #@unittest.skipIf(random.choice([True, False]), 'Не повезло,Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1=rat.Runner('бегун 1')
        runner2=rat.Runner('бегун 2')

        runner1.walk()
        runner2.run()

        self.assertNotEqual(runner1.distance,runner2.distance)


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rat.Runner('Усэйн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
                print(i)

    #@unittest.skipIf(random.choice([True, False]), 'Не повезло,Тесты в этом кейсе заморожены')
    def test1_start(self):
        tir1 = rat.Tournament(90, self.runner1, self.runner3)
        res=tir1.start()
        results={}
        for key,value in res.items():
            results[key]=value.name
        self.all_results[0] = results

    #@unittest.skipIf(random.choice([True,False]),'Не повезло,Тесты в этом кейсе заморожены')
    def test2_start(self):
        tir2 = rat.Tournament(90, self.runner2, self.runner3)
        res=tir2.start()
        results = {}
        for key,value in res.items():
            results[key]=value.name
        self.all_results[1] = results

    #@unittest.skipIf(random.choice([True, False]), 'Не повезло,Тесты в этом кейсе заморожены')
    def test3_start(self):
        tir3 = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        res=tir3.start()
        results = {}
        for key,value in res.items():
            results[key]=value.name
        self.all_results[2]=results

logging.basicConfig(level=logging.INFO,filemode='w',filename='runner_tests.log',encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")



