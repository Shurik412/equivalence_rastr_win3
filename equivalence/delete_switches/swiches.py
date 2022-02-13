# -*- coding: utf-8 -*-
from equivalence.actions.add_cols_in_tables import add_cols
from equivalence.actions.get import GettingParameter
from equivalence.actions.group_correction import GroupCorr
from equivalence.actions.selection import SelectionRemoveTick
from equivalence.actions.variable import Variable
from equivalence.calculation.regime import Regime
from equivalence.tables.Tables import Node, Vetv, Generator, Area


# area: str = "(na<500 | na>600) & na!=8082 & na!=8037 & na!=5329 & na!=5230"
def del_swiches(rastr_win: object, area: str = "na=516") -> None:
    """
    dle_swiches - функция F01 - в тестах
    :param rastr_win:
    :param area:
    :return:
    """
    group_corr_vetv = GroupCorr(rastr_win=rastr_win, table=Vetv.table, column=Vetv.groupid)
    group_corr_node = GroupCorr(rastr_win=rastr_win, table=Node.table, column=Node.sel)
    group_corr_area = GroupCorr(rastr_win=rastr_win, table=Area.table)
    rgm_obj = Regime(rastr_win=rastr_win)
    selection_remove_tick = SelectionRemoveTick(rastr_win=rastr_win)
    gen_table = rastr_win.Tables(Generator.table)
    vetv_table = rastr_win.Tables(Vetv.table)
    node_table = rastr_win.Tables(Node.table)
    ti_table = rastr_win.Tables("ti")

    rgm_obj.rgm()

    # добавляем столбцы в таблицы
    add_cols(rastr_win=rastr_win, table=Node.table, name_new_cols="sel_new")
    add_cols(rastr_win=rastr_win, table=Node.table, name_new_cols="vras_new")
    add_cols(rastr_win=rastr_win, table=Node.table, name_new_cols="qmin_new")
    add_cols(rastr_win=rastr_win, table=Node.table, name_new_cols="qmax_new")
    add_cols(rastr_win=rastr_win, table=Vetv.table, name_new_cols="sel_new2")
    add_cols(rastr_win=rastr_win, table=Area.table, name_new_cols="pop_new")
    add_cols(rastr_win=rastr_win, table=Area.table, name_new_cols="poq_new")
    add_cols(rastr_win=rastr_win, table=Vetv.table, name_new_cols="ip_new")
    add_cols(rastr_win=rastr_win, table=Vetv.table, name_new_cols="iq_new")
    add_cols(rastr_win=rastr_win, table=Vetv.table, name_new_cols="np_new")

    group_corr_area.calc_cols(key="", column="pop_new", formula=Area.pop)
    group_corr_area.calc_cols(key="", column="poq_new", formula=Area.poq)
    group_corr_vetv.calc_cols(key="", column="sel_new2", formula=Vetv.sel)

    selection_remove_tick.vetv(formula=0)
    selection_remove_tick.node(formula=0)

    group_corr_node.calc_cols(key="", column="sel_new", formula=0)
    group_corr_node.calc_cols(key="", column="sel_new", formula=Node.sel)

    group_corr_node.calc_cols(key="", column="vras_new", formula=0)
    group_corr_node.calc_cols(key="", column="vras_new", formula=Node.vras)

    group_corr_vetv.calc_cols(key="", column="ip_new", formula="ip")
    group_corr_vetv.calc_cols(key="", column="iq_new", formula="iq")
    group_corr_vetv.calc_cols(key="", column="np_new", formula="np")

    group_corr_node.calc_cols(key="", column="sel", formula=1)
    group_corr_node.calc_cols(key="", column="sel_new", formula="sel")

    group_corr_node.calc_cols(column=Node.sel, key=area, formula=1)
    group_corr_node.calc_cols(column=Node.sel, key=area, formula=Node.sel)

    # убирает sel-узла если на ВЛ с одной стороны выделен узел
    vetvyklvybexc = "(iq.bsh!=0 & ip.bsh=0)|(ip.bsh!=0 & iq.bsh=0)|(ip.sel=0|iq.sel=0)|(ip.tip=0|iq.tip=0)"
    group_corr_vetv.calc_cols(column=Vetv.groupid, key=vetvyklvybexc, formula=1)

    for povet in range(0, 10000):
        # ivet = set_sel(rastr_win=rastr_win, table=Vetv.table, key="tip=2 & !sta & groupid != 1")
        vetv_table.SetSel(
            "tip=2 & !sta & groupid != 1")  # Выборка ветвей, которые считаем выключателями и которые не откл.
        ivet = vetv_table.FindNextSel(-1)
        if ivet == (-1):
            print(f"povet={povet} - break")
            break
        ip = vetv_table.Cols(Vetv.ip).Z(ivet)
        iq = vetv_table.Cols(Vetv.iq).Z(ivet)
        if ip > iq:
            ny = iq
            ndel = ip
        else:
            ny = ip
            ndel = iq
        node_table.SetSel(f"ny={ny}")
        iny = node_table.FindNextSel(-1)
        node_table.SetSel(f"ny={ndel}")
        idel = node_table.FindNextSel(-1)
        pgdel = node_table.Cols(Node.pg).Z(idel)
        qgdel = node_table.Cols(Node.qg).Z(idel)
        pndel = node_table.Cols(Node.pn).Z(idel)
        qndel = node_table.Cols(Node.qn).Z(idel)
        bshdel = node_table.Cols(Node.bsh).Z(idel)
        gshdel = node_table.Cols(Node.qsh).Z(idel)
        qnmax2 = node_table.Cols(Node.qn_max).Z(idel)
        qnmin2 = node_table.Cols(Node.qn_min).Z(idel)
        pnmax2 = node_table.Cols(Node.pn_max).Z(idel)
        pnmin2 = node_table.Cols(Node.pn_min).Z(idel)
        exist_load2 = node_table.Cols(Node.exist_load).Z(idel)
        v2 = node_table.Cols(Node.vzd).Z(idel)
        pgny = node_table.Cols(Node.pg).Z(iny)
        qgny = node_table.Cols(Node.qg).Z(iny)
        pnny = node_table.Cols(Node.pn).Z(iny)
        qnny = node_table.Cols(Node.qn).Z(iny)
        bshny = node_table.Cols(Node.bsh).Z(iny)
        gshny = node_table.Cols(Node.gsh).Z(iny)
        qnmax1 = node_table.Cols(Node.qn_max).Z(iny)
        qnmin1 = node_table.Cols(Node.qn_min).Z(iny)
        qmax1 = node_table.Cols(Node.qn_max).Z(iny)
        qmax2 = node_table.Cols(Node.qn_max).Z(idel)
        pnmax1 = node_table.Cols(Node.pn_max).Z(iny)
        pnmin1 = node_table.Cols(Node.pn_min).Z(iny)
        exist_load1 = node_table.Cols(Node.exist_load).Z(iny)
        v1 = node_table.Cols(Node.vzd).Z(iny)

        node_table.Cols(Node.pg).SetZ(iny, pgdel + pgny)
        node_table.Cols(Node.qg).SetZ(iny, qgdel + qgny)

        node_table.Cols(Node.pn).SetZ(iny, pndel + pnny)
        node_table.Cols(Node.qn).SetZ(iny, qndel + qnny)

        node_table.Cols(Node.bsh).SetZ(iny, bshdel + bshny)
        node_table.Cols(Node.gsh).SetZ(iny, gshdel + gshny)

        node_table.Cols(Node.pn_max).SetZ(iny, pnmax1 + pnmax2)
        node_table.Cols(Node.qn_max).SetZ(iny, qnmax1 + qnmax2)

        if qnmin1 < qnmin2:
            node_table.Cols(Node.qn_min).SetZ(iny, qnmin1)
        else:
            node_table.Cols(Node.qn_min).SetZ(iny, qnmin2)

        if pnmin1 < pnmin2:
            node_table.Cols(Node.pn_min).SetZ(iny, pnmin1)
        else:
            node_table.Cols(Node.pn_min).SetZ(iny, pnmin2)

        if exist_load1 > 0 or exist_load2 > 0:
            node_table.Cols(Node.exist_load).SetZ(iny, 1)

        gen_table.SetSel(f"Node={ndel}")
        igen = gen_table.FindNextSel(-1)
        if igen != (-1):
            while igen != (-1):
                gen_table.Cols(Generator.Node).SetZ(igen, ny)
                igen = gen_table.FindNextSel(igen)

        if v1 != v2 and v1 > 0.3 and v2 > 0.3 and (qmax1 + qmax2) != 0:
            node_table.Cols(Node.vzd).SetZ(iny, (v1 * qmax1 + v2 * qmax2) / (qmax1 + qmax2))

        if v1 == 0 and v2 != 0:
            node_table.Cols(Node.vzd).SetZ(iny, v2)

        if v1 != 0 and v2 != 0:
            qmin_iny_ = node_table.Cols(Node.qmin).Z(idel)
            _qmin_idel = node_table.Cols(Node.qmin).Z(idel)

            node_table.Cols(Node.qmin).SetZ(iny, qmin_iny_ + _qmin_idel)
            node_table.Cols(Node.qmax).SetZ(iny, qmax1 + qmax2)

        if v1 == 0 and v2 != 0:
            qmin_idel_ = node_table.Cols(Node.qmin).Z(idel)
            _qmax_idel = node_table.Cols(Node.qmax).Z(idel)

            node_table.Cols(Node.qmin).SetZ(iny, qmin_idel_)
            node_table.Cols(Node.qmax).SetZ(iny, _qmax_idel)

        vetv_table.SetSel(f"(ip={ip} & iq={iq})|(iq={ip} & ip={iq})")
        vetv_table.DelRowS()  # Удаляем ветвь

        vetv_table.SetSel(f"iq={ndel}")
        vetv_table.Cols(Vetv.iq).Calc(ny)

        vetv_table.SetSel(f"ip={ndel}")
        vetv_table.Cols(Vetv.ip).Calc(ny)

        ti_table.SetSel(
            f"(prv_num=20|prv_num=7|prv_num=6|prv_num=5|prv_num=4|prv_num=3|prv_num=2|prv_num=1)&id1={ndel}")
        ti_table.Cols("id1").Calc(ny)

        node_table.DelRowS()  # Удаляем узел

    kod = rgm_obj.rgm()
    if kod != 0:
        print("Regim do not exist")

    node_table.SetSel("")
    node_table.Cols(Node.sel).Calc("0")

    vetv_table.SetSel("")
    vetv_table.Cols(Vetv.sel).Calc("0")


