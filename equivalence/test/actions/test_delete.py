# -*- coding: utf-8 -*-
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.AstraRastr import RASTR
from equivalence.actions.group_correction import GroupCorr
from equivalence.test.model_test_RUSTab.path_model import absolute_path_to_file
from equivalence.tables.node import Node
from equivalence.tables.Generator import Generator
from equivalence.calculation.equivalent import Equivalent
from equivalence.settings.equivalence import set_com_ekviv

# -*- coding: utf-8 -*-
import unittest

from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.actions.delete import Delete
from equivalence.tables.Tables import Node
from equivalence.test.model_test_RUSTab.path_model import absolute_path_to_file


class TestDelete(unittest.TestCase):
    def setUp(self) -> None:
        # загружаем тестовую 9-ти узловую схему RastrWin3
        LoadFile(rastr_win=RASTR) \
            .load(
            name_shabl_russian='динамика',
            path_file=rf'{absolute_path_to_file}\model_test_RUSTab\test9.rst')
        self.delete_obj = Delete(rastr_win=RASTR, table=Node.table)

    def test_row(self):
        self.delete_obj.row(id=1)
        _table = RASTR.Tables(Node.table)
        _table.SetSel("")
        count_table_node = _table.Count
        self.assertEqual(
            first=count_table_node,
            second=8
        )
        self.delete_obj.rows()
        count_table_node = _table.Count
        self.assertEqual(
            first=0,
            second=count_table_node
        )
