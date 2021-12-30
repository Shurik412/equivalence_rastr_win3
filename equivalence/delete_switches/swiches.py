# -*- coding: utf-8 -*-
from equivalence.actions.add_cols_in_tables import add_cols
from equivalence.actions.get import GettingParameter
from equivalence.actions.group_correction import GroupCorr
from equivalence.actions.selection import SelectionRemoveTick
from equivalence.actions.selection import set_sel
from equivalence.actions.variable import Variable
from equivalence.calculation.regime import Regime
from equivalence.tables.Generator import Generator
from equivalence.tables.area import Area
from equivalence.tables.node import Node
from equivalence.tables.vetv import Vetv
from equivalence.actions.variable import FindNextSelection


def del_swiches(rastr_win: object,
                area: str = "(na<500 | na>600) & na!=8082") -> None:
    """

    :param rastr_win:
    :param area:
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)
    group_corr_vetv = GroupCorr(rastr_win=rastr_win, table=Vetv.table, column=Vetv.groupid)
    group_corr_node = GroupCorr(rastr_win=rastr_win, table=Node.table, column=Node.sel)
    group_corr_area = GroupCorr(rastr_win=rastr_win, table=Area.table)
    get_ = GettingParameter(rastr_win=rastr_win)
    rgm_obj = Regime(rastr_win=rastr_win)
    selection_remove_tick = SelectionRemoveTick(rastr_win=rastr_win)
    gen_table = rastr_win.Tables(Generator.table)
    vetv_table = rastr_win.Tables(Vetv.table)
    node_table = rastr_win.Tables(Node.table)
    ti_table = t.Tables("ti")

    rgm_obj.rgm()

    # добавляем столбцы в таблицы
    add_cols(rastr_win=rastr_win, table=Node.table, name_new_cols="sel_new")
    add_cols(rastr_win=rastr_win, table=Node.table, name_new_cols="vras_new")
    add_cols(rastr_win=rastr_win, table=Node.table, name_new_cols="qmin_new")
    add_cols(rastr_win=rastr_win, table=Node.table, name_new_cols="qmax_new")
    add_cols(rastr_win=rastr_win, table=Vetv.table, name_new_cols="sel_new2")
    add_cols(rastr_win=rastr_win, table=Area.table, name_new_cols="pop_new")
    add_cols(rastr_win=rastr_win, table=Area.table, name_new_cols="poq_new")

    group_corr_area.calc_cols(key="", column="pop_new", formula=Area.pop)
    group_corr_area.calc_cols(key="", column="poq_new", formula=Area.poq)

    group_corr_vetv.calc_cols(key="", column="sel_new2", formula=Vetv.sel)

    selection_remove_tick.vetv(formula=0)
    selection_remove_tick.node(formula=0)

    group_corr_node.calc_cols(key="", column="sel_new", formula=0)
    group_corr_node.calc_cols(key="", column="sel_new", formula=Node.sel)

    group_corr_node.calc_cols(key="", column="vras_new", formula=0)
    group_corr_node.calc_cols(key="", column="vras_new", formula=Node.vras)

    # --------- удаление выключателей ---------------
    group_corr_node.calc_cols(column="sel", key=area, formula=1)
    group_corr_node.calc_cols(column=Node.sel, key=area, formula=1)

    # убирает sel-узла если на ВЛ с одной стороны выделен узел
    vetvyklvybexc = "(iq.bsh!=0 & ip.bsh=0)|(ip.bsh!=0 & iq.bsh=0)|(ip.sel=0|iq.sel=0)|(ip.tip=0|iq.tip=0))"

    flvykl = 0
    group_corr_vetv.calc_cols(column=Vetv.groupid, key=vetvyklvybexc, formula=1)

    for povet in range(0, 10000):
        ivet = set_sel(rastr_win=rastr_win, table=Vetv.table, key="tip=2 & !sta &groupid !=1")
        if ivet is None:
            break

        ip = get_.get_cell_row(table=Vetv.table, column=Vetv.ip, row=ivet)
        iq = get_.get_cell_row(table=Vetv.table, column=Vetv.iq, row=ivet)

        if ip > iq:
            ny = iq
            ndel = ip
        else:
            ny = ip
            ndel = iq

        ndny = 0
        ndndel = 0

        # Меняем местами, так как удаляемый нельзя удалять, а неудаляемый можно
        if ndndel == 0 and ndny == 1:
            buff = ny
            ny = ndel
            ndel = buff

        if ndndel == 0 or ndny == 0:  # Если хотя бы один можно удалить
            flvykl = flvykl + 1

            iny = set_sel(rastr_win=rastr_win, table=Vetv.table, key=f"ny={ny}")
            idel = set_sel(rastr_win=rastr_win, table=Vetv.table, key=f"ny={ndel}")

            pgdel = get_.get_cell_row(table=Node.table, column=Node.pg, row=idel)
            qgdel = get_.get_cell_row(table=Node.table, column=Node.qg, row=idel)
            pndel = get_.get_cell_row(table=Node.table, column=Node.pn, row=idel)
            qndel = get_.get_cell_row(table=Node.table, column=Node.qn, row=idel)
            bshdel = get_.get_cell_row(table=Node.table, column=Node.bsh, row=idel)
            gshdel = get_.get_cell_row(table=Node.table, column=Node.qsh, row=idel)

            pgny = get_.get_cell_row(table=Node.table, column=Node.pg, row=iny)
            qgny = get_.get_cell_row(table=Node.table, column=Node.qg, row=iny)
            pnny = get_.get_cell_row(table=Node.table, column=Node.pn, row=iny)
            qnny = get_.get_cell_row(table=Node.table, column=Node.qn, row=iny)
            bshny = get_.get_cell_row(table=Node.table, column=Node.bsh, row=iny)
            gshny = get_.get_cell_row(table=Node.table, column=Node.gsh, row=iny)

            qnmax1 = get_.get_cell_row(table=Node.table, column=Node.qn_max, row=iny)
            qnmin1 = get_.get_cell_row(table=Node.table, column=Node.qn_min, row=iny)

            qnmax2 = get_.get_cell_row(table=Node.table, column=Node.qn_max, row=idel)
            qnmin2 = get_.get_cell_row(table=Node.table, column=Node.qn_min, row=idel)

            pnmax1 = get_.get_cell_row(table=Node.table, column=Node.pn_max, row=iny)
            pnmin1 = get_.get_cell_row(table=Node.table, column=Node.pn_min, row=iny)

            pnmax2 = get_.get_cell_row(table=Node.table, column=Node.pn_max, row=idel)
            pnmin2 = get_.get_cell_row(table=Node.table, column=Node.pn_min, row=idel)

            exist_load1 = get_.get_cell_row(table=Node.table, column=Node.exist_load, row=iny)
            exist_load2 = get_.get_cell_row(table=Node.table, column=Node.exist_load, row=idel)

            variable_.make_changes_row(table=Node.table, column=Node.pg, row=iny, value=pgdel + pgny)
            variable_.make_changes_row(table=Node.table, column=Node.qg, row=iny, value=qgdel + qgny)
            variable_.make_changes_row(table=Node.table, column=Node.pn, row=iny, value=pndel + pnny)
            variable_.make_changes_row(table=Node.table, column=Node.qn, row=iny, value=qndel + qnny)
            variable_.make_changes_row(table=Node.table, column=Node.bsh, row=iny, value=bshdel + bshny)
            variable_.make_changes_row(table=Node.table, column=Node.gsh, row=iny, value=gshdel + gshny)

            variable_.make_changes_row(table=Node.table, column=Node.pn_max, row=iny, value=pnmax1 + pnmax2)
            variable_.make_changes_row(table=Node.table, column=Node.qn_max, row=iny, value=qnmax1 + qnmax2)

            if qnmin1 < qnmin2:
                variable_.make_changes_row(table=Node.table, column=Node.qn_min, row=iny, value=qnmin1)
            else:
                variable_.make_changes_row(table=Node.table, column=Node.qn_min, row=iny, value=qnmin2)

            if pnmin1 < pnmin2:
                variable_.make_changes_row(table=Node.table, column=Node.pn_min, row=iny, value=pnmin1)
            else:
                variable_.make_changes_row(table=Node.table, column=Node.pn_min, row=iny, value=pnmin2)

            if exist_load1 > 0 or exist_load2 > 0:
                variable_.make_changes_row(table=Node.table, column=Node.exist_load, row=iny, value=1)

            v1 = get_.get_cell_row(table=Node.table, column=Node.vzd, row=iny)
            v2 = get_.get_cell_row(table=Node.table, column=Node.vzd, row=idel)

            igen = set_sel(rastr_win=rastr_win, table=Generator.table, key=f"Node={ndel}")
            if igen != (-1):
                while igen != (-1):
                    variable_.make_changes_row(table=Generator.table, column=Generator.Node, row=igen, value=ny)
                    igen = gen_table.FindNextSel(-1)

            if v1 != v2 and v1 > 0.3 and v2 > 0.3 and (qmax1 + qmax2) != 0:
                variable_.make_changes_row(table=Node.table, column=Node.vzd, row=iny,
                                           value=(v1 * qmax1 + v2 * qmax2) / (
                                                   qmax1 + qmax2))  # Делаем средневзвешенное по qmax напряжение

            if v1 == 0 and v2 != 0:
                variable_.make_changes_row(table=Node.table, column=Node.vzd, row=iny, value=v2)

            if v1 != 0 and v2 != 0:
                qmin_iny_ = get_.get_cell_row(table=Node.table, column=Node.qmin, row=iny)
                _qmin_idel = get_.get_cell_row(table=Node.table, column=Node.qmin, row=ndel)
                variable_.make_changes_row(table=Node.table, column=Node.qmin, row=iny, value=qmin_iny_ + _qmin_idel)
                variable_.make_changes_row(table=Node.table, column=Node.qmax, row=iny, value=qmax1 + qmax2)

            vetv_table.SetSel(f"(ip={ip} & iq={iq})|(iq={ip} & ip={iq})")
            vetv_table.DelRowS()  # Удаляем ветвь

            group_corr_node.calc_cols(column=Vetv.iq, key=f"iq={ndel}", formula=ny)
            group_corr_node.calc_cols(column=Vetv.ip, key=f"ip={ndel}", formula=ny)

            ti_table.SetSel(
                f"(prv_num=20 | prv_num=7 | prv_num=6 | prv_num=5 | prv_num=4 | prv_num=3 | prv_num=2 | prv_num=1) & id1={ndel}")
            ti_table.Cols("id1").Calc(ny)

            node_table.DelRowS()  # Удаляем узел
        else:
            group_corr_vetv.calc_cols(key=f"(ip={ip} & iq={iq})|(iq={ip} & ip={iq})", column=Vetv.groupid, formula=1)

    kod = rgm_obj.rgm()
    if kod != 0:
        print("Regim do not exist")

    group_corr_vetv.calc_cols(key="", column=Vetv.sel, formula=0)
    group_corr_node.calc_cols(key="", column=Node.sel, formula=0)


def del_switches_gen(rastr_win: object) -> None:
    variable_ = Variable(rastr_win=rastr_win)
    group_corr_vetv = GroupCorr(rastr_win=rastr_win, table=Vetv.table, column=Vetv.groupid)
    group_corr_node = GroupCorr(rastr_win=rastr_win, table=Node.table, column=Node.sel)
    group_corr_area = GroupCorr(rastr_win=rastr_win, table=Area.table)
    get_ = GettingParameter(rastr_win=rastr_win)
    rgm_obj = Regime(rastr_win=rastr_win)
    selection_remove_tick = SelectionRemoveTick(rastr_win=rastr_win)
    gen_table = rastr_win.Tables(Generator.table)
    vetv_table = rastr_win.Tables(Vetv.table)
    node_table = rastr_win.Tables(Node.table)
    ti_table = t.Tables("ti")
    findNextSel = FindNextSelection(rastr_win=rastr_win, table=Node.table)

    selection_remove_tick.node(formula=0)
    selection_remove_tick.vetv(formula=0)

    k1 = findNextSel.row(table=Node.table, select="")

    while k != (-1):
        ny1 = get_.get_cell_row(table=Node.table, column=Node.ny, row=k1)
        vetv_table.SetSel(f"(ip={ny1})|(iq={ny1})")
        vetv_count = get_.get_count_table(table=Vetv.table)
        if vetv_count == 1:
            vetv_table.SetSel(f"x<1 & (tip=0|tip=2)&((ip={ny1})|(iq={ny1}))")
            if vetv_count.Count() == 1:
                k3 = findNextSel.row(table=Node.table, select=f"x<1 & (tip=0|tip=2)&((ip={ny1})|(iq={ny1}))")
                if k3 != (-1):
                    ip_ = get_.get_cell_row(table=Vetv.table, column=Vetv.ip, row=k3)
                    if ip == ny1:
                        ny2 = get_.get_cell_row(table=Vetv.table, column=Vetv.iq, row=k3)
                    else:
                        ny2 = get_.get_cell_row(table=Vetv.table, column=Vetv.ip, row=k3)
                    k2 = findNextSel.row(table=Generator.table, select=f"Node={ny1}")
                    if k2 != (-1):
                        k4 = findNextSel.row(table=Node.table, select=f"ny={ny2}")
                        if k4 != (-1):
                            pn_k1 = get_.get_cell_row(table=Node.table, column=Node.pn, row=k1)
                            pn_k4 = get_.get_cell_row(table=Node.table, column=Node.pn, row=k4)

                            variable_.make_changes_row(table=Node.table, column=Node.pn, row=k4,
                                                       value=pn_k1 + pn_k4)

                            exist_load_k1 = get_.get_cell_row(table=Node.table, column=Node.exist_load, row=k1)
                            variable_.make_changes_row(table=Node.table, column=Node.exist_load, row=k4,
                                                       value=exist_load_k1)

                            exist_gen_k1 = get_.get_cell_row(table=Node.table, column=Node.exist_gen, row=k1)
                            variable_.make_changes_row(table=Node.table, column=Node.exist_gen, row=k4,
                                                       value=exist_gen_k1)

                            pn_max_k1 = get_.get_cell_row(table=Node.table, column=Node.pn_max, row=k1)
                            pn_max_k4 = get_.get_cell_row(table=Node.table, column=Node.pn_max, row=k4)
                            variable_.make_changes_row(table=Node.table, column=Node.pn_max, row=k4,
                                                       value=pn_max_k1 + pn_max_k4)

                            pn_min_k4 = get_.get_cell_row(table=Node.table, column=Node.pn_min, row=k4)
                            pn_min_k1 = get_.get_cell_row(table=Node.table, column=Node.pn_min, row=k1)
                            if pn_min_k4 >= pn_min_k1:
                                variable_.make_changes_row(table=Node.table, column=Node.pn_min, row=k4,
                                                           value=pn_min_k1)

                            pg_max_k1 = get_.get_cell_row(table=Node.table, column=Node.pg_max, row=k1)
                            pg_max_k4 = get_.get_cell_row(table=Node.table, column=Node.pg_max, row=k4)
                            variable_.make_changes_row(table=Node.table, column=Node.pg_max, row=k4,
                                                       value=pg_max_k1 + pg_max_k4)

                            pg_min_k4 = get_.get_cell_row(table=Node.table, column=Node.pg_min, row=k4)
                            pg_min_k1 = get_.get_cell_row(table=Node.table, column=Node.pg_min, row=k1)
                            if pg_min_k4 >= pg_min_k1:
                                variable_.make_changes_row(table=Node.table, column=Node.pg_min, row=k4,
                                                           value=pg_min_k1)

                            variable_.make_changes_row(table=Node.table, column=Node.sel, row=k1, value=1)
                            variable_.make_changes_row(table=Node.table, column=Node.sel, row=k3, value=1)

                            ti_table.SetSel(f"(prv_num=20|prv_num=7|prv_num=6|prv_num=5|prv_num=4|prv_num=3|prv_num=2|prv_num=1)&id1={ny1}")
                            ti_table.Cols("id1").Calc(ny2)
                            gen_table.SetSel(f"Node={ny1}")
                            k2 = gen_table.FindNextSel(-1)
                            while k2 != (-1):
                                variable_.make_changes_row(table=Generator.table, column=Generator.Node, row=k2,
                                                           value=ny2)
                                k2 = gen_table.FindNextSel(k2)
        uzl.SetSel("")
        k1 = uzl.FindNextSel(k1)

    vetv_table.SetSel("sel=1")
    vetv_table.DelRowS()

    node_table.SetSel("sel=1")
    node_table.DelRowS()

    selection_remove_tick.node(formula=0)
    selection_remove_tick.vetv(formula=0)