def del_switches_gen(rastr_win: object) -> None:
    """

    :param rastr_win:
    :return:
    """
    selection_remove_tick = SelectionRemoveTick(rastr_win=rastr_win)
    gen_table = rastr_win.Tables(Generator.table)
    vetv_table = rastr_win.Tables(Vetv.table)
    node_table = rastr_win.Tables(Node.table)
    ti_table = rastr_win.Tables("ti")

    selection_remove_tick.node(formula=0)
    selection_remove_tick.vetv(formula=0)

    node_table.SetSel("")
    k1 = node_table.FindNextSel(-1)
    while k1 != (-1):
        ny1 = node_table.Cols(Node.ny).Z(k1)
        vetv_table.SetSel(f"(ip={ny1})|(iq={ny1})")
        vetv_count = vetv_table.Count
        if vetv_count == 1:
            vetv_table.SetSel(f"x<1 & (tip=0|tip=2)&((ip={ny1})|(iq={ny1}))")
            vetv_count2 = vetv_table.Count
            if vetv_count2 == 1:
                vetv_table.SetSel(f"(x<1 & (tip=0|tip=2) & ((ip={ny1})|(iq={ny1})))")
                k3 = vetv_table.FindNextSel(-1)
                if k3 != (-1):
                    ip_k3 = vetv_table.Cols(Vetv.ip).Z(k3)
                    if ip_k3 == ny1:
                        ny2 = vetv_table.Cols(Vetv.iq).Z(k3)
                    else:
                        ny2 = vetv_table.Cols(Vetv.ip).Z(k3)
                    gen_table.SetSel(f"Node={ny1}")
                    k2 = gen_table.FindNextSel(-1)
                    if k2 != (-1):
                        node_table.SetSel(f"ny={ny2}")
                        k4 = node_table.FindNextSel(-1)
                        if k4 != (-1):
                            pn_k1 = node_table.Cols(Node.pn).Z(k1)
                            pn_k4 = node_table.Cols(Node.pn).Z(k4)

                            qn_k1 = node_table.Cols(Node.qn).Z(k1)
                            qn_k4 = node_table.Cols(Node.qn).Z(k4)
                            vzd_k1 = node_table.Cols(Node.vzd).Z(k1)

                            node_table.Cols(Node.pn).SetZ(k4, pn_k1 + pn_k4)
                            node_table.Cols(Node.qn).SetZ(k4, qn_k1 + qn_k4)
                            node_table.Cols(Node.vzd).SetZ(k4, vzd_k1)

                            exist_load_k1 = node_table.Cols(Node.exist_load).Z(k1)
                            node_table.Cols(Node.exist_load).SetZ(k4, exist_load_k1)

                            exist_gen_k1 = node_table.Cols(Node.exist_gen).Z(k1)
                            node_table.Cols(Node.exist_gen).SetZ(k4, exist_gen_k1)

                            pn_max_k1 = node_table.Cols(Node.pn_max).Z(k1)
                            pn_max_k4 = node_table.Cols(Node.pn_max).Z(k4)
                            node_table.Cols(Node.pn_max).SetZ(k4, pn_max_k1 + pn_max_k4)

                            pn_min_k4 = node_table.Cols(Node.pn_min).Z(k4)
                            pn_min_k1 = node_table.Cols(Node.pn_min).Z(k1)
                            if pn_min_k4 >= pn_min_k1:
                                node_table.Cols(Node.pn_min).SetZ(k4, pn_min_k1)

                            pg_max_k1 = node_table.Cols(Node.pg_max).Z(k1)
                            pg_max_k4 = node_table.Cols(Node.pg_max).Z(k4)
                            node_table.Cols(Node.pg_max).SetZ(k4, pg_max_k1 + pg_max_k4)

                            pg_min_k4 = node_table.Cols(Node.pg_min).Z(k4)
                            pg_min_k1 = node_table.Cols(Node.pg_min).Z(k1)
                            if pg_min_k4 >= pg_min_k1:
                                node_table.Cols(Node.pg_min).SetZ(k4, pg_min_k1)

                            node_table.Cols(Node.sel).SetZ(k1, 1)
                            vetv_table.Cols(Vetv.sel).SetZ(k3, 1)
                            # ti_table.SetSel(
                            #     f"(prv_num=20|prv_num=7|prv_num=6|prv_num=5|prv_num=4|prv_num=3|prv_num=2|prv_num=1)&id1={ny1}")
                            # ti_table.Cols("id1").Calc(ny2)
                            gen_table.SetSel(f"Node={ny1}")
                            k2 = gen_table.FindNextSel(-1)
                            while k2 != (-1):
                                gen_table.Cols(Generator.Node).SetZ(k2, ny2)
                                k2 = gen_table.FindNextSel(k2)
        node_table.SetSel("")
        k1 = node_table.FindNextSel(k1)

    vetv_table.SetSel("sel=1")
    vetv_table.DelRowS()

    node_table.SetSel("sel=1")
    node_table.DelRowS()

    selection_remove_tick.node(formula=0)
    selection_remove_tick.vetv(formula=0)


