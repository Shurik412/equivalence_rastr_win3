# -*- coding: utf-8 -*-
from prettytable import PrettyTable

from equivalence.AstraRastr import RASTR


class Regime:
    """
    Расчет режима
    """

    def __init__(self,
                 rastr_win=RASTR,
                 switch_command_line: bool = False):
        """
        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param par: строка дополнительных параметров
            Параметры могут быть следующими:
                "" – c параметрами по умолчанию;
                "p" – расчет с плоского старта;
                "z" – отключение стартового алгоритма;
                "c" – отключение контроля данных;
                "r" – отключение подготовки данных (можно использовать при повторном расчете режима
                      с измененными значениями узловых мощностей и модулей напряжения);
        :param switch_command_line: True/False - вывод сообщений в протокол.
        """
        self.rastr_win = rastr_win
        self.switch_command_line = switch_command_line

    def __bool__(self):
        return self.switch_command_line

    def rgm(self, par: str = ''):
        kod = self.rastr_win.rgm(par)
        if self.switch_command_line:
            self.output_messages_results(kod)
        return kod

    @staticmethod
    def output_messages_results(kod):
        pt = PrettyTable()
        pt.title = "Расчет УР режима"
        pt.field_names = ['Описание', 'Параметр']
        pt.add_row(['Запуск "Расчет режима"', ''])
        if kod != 0:
            pt.add_row(['Сообщение о результатх расчета УР', 'Режим не сбалансирован!'])
        elif kod == 0:
            pt.add_row(['Сообщение о результатх расчета УР', 'Расчет УР завершен успешно!'])
        print(pt)
        return kod



