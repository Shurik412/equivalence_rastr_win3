# -*- coding: utf-8 -*-
from equivalence.actions.group_correction import GroupCorr
from equivalence.tables.Generator import Generator
from equivalence.tables.node import Node
from equivalence.tables.vetv import Vetv


class SelectionTick:
    def __init__(self, rastr_win: object, area: int):
        self.rastr_win = rastr_win
        self.area = area

    def vetv_in_area(self, formula=1):
        groupCorr = GroupCorr(rastr_win=self.rastr_win, table=Vetv.table, column=Vetv.sel)
        groupCorr.calc(key=f"iq.na={self.area} & ip.na={self.area}", formula=formula)

    def node_in_area(self, formula=1):
        groupCorr = GroupCorr(rastr_win=self.rastr_win, table=Node.table, column=Node.sel)
        groupCorr.calc(key=f"na={self.area}", formula=formula)

    def generator_in_area(self, formula=1):
        groupCorr = GroupCorr(rastr_win=self.rastr_win, table=Generator.table, column=Generator.sel)
        groupCorr.calc(key=f'Node.na={self.area}', formula=formula)


class SelectionRemoveTick:
    def __init__(self, rastr_win: object):
        self.rastr_win = rastr_win

    def vetv(self, formula=0):
        groupCorr = GroupCorr(rastr_win=self.rastr_win, table=Vetv.table, column=Vetv.sel)
        groupCorr.calc(key=f"", formula=formula)

    def node(self, formula=0):
        groupCorr = GroupCorr(rastr_win=self.rastr_win, table=Node.table, column=Node.sel)
        groupCorr.calc(key=f"", formula=formula)

    def generator(self, formula=0):
        groupCorr = GroupCorr(rastr_win=self.rastr_win, table=Generator.table, column=Generator.sel)
        groupCorr.calc(key=f"", formula=formula)


def sel_vetv(rastr_win: object,
             area: int) -> None:
    """

    :param rastr_win:
    :param area:
    :return:
    """
    group_corr = GroupCorr(rastr_win=rastr_win, table=Vetv.table, column=Vetv.sel, switch_command_line=False)
    group_corr.calc(key=f"iq.na={area} & ip.na={area}", formula=1)


def sel_node(rastr_win: object,
             area: int) -> None:
    group_corr = GroupCorr(rastr_win=rastr_win, table=Node.table, column=Node.sel, switch_command_line=False)
    group_corr.calc(key=f"na={area}", formula=1)
