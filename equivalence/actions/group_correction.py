# -*- coding: utf-8 -*-
from equivalence.AstraRastr import RASTR
from equivalence.tables.Tables import Node, Vetv, Generator


class GroupCorr:
    """
    Класс GroupCorr - групповая коррекция
      Данный класс изменяет значения в соотвтетсии с заданной формулой и выборкой.
      Пример вызова класса:
    >> rastr_moduls.GroupCorr(Rastr=<объект RastrWinLib>,
                                table=< название таблицы ("Generator" или "node")>,
                                column=< название параметра (vzd,P,pl_ip ...)>,
                                viborka=< название района или диапазон знчений ("na > 1") >,
                                formula=< pn*1.15 >)
    """

    def __init__(self,
                 table: str,
                 column: str = 'sel',
                 rastr_win: object = RASTR,
                 switch_command_line: bool = False):
        f"""

        :param table:
        :param column:
        :param rastr_win: 
        :param switch_command_line:
        """
        self.rastr_win = rastr_win
        self.table = self.rastr_win.Tables(table)
        self.column = self.table.Cols(column)
        self.switch_command_line = switch_command_line

    def calc(self, key: str, formula):
        """

        :param key:
        :param formula:
        :return:
        """
        self.table.SetSel(key)
        self.column.Calc(formula)
        if self.switch_command_line:
            print(f'Изменение параметра {self.column.name}: выборка {key}; формула: {formula}.')

    def calc_cols(self, key: str, formula, column: str):
        """

        :param key:
        :param formula:
        :param column:
        :return:
        """
        self.table.SetSel(key)
        self.table.Cols(column).Calc(formula)
        if self.switch_command_line:
            print(f'Изменение параметра {self.column.name}: выборка {key}; формула: {formula}.')


class Zeroing:
    """
    Класс обнуления.
    """

    def __init__(self, rastr_win: object = RASTR):
        f"""
        :param rastr_win: 
        """
        self.rastr_win = rastr_win

    def node(self):
        _table = self.rastr_win.Tables(Node.table)
        _table.SetSel("")
        _table.Cols(Node.sel).Calc(0)

    def vetv(self):
        _table = self.rastr_win.Tables(Vetv.table)
        _table.SetSel("")
        _table.Cols(Vetv.sel).Calc(0)

    def generators(self):
        _table = self.rastr_win.Tables(Generator.table)
        _table.SetSel("")
        _table.Cols(Generator.sel).Calc(0)
