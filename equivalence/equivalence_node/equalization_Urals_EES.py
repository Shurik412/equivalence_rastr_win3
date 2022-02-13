# -*- coding: utf-8 -*-
from equivalence.tables.Tables import Vetv, Node, Generator


def equalization_of_the_Urals_energy_system(
        selection_of_the_area: str,
        rastr_win: object) -> None:
    """
    # ************************************************************
    # Назначение: Эквиваленитрование ОЭС Урала
    # Входные параметры: selection_of_the_area - выборка районов ОЭС Урала
    # Возврат:    Nothing
    # ************************************************************
    """
    table_node = rastr_win.Tables(Node.table)
    table_vetv = rastr_win.Tables(Vetv.table)
    table_generator = rastr_win.Tables(Generator.table)

    table_node.SetSel(selection_of_the_area)
    table_node.Cols(Node.sel).Calc(1)
    j = table_node.FindNextSel(-1)
    while j != (-1):
        ny_node = table_node.Cols(Node.ny).Z(j)
        tip_node = table_node.Cols(Node.tip).Z(j)
        # uhom_node = tip_node.Cols(Node.uhom).Z(j)
        if tip_node > 1:
            table_generator.SetSel(f"Node.ny={ny_node}")
            j_gen = table_generator.FindNextSel(-1)
            if j_gen != (-1):
                table_vetv.SetSel(f"(ip={ny_node})|(iq={ny_node})")
                j_vetv = table_vetv.FindNextSel(-1)
                while j_vetv != (-1):
                    tip_vetv = table_vetv.Cols(Vetv.tip).Z(j_vetv)
                    if tip_vetv == 1:
                        v_ip = tip_vetv.Cols(Vetv.v_ip).Z(j_vetv)
                        v_iq = tip_vetv.Cols(Vetv.v_iq).Z(j_vetv)

                        if (v_ip > 430 and v_iq < 580) or (v_ip < 430 and v_iq > 580):
                            table_node.Cols(Node.sel).SetZ(j, 0)

                    j_vetv = table_vetv.FindNextSel(j_vetv)
        else:
            table_vetv.SetSel(f"(ip={ny_node})|(iq={ny_node})")
            j_vetv_2 = table_vetv.FindNextSel(-1)
            while j_vetv_2 != (-1):
                tip_vetv_2 = table_vetv.Cols(Vetv.tip).Z(j_vetv_2)
                if tip_vetv_2 == 1:
                    v_ip_2 = table_vetv.Cols(Vetv.table).Z(j_vetv_2)
                    v_iq_2 = table_vetv.Cols(Vetv.table).Z(j_vetv_2)
                    if (v_ip_2 > 430 and v_iq_2 < 580) or (v_ip_2 < 430 and v_iq_2 > 580):
                        table_node.Cols(Node.sel).SetZ(j, 0)
                j_vetv_2 = table_vetv.FindNextSel(j_vetv_2)
        table_node.SetSel(selection_of_the_area)
        j = table_node.FindNextSel(j)
    print(" -> Завершено выделение района(-ов): " & selection_of_the_area)
