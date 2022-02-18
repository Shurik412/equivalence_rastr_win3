# -*- coding: utf-8 -*-
import unittest

from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.actions.zeroing import Zeroing
from equivalence.tables.Tables import Node
from equivalence.test.model_test_RUSTab.path_model import absolute_path_to_file


class TestZeroing(unittest.TestCase):
    def setUp(self) -> None:
        # загружаем тестовую 9-ти узловую схему RastrWin3
        LoadFile(rastr_win=RASTR) \
            .load(
            name_shabl_russian='динамика',
            path_file=rf'{absolute_path_to_file}\model_test_RUSTab\test9.rst')
        self.zeroing_obj = Zeroing(rastr_win=RASTR)

    def test_row(self):
        self.zeroing_obj.node()
        _table = RASTR.Tables(Node.table)
        _table.SetSel("sel=1")
        count_table_node = _table.Count
        self.assertEqual(
            first=count_table_node,
            second=0
        )
