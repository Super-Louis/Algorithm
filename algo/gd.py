# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: gd.py
# Python  : python3.6
# Time    : 18-5-31 22:36
# Github  : https://github.com/Super-Louis

stations = dict()
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}

final_stations = set()

def get_best_stations():
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

    while states_needed:
        max_states_cover = set()
        best_station = None
        for station, states in stations.items():
            covered = states & states_needed
            if len(covered) > len(max_states_cover):
                best_station = station
                max_states_cover = covered
        final_stations.add(best_station)
        states_needed -= max_states_cover
    return final_stations

if __name__ == '__main__':
    final_stations = get_best_stations()
    print(final_stations)