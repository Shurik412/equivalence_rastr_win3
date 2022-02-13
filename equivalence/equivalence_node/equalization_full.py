# -*- coding: utf-8 -*-
from equivalence.equivalence_node.search_area_by_name import na_of_the_area_by_name
from equivalence.tables.Tables import Node, Vetv, Generator


def equivalent_full_to_nodes(
        rastr_win: object,
        name_area: str,
        uhom: int) -> None:
    """
    #************************************************************
    # Назначение: Эквивалентирование генераторных узлов.
    # Входные
    # параметры:
    # Возврат:    Nothing
    #************************************************************
    """
    na = na_of_the_area_by_name(rastr_win=rastr_win, name_area=name_area)
    vyborka = f"(na={na}) & (uhom < {uhom})"
    print(vyborka)
    table_node = rastr_win.Tables(Node.table)
    table_vetv = rastr_win.Tables(Vetv.table)
    table_generator = rastr_win.Tables(Generator.table)

    table_node.SetSel(vyborka)
    table_node.Cols(Node.sel).Calc(1)
    print(f"table_node.Count={table_node.Count}")
    j = table_node.FindNextSel(-1)
    while j != (-1):
        # print(f'j={j}')
        ny = table_node.Cols(Node.ny).Z(j)
        tip_node = table_node.Cols(Node.tip).Z(j)
        uhom_node = table_node.Cols(Node.uhom).Z(j)
        if tip_node > 1:  # все генераторные узла
            table_generator.SetSel(f"Node.ny={ny}")
            j_gen = table_generator.FindNextSel(-1)
            if j_gen != (-1):
                table_vetv.SetSel(f"(ip={ny})|(iq={ny})")
                j_vetv = table_vetv.FindNextSel(-1)
                while j_vetv != (-1):
                    tip_vetv = table_vetv.Cols(Vetv.tip).Z(j_vetv)
                    if tip_vetv == 1:
                        v_ip = table_vetv.Cols(Vetv.v_ip).Z(j_vetv)
                        v_iq = table_vetv.Cols(Vetv.v_iq).Z(j_vetv)
                        if (v_ip > 170 and v_iq < 250) or (v_ip < 170 and v_iq > 250):
                            table_node.Cols(Node.sel).SetZ(j, 0)
                    j_vetv = table_vetv.FindNextSel(j_vetv)
        else:
            table_vetv.SetSel(f"(ip={ny})|(iq={ny})")
            j_vetv_2 = table_vetv.FindNextSel(-1)
            while j_vetv_2 != (-1):
                tip_vetv_2 = table_vetv.Cols(Vetv.tip).Z(j_vetv_2)
                if tip_vetv_2 == 1:
                    v_ip_2 = table_vetv.Cols(Vetv.v_ip).Z(j_vetv_2)
                    v_iq_2 = table_vetv.Cols(Vetv.v_iq).Z(j_vetv_2)
                    if (v_ip_2 > 170 and v_iq_2 < 250) or (v_ip_2 < 170 and v_iq_2 > 250):
                        table_node.Cols(Node.sel).SetZ(j, 0)
                j_vetv_2 = table_vetv.FindNextSel(j_vetv_2)
        table_node.SetSel(vyborka)
        j = table_node.FindNextSel(j)

    print(f" -> Завершено выделение района(-ов): {vyborka}")