def delete_UKR(rastr_win: object):
    """

    :param rastr_win:
    :return:
    """

    selection_remove_tick = SelectionRemoveTick(rastr_win=rastr_win)
    vetv_table = rastr_win.Tables(Vetv.table)
    node_table = rastr_win.Tables(Node.table)

    selection_remove_tick.node(formula=0)
    selection_remove_tick.vetv(formula=0)

    vetv_table.SetSel("(iq.na>800 & ip.na>300 & ip.na<400)")
    k = vetv_table.FindNextSel(-1)
    while k != (-1):
        iq1 = vetv_table.Cols(Vetv.iq).Z(k)
        node_table.SetSel(f"ny={iq1}")
        k2 = node_table.FindNextSel(-1)
        if k2 != (-1):
            node_table.Cols(Node.sel).SetZ(k2, 1)
        k = vetv_table.FindNextSel(k)

    vetv_table.SetSel("(ip.na>800 & iq.na>300 & iq.na<400)")
    k = vetv_table.FindNextSel(-1)
    while k != (-1):
        ip1 = vetv_table.Cols(Vetv.ip).Z(k)
        node_table.SetSel(f"ny={ip1}")
        k2 = node_table.FindNextSel(-1)
        if k2 != (-1):
            node_table.Cols(Node.sel).SetZ(k2, 1)
        k = vetv_table.FindNextSel(k)

    vetv_table.SetSel("((iq.sel=1 &ip.sel=0)|(ip.sel=1 &iq.sel=0)) & ip.na>800 & iq.na>800 &!sta")
    k = vetv_table.FindNextSel(-1)
    while k != (-1):
        iq1 = vetv_table.Cols(Vetv.iq).Z(k)
        node_table.SetSel(f"ny={iq1}")
        k2 = node_table.FindNextSel(-1)
        if k2 != (-1):
            node_table.Cols(Node.sel).SetZ(k2, 1)

        ip1 = vetv_table.Cols(Vetv.ip).Z(k)
        node_table.SetSel(f"ny={ip1}")
        k2 = node_table.FindNextSel(-1)
        if k2 != (-1):
            node_table.Cols(Node.sel).SetZ(k2, 1)
        vetv_table.SetSel("((iq.sel=1 &ip.sel=0) | (ip.sel=1 &iq.sel=0)) & ip.na>800 & iq.na>800 &!sta")
        k = vetv_table.FindNextSel(k)

    node_table.SetSel("sel=1")
    node_table.DelRowS()

    vetv_table.SetSel("sel=1")
    vetv_table.DelRowS()


