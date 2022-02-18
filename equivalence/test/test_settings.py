from equivalence.settings import area_json

for area in area_json:
    print(f"{area['area_name']}\t{area['equivalent']}\t{area['u_min_TR']}\t{area['u_min_AREA']}\t{area['u_max_AREA']}\t{area['num_area']}\t")
