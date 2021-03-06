#!/usr/bin/env python3
import ast
import sys
import itertools
import lineal

def solve():
    with open(sys.argv[1]) as _input:
        lines = _input.readlines()
    
    N,M,K= int(lines[0]), int(lines[1]), int(lines[2]) 
    
    
    animals = ast.literal_eval(lines[3])
    greatness = ast.literal_eval(lines[4])
    greatness = [int(i) for i in greatness]
    animals_dict = dict(zip(animals, greatness)) # Diccionario (animal:grandeza) O(N)
    

    parts = [ast.literal_eval(lines[i]) for i in range(5, len(lines))]
    lineal.sort_rest_of_scenes_locally(parts, N, animals_dict) 
    lineal.sort_scenes(parts, animals_dict)
    
    all_scenes = list(itertools.chain(*parts))
    famous_animals = lineal.get_animal_ocurrences(all_scenes, animals, max)
    not_famous_animals = lineal.get_animal_ocurrences(all_scenes, animals, min)
    for i in range(len(parts)):
        if i == 0:
            print('Apertura: ', end=' ')
            print(parts[0])
        else:
            print('Parte: ', end=' ')
            print(parts[i])
    
    print('El animal que participó en más escenas dentro del espectaculo fueron: ')
    for animal,times in famous_animals.items():
        print('*    ' + animal + ', que participó en ' + str(times) + ' escenas')
    
    print('El animal que partició en menos escenas fueron: ')
    for animal,times in not_famous_animals.items():
        print('*    ' + animal + ', que participó en ' + str(times) + ' escenas')
   

    print('La escena de mayor grandeza fue ' + max(lineal.scenes_to_greatness, key=lineal.scenes_to_greatness.get))
    print('La escena de menor grandeza fue ' + min(lineal.scenes_to_greatness, key=lineal.scenes_to_greatness.get))
    print('El promedio de grandeza de todo el espectaculo fue de ' + str(lineal.get_avg(all_scenes, lineal.scenes_to_greatness)))

solve()
