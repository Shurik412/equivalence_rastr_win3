def removing_nodes_without_branches(rastr_win: object):
    # ************************************************************
    #  Назначение: Удаление узлов без связи с ветвями
    #  Входные параметры: Nothing
    #  Возврат:    Nothing
    # ************************************************************
    node = rastr_win.Tables(Node.table)
    vetv = rastr_win.Tables(Vetv.table)
    nodeColMax = node.Count - 1
    # vetvColMax = vetv.Count - 1
    ii = 0
    for i in range(0, nodeColMax):
        Bsh = node.Cols("bsh").Z(i)
        id_ny = node.Cols("ny").Z(i)
        vetv.SetSel(f"ip.ny={id_ny} | iq.ny={id_ny}")
        col_vetv = vetv.FindNextSel(-1)
        key_1 = 1
        if key_1 == 1:
            node.Cols("sel").SetZ(i, 0)
            if col_vetv == (-1):
                node.Cols("sel").SetZ(i, 1)
                ii = ii + 1
        if key_1 == 0:
            vetv.Cols("sel").SetZ(i, 0)
            if colvetv != (-1):
                type_id = vetv.Cols("tip").Z(colvetv)
                if type_id == 2:
                    if Bsh == 0:
                        vetv.Cols("sel").SetZ(colvetv, 1)
    node.SetSel("sel=1")
    ii = node.Count - 1
    node.DelRowS()
    print(f" - удалены узлоы без связей с ветвями: {ii}")
    rastr_win.rgm("p")
