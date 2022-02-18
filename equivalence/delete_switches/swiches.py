# -*- coding: utf-8 -*-
from equivalence.actions.add_cols_in_tables import add_cols, AddCols
from equivalence.actions.get import GettingParameter
from equivalence.actions.group_correction import GroupCorr
from equivalence.actions.selection import SelectionRemoveTick
from equivalence.actions.variable import Variable
from equivalence.calculation.regime import Regime
from equivalence.tables.Tables import Node, Vetv, Generator, Area
from equivalence.actions.zeroing import Zeroing


def del_swiches(
        rastr_win: object,
        viborka_main: str = "(na<500 | na>600) & na!=8082 & na!=8037 & na!=5329 & na!=5230") -> None:
    """
    dle_swiches -
    :param rastr_win:
    :param viborka_main:
    :return:
    """
    gen_table = rastr_win.Tables(Generator.table)
    vetv_table = rastr_win.Tables(Vetv.table)
    node_table = rastr_win.Tables(Node.table)
    area_table = rastr_win.Tables(Area.table)

    zeroing_obj = Zeroing(rastr_win=rastr_win)

    node_add_cols_odj = AddCols(rastr_win=rastr_win, table=Node.table)
    vetv_add_cols_obj = AddCols(rastr_win=rastr_win, table=Vetv.table)
    area_add_cols_obj = AddCols(rastr_win=rastr_win, table=Area.table)

    # добавляем столбцы в таблицы
    node_add_cols_odj.add(name_new_cols='sel_new')
    node_add_cols_odj.add(name_new_cols='vras_new')
    node_add_cols_odj.add(name_new_cols='qmin_new')
    node_add_cols_odj.add(name_new_cols='qmax_new')

    vetv_add_cols_obj.add(name_new_cols='sel_new2')
    vetv_add_cols_obj.add(name_new_cols='ip_new')
    vetv_add_cols_obj.add(name_new_cols='iq_new')
    vetv_add_cols_obj.add(name_new_cols='nq_new')

    area_add_cols_obj.add(name_new_cols='pop_new')
    area_add_cols_obj.add(name_new_cols='poq_new')

    area_table.Cols("pop_new").Calc(Area.pop)
    area_table.Cols("poq_new").Calc(Area.poq)
    vetv_table.SetSel("")
    vetv_table.Cols("sel_new2").Calc(Vetv.sel)

    zeroing_obj.node()
    zeroing_obj.vetv()

    node_table.SetSel("")
    node_table.Cols("sel_new").Calc(0)
    node_table.Cols("sel_new").Calc(Node.sel)

    node_table.Cols("vras_new").Calc(0)
    node_table.Cols("vras_new").Calc(Node.vras)

    vetv_table.SetSel("")
    vetv_table.Cols("ip_new").Calc("ip")
    vetv_table.Cols("iq_new").Calc("iq")
    vetv_table.Cols("np_new").Calc("np")

    node_table.SetSel(viborka_main)
    node_table.Cols(Node.sel).Calc(1)
    node_table.Cols("sel_new").Calc("sel")

    # убирает sel-узла если на ВЛ с одной стороны выделен узел
    vetvyklvybexc = "(iq.bsh!=0 & ip.bsh=0)|(ip.bsh!=0 & iq.bsh=0)|(ip.sel=0|iq.sel=0)|(ip.tip=0|iq.tip=0)"
    vetv_table.SetSel(vetvyklvybexc)
    vetv_table.Cols("groupid").Calc(1)

    for povet in range(0, 10000):
        # Выборка ветвей, которые считаем выключателями и которые не откл.
        vetv_table.SetSel("tip=2 & !sta & groupid != 1")
        ivet = vetv_table.FindNextSel(-1)
        if ivet == (-1):
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
        gshdel = node_table.Cols(Node.gsh).Z(idel)

        qnmax2 = node_table.Cols(Node.qn_max).Z(idel)
        qnmin2 = node_table.Cols(Node.qn_min).Z(idel)
        pnmax2 = node_table.Cols(Node.pn_max).Z(idel)
        pnmin2 = node_table.Cols(Node.pn_min).Z(idel)
        exist_load2 = node_table.Cols(Node.exist_load).Z(idel)

        pgny = node_table.Cols(Node.pg).Z(iny)
        qgny = node_table.Cols(Node.qg).Z(iny)
        pnny = node_table.Cols(Node.pn).Z(iny)
        qnny = node_table.Cols(Node.qn).Z(iny)
        bshny = node_table.Cols(Node.bsh).Z(iny)
        gshny = node_table.Cols(Node.gsh).Z(iny)

        qnmax1 = node_table.Cols(Node.qn_max).Z(iny)
        qnmin1 = node_table.Cols(Node.qn_min).Z(iny)
        pnmax1 = node_table.Cols(Node.pn_max).Z(iny)
        pnmin1 = node_table.Cols(Node.pn_min).Z(iny)
        exist_load1 = node_table.Cols(Node.exist_load).Z(iny)

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

        v1 = node_table.Cols(Node.vzd).Z(iny)
        v2 = node_table.Cols(Node.vzd).Z(idel)

        qmax1 = node_table.Cols("qmax").Z(iny)
        qmax2 = node_table.Cols("qmax").Z(idel)

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

        node_table.DelRowS()  # Удаляем узелов