def delete_area(rastr_win: object) -> None:
    """

    :param rastr_win:
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)
    group_corr_vetv = GroupCorr(rastr_win=rastr_win, table=Vetv.table, column=Vetv.groupid)
    group_corr_node = GroupCorr(rastr_win=rastr_win, table=Node.table, column=Node.sel)
    get_ = GettingParameter(rastr_win=rastr_win)
    rgm_obj = Regime(rastr_win=rastr_win)
    gen_table = rastr_win.Tables(Generator.table)
    vetv_table = rastr_win.Tables(Vetv.table)
    node_table = rastr_win.Tables(Node.table)
    pqd = rastr_win.Tables("graphik2")
    polin_table = rastr_win.Tables("polin")
    darea_table = rastr_win.Tables("darea")
    area_table = rastr_win.Tables("area")
    area2_table = rastr_win.Tables("area2")

    add_cols(rastr_win=rastr_win, table=Vetv.table, name_new_cols="pl_iq_new")
    add_cols(rastr_win=rastr_win, table=Vetv.table, name_new_cols="pl_ip_new")
    add_cols(rastr_win=rastr_win, table=Vetv.table, name_new_cols="ql_iq_new")
    add_cols(rastr_win=rastr_win, table=Vetv.table, name_new_cols="ql_ip_new")
    add_cols(rastr_win=rastr_win, table=Vetv.table, name_new_cols="gran")
    add_cols(rastr_win=rastr_win, table=Node.table, name_new_cols="muskod_new")
    add_cols(rastr_win=rastr_win, table=Node.table, name_new_cols="vras_new")

    group_corr_vetv.calc_cols(column="pl_iq_new", key="", formula="pl_iq")
    group_corr_vetv.calc_cols(column="pl_ip_new", key="", formula="pl_ip")
    group_corr_vetv.calc_cols(column="ql_iq_new", key="", formula="ql_iq")
    group_corr_vetv.calc_cols(column="ql_ip_new", key="", formula="ql_ip")
    group_corr_node.calc_cols(column="vras_new", key="", formula="vras")

    vetv_table.SetSel("ip.sel=1 & iq.sel=0")
    k = vetv_table.FindNextSel(-1)
    while k != (-1):
        ip1 = vetv_table.Cols(Vetv.ip).Z(k)
        pn11 = vetv_table.Cols("pl_ip_new").Z(k)
        qn11 = vetv_table.Cols("ql_ip_new").Z(k)
        vetv_table.Cols(Vetv.br_ip).SetZ(k, 0)
        vetv_table.Cols("gran").SetZ(k, 1)
        node_table.SetSel(f"ny={ip1}")
        k2 = node_table.FindNextSel(-1)
        if k2 != (-1):
            muskod_new_ = get_.get_cell_row(table=Node.table, column="muskod_new", row=k2)
            if muskod_new_ == 0:
                variable_.make_changes_row(table=Node.table, column=Node.pn, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.qn, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.pg, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.qg, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.nrk, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.brk, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.qsh, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.bshr, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.bsh, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.vras, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column="muskod_new", row=k2, value=1)

                vras_new_ = get_.get_cell_row(table=Node.table, column="vras_new", row=k2)
                variable_.make_changes_row(table=Node.table, column=Node.vzd, row=k2, value=vras_new_)
                variable_.make_changes_row(table=Node.table, column=Node.qmin, row=k2, value=-9999.0)
                variable_.make_changes_row(table=Node.table, column=Node.qmax, row=k2, value=9999.0)
                variable_.make_changes_row(table=Node.table, column=Node.pg_min, row=k2, value=-9999.0)
                variable_.make_changes_row(table=Node.table, column=Node.pg_max, row=k2, value=9999.0)
                variable_.make_changes_row(table=Node.table, column=Node.pn_min, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.pn_max, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.qn_min, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.qn_max, row=k2, value=0)

                variable_.make_changes_row(table=Node.table, column=Node.exist_gen, row=k2, value=1)
                variable_.make_changes_row(table=Node.table, column=Node.exist_load, row=k2, value=0)

                uhom_ = get_.get_cell_row(table=Node.table, column=Node.uhom, row=k2)
                if uhom_ == 110:
                    variable_.make_changes_row(table=Node.table, column=Node.qmin, row=k2, value=-300.)
                    variable_.make_changes_row(table=Node.table, column=Node.qmax, row=k2, value=300.)
                    variable_.make_changes_row(table=Node.table, column=Node.pg_min, row=k2, value=-300.)
                    variable_.make_changes_row(table=Node.table, column=Node.pg_max, row=k2, value=300.)

            pg_k2 = get_.get_cell_row(table=Node.table, column=Node.pg, row=k2)
            qg_k2 = get_.get_cell_row(table=Node.table, column=Node.qg, row=k2)

            variable_.make_changes_row(table=Node.table, column=Node.pg, row=k2,
                                       value=pg_k2 - pn11)
            variable_.make_changes_row(table=Node.table, column=Node.qg, row=k2,
                                       value=qg_k2 - qn11)
        k = vetv_table.FindNextSel(k)

    vetv_table.SetSel("iq.sel=1 & ip.sel=0")
    k = vetv_table.FindNextSel(-1)
    while k != (-1):
        iq1 = get_.get_cell_row(table=Vetv.table, column=Vetv.iq, row=k)
        pn11 = get_.get_cell_row(table=Vetv.table, column="pl_iq_new", row=k)
        qn11 = get_.get_cell_row(table=Vetv.table, column="ql_iq_new", row=k)
        variable_.make_changes_row(table=Vetv.table, column=Vetv.br_ip, row=k, value=0)
        variable_.make_changes_row(table=Vetv.table, column="gran", row=k, value=1)
        node_table.SetSel(f"ny={iq1}")
        k2 = node_table.FindNextSel(-1)
        if k2 != (-1):
            muskod_new_ = get_.get_cell_row(table=Node.table, column="muskod_new", row=k2)
            if muskod_new_ == 0:
                variable_.make_changes_row(table=Node.table, column=Node.pn, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.qn, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.pg, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.qg, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.nrk, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.brk, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.qsh, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.bshr, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.bsh, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.vras, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column="muskod_new", row=k2, value=1)
                vras_new_ = get_.get_cell_row(table=Node.table, column="vras_new", row=k2)
                variable_.make_changes_row(table=Node.table, column=Node.vzd, row=k2, value=vras_new_)
                variable_.make_changes_row(table=Node.table, column=Node.qmin, row=k2, value=-9999.)
                variable_.make_changes_row(table=Node.table, column=Node.qmax, row=k2, value=9999.)
                variable_.make_changes_row(table=Node.table, column=Node.pg_min, row=k2, value=-9999.)
                variable_.make_changes_row(table=Node.table, column=Node.pg_max, row=k2, value=9999.)
                variable_.make_changes_row(table=Node.table, column=Node.pn_min, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.pn_max, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.qn_min, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.qn_max, row=k2, value=0)
                variable_.make_changes_row(table=Node.table, column=Node.exist_gen, row=k2, value=1)
                variable_.make_changes_row(table=Node.table, column=Node.exist_load, row=k2, value=0)

                uhom_k2 = get_.get_cell_row(table=Node.table, column=Node.uhom, row=k2)
                if uhom_k2 == 110:
                    variable_.make_changes_row(table=Node.table, column=Node.qmin, row=k2, value=-300)
                    variable_.make_changes_row(table=Node.table, column=Node.qmax, row=k2, value=300)
                    variable_.make_changes_row(table=Node.table, column=Node.pg_min, row=k2, value=-300)
                    variable_.make_changes_row(table=Node.table, column=Node.pg_max, row=k2, value=300)

            variable_.make_changes_row(table=Node.table, column=Node.pg, row=k2,
                                       value=(get_.get_cell_row(table=Node.table,
                                                                column=Node.pg,
                                                                row=k2) + pn11))

            variable_.make_changes_row(table=Node.table, column=Node.qg, row=k2,
                                       value=(get_.get_cell_row(table=Node.table,
                                                                column=Node.qg,
                                                                row=k2) + qn11))
        k = vetv_table.FindNextSel(k)

    vetv_table.SetSel("iq.sel=1 & ip.sel=1")
    vetv_table.Cols(Vetv.sel).Calc(1)
    vetv_table.SetSel("sel=1")
    vetv_table.DelRowS()
    rgm_obj.rgm()
    delUzlotkl = 1
    if delUzlotkl == 1:
        vetv_table.SetSel("1")
        vetv_table.Cols(Vetv.sel).Calc(0)
        node_table.SetSel("1")
        node_table.Cols(Node.sel).Calc(0)
        node_table.SetSel("1")
        inode = node_table.FindNextSel(-1)

        while inode != (-1):
            ny = get_.get_cell_row(table=Node.table,
                                   column=Node.ny,
                                   row=inode)
            vetv_table.SetSel(f"{ny} =ip|iq={ny}")
            vtv = vetv_table.FindNextSel(-1)
            if vtv > (-1):
                pass
            else:
                variable_.make_changes_row(table=Vetv.table,
                                           column=Vetv.sel,
                                           row=inode,
                                           value=1)
            inode = node_table.FindNextSel(inode)
        node_table.SetSel("sel=1")
        node_table.DelRowS()

    node_table.SetSel("muskod_new=1")
    node_table.Cols("muskod_new").Calc(0)

    gen_table.SetSel("Node.ny=0")
    gen_table.DelRowS()

    gen_table.SetSel("Node.na=0")
    k = gen_table.FindNextSel(-1)
    while k != (-1):
        pq22 = get_.get_cell_row(table=Generator.table,
                                 column=Generator.NumPQ,
                                 row=k)
        pqd.SetSel(f"Num={pq22}")
        pqd.DelRowS()
        k = gen_table.FindNextSel(k)

    gen_table.SetSel(f"Node.na=0")
    gen_table.DelRowS()

    graphikIT = rastr_win.Tables("graphikIT")
    graphikIT.SetSel("")
    k = graphikIT.FindNextSel(-1)
    while k != (-1):
        nzav = graphikIT.Cols("Num").Z(k)
        vetv_table.SetSel(f"n_it={nzav}")
        k2 = vetv_table.FindNextSel(-1)
        if k2 != (-1):
            pass
        else:
            variable_.make_changes_row(table="graphikIT",
                                       column="Num",
                                       row=k,
                                       value=0)
        k = graphikIT.FindNextSel(k)

    graphikIT.SetSel("Num=0")
    graphikIT.DelRowS()
    area_table.SetSel("")
    k = area_table.FindNextSel(-1)
    while k != (-1):
        na1 = area_table.Cols("na").Z(k)
        node_table.SetSel(f"na={na1}")
        k2 = node_table.FindNextSel(-1)
        if k2 != (-1):
            pass
        else:
            variable_.make_changes_row(table=Area.table,
                                       column=Area.na,
                                       row=k,
                                       value=0)
        k = area_table.FindNextSel(k)

    area_table.SetSel("na=0")
    area_table.DelRowS()
    area2_table.SetSel("")
    k = area2_table.FindNextSel(-1)
    while k != (-1):
        na1 = darea_table.Cols("no").Z(k)
        area_table.SetSel(f"no={na1}")
        k2 = area_table.FindNextSel(-1)
        if k2 != (-1):
            pass
        else:
            variable_.make_changes_row(table="darea",
                                       column="no",
                                       row=k,
                                       value=0)
        k = darea_table.FindNextSel(k)

    area2_table.SetSel("npa=0")
    area2_table.DelRowS()
    darea_table.SetSel("")
    k = darea_table.FindNextSel(-1)
    while k != (-1):
        na1 = darea_table.Cols("no").Z(k)
        area_table.SetSel(f"no={na1}")
        k2 = area_table.FindNextSel(-1)
        if k2 != (-1):
            pass
        else:
            darea_table.Cols("no").SetZ(k, 0)
        k = darea_table.FindNextSel(k)

    darea_table.SetSel("nsx=0")
    darea_table.DelRowS()

    polin_table.SetSel("")
    k = polin_table.FindNextSel(-1)
    while k != (-1):
        nsx1 = polin_table.Cols("nsx").Z(k)
        node_table.SetSel(f"nsx={nsx1}")
        k2 = node_table.FindNextSel(-1)
        if k2 != (-1):
            pass
        else:
            polin_table.Cols("nsx").SetZ(k, 0)
        k = polin_table.FindNextSel(k)

    polin_table.SetSel("nsx=0")
    polin_table.DelRowS()
    rgm_obj.rgm()


def vzd_node(rastr_win: object):
    """

    :param rastr_win:
    :return:
    """
    table_node = rastr_win.Tables(Node.table)
    count_node = table_node.Count - 1
    for i in range(0, count_node):
        q_min = table_node.Cols(Node.qmin).Z(i)
        q_max = table_node.Cols(Node.qmax).Z(i)
        uhom = table_node.Cols(Node.uhom).Z(i)
        if q_min == -9999.0 and q_max == 9999.0:
            table_node.Cols(Node.vzd).SetZ(i, uhom)
