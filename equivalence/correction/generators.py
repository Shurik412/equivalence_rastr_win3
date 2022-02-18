def off_the_generator_if_the_node_off(rastr_win: object):
    # '************************************************************
    # ' Назначение: Отключение генераора, если узел к которому подключен
    # '             генератор отключен.
    # ' Входные параметры: Nothing
    # ' Возврат:    Nothing
    # '************************************************************
    t_gen = rastr_win.Tables(Generator.table)
    t_node = rastr_win.Tables(Node.table)
    t_gen.SetSel("")
    k = t_gen.FindNextSel(-1)
    while k != (-1):
        nyGenerator = t_gen.Cols(Generator.Node).Z(k)
        t_node.SetSel(f"ny={nyGenerator}")
        kk = t_node.FindNextSel(-1)
        if kk != (-1):
            sta_gen = t_node.Cols(Node.sta).Z(kk)
            if sta_gen == 1:
                t_gen.Cols(Generator.sta).SetZ(k, 1)
        t_gen.SetSel("")
        k = t_gen.FindNextSel(k)
    print(" - Отключены генераторы в отключенных узлах.")


def delete_Generator_without_nodes(rastr_win: object):
    # ************************************************************
    #  Назначение:
    #  Входные параметры: Nothing
    #  Возврат:    Nothing
    # ************************************************************
    gen_tabel = rastr_win.Tables(Generator.table)
    gen_tabel.SetSel("Node.ny=0")
    gen_tabel.DelRowS()
