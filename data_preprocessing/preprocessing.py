#! /usr/bin/env python3

import sys
import re

reg_dim = re.compile(r'(?<=\d) (in|seats|gal|RPM)')
reg_split = re.compile(r",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)")
body_type = ['Convertible', 'Coupe', 'Hatchback', 'Minivan', 'Pickup Truck', 'SUV / Crossover', 'Sedan', 'Van', 'Wagon']
transmission = ['A', 'CVT', 'Dual Clutch', 'M']
engine_type = ['H', 'I', 'R', 'V', 'W']
wheel_system = ['4X2', 'All-Wheel Drive', 'Four-Wheel Drive', 'Front-Wheel Drive', 'Rear-Wheel Drive']
fuel_type = ['Biodiesel', 'Compressed Natural Gas', 'Diesel', 'Electric', 'Flex Fuel Vehicle', 'Gasoline', 'Hybrid']
type_list = [body_type, fuel_type, transmission, wheel_system]
index_list = [5, 23, 56, 62]
drop_list = [0, 2, 3, 4, 5, 6, 7, 9, 11, 12, 13, 15, 16, 17, 18, 20, 23, 24, 28,
             30, 31, 33, 36, 37, 38, 40, 41, 42, 45, 46, 47, 49, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]
for line in sys.stdin:
    line = line.strip()
    items = re.split(reg_split, line)
    items = [re.sub('--', '', item) for item in items]
    items = [re.sub(reg_dim, '', item) for item in items]
    items = [re.sub('FALSE', '0', item, flags=re.IGNORECASE) for item in items]
    items = [re.sub('TRUE', '1', item, flags=re.IGNORECASE) for item in items]
    try:
        hp = re.split(r' hp @ ', re.sub('[",]', '', items[47]))
        torque = re.split(r' lb-ft @ ', re.sub('[",]', '', items[55]))
        items.extend(hp)
        items.extend(torque)

    except IndexError:
        continue

    for i in range(len(type_list)):
        try:
            index0 = type_list[i].index(items[index_list[i]])
            tp = [0] * len(type_list[i])
            tp[index0] = 1
            items.extend(tp)
        except ValueError:
            tp = [''] * len(type_list[i])
            items.extend(tp)
    try:
        index2 = engine_type.index(items[15][0])
        eng_tp = [0] * len(engine_type)
        eng_tp[index2] = 1
        items.extend(eng_tp)
    except (ValueError, IndexError):
        eng_tp = [''] * len(engine_type)
        items.extend(eng_tp)
    for i in reversed(drop_list):
        items.pop(i)
    if len(items) == 57:
        print('\t'.join([str(item) for item in items]))

