# -*- coding: utf-8 -*-
import time

from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.actions.zeroing import Zeroing
from equivalence.calculation.equivalent import Equivalent
from equivalence.calculation.regime import Regime
from equivalence.correction.generators import delete_Generator_without_nodes, off_the_generator_if_the_node_off
from equivalence.correction.node import removing_nodes_without_branches
from equivalence.correction.reactors import reactors_change
from equivalence.correction.vetv import remove_line, off_the_line_from_two_side, del_vetv
from equivalence.delete_switches.swiches import delete_area, delete_UKR, del_swiches, del_switches_gen, vzd_node
from equivalence.equivalence_node.equalization_full import equivalent_full_to_nodes
from equivalence.making_settings.equivalence import set_com_ekviv
from equivalence.settings import PATH_FILE_RASTR_LOAD, PATH_FILE_RASTR_SAVE
from equivalence.settings import area_json
from equivalence.tools.tool import changing_number_of_semicolons


def main():
    regime_obj = Regime(rastr_win=RASTR, switch_command_line=True)
    equivalent_obj = Equivalent(rastr_win=RASTR)
    zeroing_object = Zeroing(rastr_win=RASTR)

    print("Запуск:\n")

    # устанавливает настройки эквивалентирования

    set_com_ekviv(
        rastr_win=RASTR,
        zmax=1000,
        otm_n=0,
        smart=0,
        tip_ekv=0,
        ekvgen=0,
        tip_gen=1,
        ek_sh=0
    )

    # задает выделение sel=0 (обнуление)
    zeroing_object.node()
    zeroing_object.vetv()

    # расчет режима
    regime_obj.rgm(par='p')

    # отключение линий односторонне включенных
    off_the_line_from_two_side(rastr_win=RASTR)

    # откл. генераторов если откл. узел
    off_the_generator_if_the_node_off(rastr_win=RASTR)

    regime_obj.rgm(par='p')

    for area in area_json:
        if area['equivalent']:
            equivalent_full_to_nodes(
                rastr_win=RASTR,
                name_area=area['area_name'],
                uhom=area['u_min_TR'],
                v_ip_input=area['u_min_AREA'],
                v_iq_input=area['u_max_AREA']
            )
        equivalent_obj.ekv()
        # обнуление
        zeroing_object.node()
        zeroing_object.vetv()

    regime_obj.rgm(par='p')

    del_swiches(rastr_win=RASTR)
    print('1. del_swiches')

    zeroing_object.node()
    zeroing_object.vetv()

    regime_obj.rgm(par='p')

    del_switches_gen(rastr_win=RASTR)
    print('2. del_switches_gen')

    zeroing_object.node()
    zeroing_object.vetv()

    regime_obj.rgm(par='p')

    delete_UKR(rastr_win=RASTR)
    print('3. delete_UKR')

    zeroing_object.node()
    zeroing_object.vetv()

    regime_obj.rgm(par='p')

    delete_area(rastr_win=RASTR)
    print('4. delete_area')

    zeroing_object.node()
    zeroing_object.vetv()

    regime_obj.rgm(par='p')

    vzd_node(rastr_win=RASTR)
    print('6. vzd_node')

    zeroing_object.node()
    zeroing_object.vetv()

    regime_obj.rgm(par='p')

    off_the_generator_if_the_node_off(rastr_win=RASTR)

    zeroing_object.node()
    zeroing_object.vetv()

    delete_Generator_without_nodes(rastr_win=RASTR)

    zeroing_object.node()
    zeroing_object.vetv()

    reactors_change(rastr_win=RASTR)

    zeroing_object.node()
    zeroing_object.vetv()

    # remove_line(rastr_win=RASTR)

    # zeroing_object.node()
    # zeroing_object.vetv()

    regime_obj.rgm(par='p')

    del_vetv(rastr_win=RASTR)

    zeroing_object.node()
    zeroing_object.vetv()

    regime_obj.rgm(par='p')

    removing_nodes_without_branches(rastr_win=RASTR)

    zeroing_object.node()
    zeroing_object.vetv()

    delete_Generator_without_nodes(rastr_win=RASTR)

    regime_obj.rgm(par='p')


if __name__ == '__main__':
    LoadFile(rastr_win=RASTR).load(path_file=PATH_FILE_RASTR_LOAD, name_shabl_russian='режим')

    start = time.time()
    main()
    end = time.time()
    print(
        f'Время работы: '
        f'{changing_number_of_semicolons(number=(end - start) / 60, digits=2)} мин.'
    )

    save_file(rastr_win=RASTR, path_file=PATH_FILE_RASTR_SAVE, name_shabl_russian='режим')
    save_file(rastr_win=RASTR, path_file=f'{PATH_FILE_RASTR_SAVE}.rst', name_shabl_russian='динамика')