def del_switches_gen(rastr_win: object) -> None:
    """

    :param rastr_win:
    :return:
    """
    gen_table = rastr_win.Tables(Generator.table)
    vetv_table = rastr_win.Tables(Vetv.table)
    node_table = rastr_win.Tables(Node.table)

    node_table.SetSel("")
    k1 = node_table.FindNextSel(-1)
    while k1 != (-1):
        ny1 = node_table.Cols(Node.ny).Z(k1)
        vetv_table.SetSel(f"(ip={ny1})|(iq={ny1})")
        vetv_count = vetv_table.Count
        if vetv_count == 1:
            vetv_table.SetSel(f"x<1 & (tip=0|tip=2) & ((ip={ny1})|(iq={ny1}))")
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
                            ti_table.SetSel(
                                f"(prv_num=20|prv_num=7|prv_num=6|prv_num=5|prv_num=4|prv_num=3|prv_num=2|prv_num=1)&id1={ny1}")
                            ti_table.Cols("id1").Calc(ny2)
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


def delete_UKR(rastr_win: object):
    """

    :param rastr_win:
    :return:
    """
    vetv_table = rastr_win.Tables(Vetv.table)
    node_table = rastr_win.Tables(Node.table)

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

    vetv_table.SetSel("((iq.sel=1 & ip.sel=0)|(ip.sel=1 & iq.sel=0)) & ip.na>800 & iq.na>800 &!sta")
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
        vetv_table.SetSel("((iq.sel=1 & ip.sel=0)|(ip.sel=1 & iq.sel=0)) & ip.na>800 & iq.na>800 &!sta")
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
    gen_table = rastr_win.Tables(Generator.table)
    vetv_table = rastr_win.Tables(Vetv.table)
    node_table = rastr_win.Tables(Node.table)
    pqd = rastr_win.Tables("graphik2")
    graphikIT = rastr_win.Tables("graphikIT")
    polin_table = rastr_win.Tables("polin")
    darea_table = rastr_win.Tables("darea")
    area_table = rastr_win.Tables("area")
    area2_table = rastr_win.Tables("area2")

    node_add_cols_odj = AddCols(rastr_win=rastr_win, table=Node.table)
    vetv_add_cols_obj = AddCols(rastr_win=rastr_win, table=Vetv.table)

    vetv_add_cols_obj.add(name_new_cols='pl_iq_new')
    vetv_add_cols_obj.add(name_new_cols='pl_ip_new')
    vetv_add_cols_obj.add(name_new_cols='ql_iq_new')
    vetv_add_cols_obj.add(name_new_cols='ql_ip_new')
    vetv_add_cols_obj.add(name_new_cols='ql_ip_new')
    vetv_add_cols_obj.add(name_new_cols='gran')

    node_add_cols_odj.add(name_new_cols='muskod_new')
    node_add_cols_odj.add(name_new_cols='vras_new')

    vetv_table.Cols("pl_iq_new").Calc("pl_iq")
    vetv_table.Cols("pl_ip_new").Calc("pl_ip")
    vetv_table.Cols("ql_iq_new").Calc("ql_iq")
    vetv_table.Cols("ql_ip_new").Calc("ql_ip")
    node_table.Cols("vras_new").Calc("vras")

    gen_table.SetSel("Node.sel=1")
    gen_table.DelRowS()

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
            muskod_new_ = node_table.Cols("muskod_new").SetZ(k2, 0)
            if muskod_new_ == 0:
                node_table.Cols(Node.pn).SetZ(k2, 0)
                node_table.Cols(Node.qn).SetZ(k2, 0)

                node_table.Cols(Node.pg).SetZ(k2, 0)
                node_table.Cols(Node.qg).SetZ(k2, 0)

                node_table.Cols(Node.nrk).SetZ(k2, 0)
                node_table.Cols(Node.brk).SetZ(k2, 0)

                node_table.Cols(Node.qsh).SetZ(k2, 0)
                node_table.Cols(Node.bshr).SetZ(k2, 0)

                node_table.Cols(Node.bsh).SetZ(k2, 0)
                node_table.Cols(Node.vras).SetZ(k2, 0)

                node_table.Cols("muskod_new").SetZ(k2, 1)
                node_table.Cols(Node.vzd).SetZ(k2, node_table.Cols("vras_new").z(k2))

                node_table.Cols(Node.qmin).SetZ(k2, -9999.)
                node_table.Cols(Node.qmax).SetZ(k2, 9999.)

                node_table.Cols(Node.pg_min).SetZ(k2, -9999.)
                node_table.Cols(Node.pg_max).SetZ(k2, 9999.)

                node_table.Cols(Node.pn_min).SetZ(k2, 0)
                node_table.Cols(Node.pn_max).SetZ(k2, 0)

                node_table.Cols(Node.qn_min).SetZ(k2, 0)
                node_table.Cols(Node.qn_max).SetZ(k2, 0)

                node_table.Cols(Node.exist_gen).SetZ(k2, 1)
                node_table.Cols(Node.exist_load).SetZ(k2, 0)

                uhom_ = node_table.Cols(Node.uhom).Z(k2)
                if uhom_ == 110:
                    node_table.Cols(Node.qmin).SetZ(k2, -300.)
                    node_table.Cols(Node.qmax).SetZ(k2, 300.)

                    node_table.Cols(Node.pg_min).SetZ(k2, -300.)
                    node_table.Cols(Node.pg_max).SetZ(k2, 300.)

            node_table.Cols(Node.pg).SetZ(k2, node_table.Cols(Node.pg).Z(k2) - pn11)
            node_table.Cols(Node.qg).SetZ(k2, node_table.Cols(Node.qg).Z(k2) - qn11)

        k = vetv_table.FindNextSel(k)

    vetv_table.SetSel("iq.sel=1 & ip.sel=0")
    k = vetv_table.FindNextSel(-1)
    while k != (-1):
        iq1 = vetv_table.Cols(Vetv.iq).Z(k)
        pn11 = vetv_table.Cols("pl_iq_new").Z(k)
        qn11 = vetv_table.Cols("ql_iq_new").Z(k)

        vetv_table.Cols(Vetv.br_ip).SetZ(k, 0)
        vetv_table.Cols("gran").SetZ(k, 1)

        node_table.SetSel(f"ny={iq1}")
        k2 = node_table.FindNextSel(-1)
        if k2 != (-1):
            muskod_new_ = node_table.Cols("muskod_new").Z(k2)
            if muskod_new_ == 0:
                node_table.Cols(Node.pn).SetZ(k2, 0)
                node_table.Cols(Node.qn).SetZ(k2, 0)

                node_table.Cols(Node.pg).SetZ(k2, 0)
                node_table.Cols(Node.qg).SetZ(k2, 0)

                node_table.Cols(Node.nrk).SetZ(k2, 0)
                node_table.Cols(Node.brk).SetZ(k2, 0)

                node_table.Cols(Node.qsh).SetZ(k2, 0)
                node_table.Cols(Node.bshr).SetZ(k2, 0)

                node_table.Cols(Node.bsh).SetZ(k2, 0)
                node_table.Cols(Node.vras).SetZ(k2, 0)
                node_table.Cols("muskod_new").SetZ(k2, 1)

                node_table.Cols(Node.vzd).SetZ(k2, node_table.Cols("vras_new").Z(k2))

                node_table.Cols(Node.qmin).SetZ(k2, -9999.)
                node_table.Cols(Node.qmax).SetZ(k2, 9999.)

                node_table.Cols(Node.pg_min).SetZ(k2, -9999.)
                node_table.Cols(Node.pg_max).SetZ(k2, 9999.)

                node_table.Cols(Node.pn_min).SetZ(k2, 0)
                node_table.Cols(Node.pn_max).SetZ(k2, 0)

                node_table.Cols(Node.qn_min).SetZ(k2, 0)
                node_table.Cols(Node.qn_max).SetZ(k2, 0)

                node_table.Cols(Node.exist_gen).SetZ(k2, 1)
                node_table.Cols(Node.exist_load).SetZ(k2, 0)

                uhom_k2 = node_table.Cols(Node.uhom).Z(k2)
                if uhom_k2 == 110:
                    node_table.Cols(Node.qmin).SetZ(k2, -300.)
                    node_table.Cols(Node.qmax).SetZ(k2, 300.)

                    node_table.Cols(Node.pg_min).SetZ(k2, -300.)
                    node_table.Cols(Node.pg_max).SetZ(k2, 300.)

            node_table.Cols(Node.pg).SetZ(k2, (node_table.Cols(Node.pg).Z(k2)) + pn11)
            node_table.Cols(Node.pg).SetZ(k2, (node_table.Cols(Node.qg).Z(k2)) + qn11)

        k = vetv_table.FindNextSel(k)

    vetv_table.SetSel("iq.sel=1 & ip.sel=1")
    vetv_table.Cols(Vetv.sel).Calc(1)
    vetv_table.SetSel("sel=1")
    vetv_table.DelRowS()
    rastr_win.rgm("p")
    # -------------- удаление узлов -----------------
    delUzlotkl = 1
    if delUzlotkl == 1:
        vetv_table.SetSel("1")
        vetv_table.Cols(Vetv.sel).Calc(0)

        node_table.SetSel("1")
        node_table.Cols(Node.sel).Calc(0)

        node_table.SetSel("1")
        inode = node_table.FindNextSel(-1)

        while inode != (-1):
            ny = node_table.Cols(Node.ny).Z(inode)
            vetv_table.SetSel(f"{ny}=ip|iq={ny}")
            vtv = vetv_table.FindNextSel(-1)
            if vtv > (-1):
                pass
            else:
                node_table.Cols(Node.sel).SetZ(inode, 1)
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
        pq22 = gen_table.Cols(Generator.NumPQ).Z(k)
        pqd.SetSel(f"Num={pq22}")
        pqd.DelRowS()
        k = gen_table.FindNextSel(k)
    # --------------удаление всего остального-----------------
    gen_table.SetSel(f"Node.na=0")
    gen_table.DelRowS()
    graphikIT.SetSel("")
    k = graphikIT.FindNextSel(-1)
    while k != (-1):
        nzav = graphikIT.Cols("Num").Z(k)
        vetv_table.SetSel(f"n_it={nzav}")
        k2 = vetv_table.FindNextSel(-1)
        if k2 != (-1):
            pass
        else:
            graphikIT.Cols("Num").SetZ(k, 0)
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
            area_table.Cols("na").SetZ(k, 0)
        k = area_table.FindNextSel(k)

    area_table.SetSel("na=0")
    area_table.DelRowS()
    area2_table.SetSel("")
    k = area2_table.FindNextSel(-1)
    while k != (-1):
        na1 = area2_table.Cols("npa").Z(k)
        node_table.SetSel(f"npa={na1}")
        k2 = node_table.FindNextSel(-1)
        if k2 != (-1):
            pass
        else:
            area2_table.Cols("npa").SetZ(k, 0)
        k = area2_table.FindNextSel(k)

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

    darea_table.SetSel("no=0")
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
        if q_min == -9999.0 and q_max == 9999.0:
            uhom = table_node.Cols(Node.uhom).Z(i)
            table_node.Cols(Node.vzd).SetZ(i, uhom)
