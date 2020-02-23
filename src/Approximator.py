from random import randint
from math import gcd
from time import time

ACTUAL_APPROXIMATION = 1.202056903159594285399738161511449990764986292

def main():
    combinations = int( input("Combinations: ") )
    bound = int( input("Bound: ") )
    
    data = []
    start_time = int( round(time() * 1000) )
    
    print( '=' * 20 )
    print( "Data Set:" )
    print( '=' * 20 )
    
    # Generates data set
    for i in range(combinations):
        combo = (randint(0, bound), randint(0, bound), randint(0, bound))
        data.append(combo)

        print(combo)

    # Checks for a combination of coprime triplets.
    coprime = 0
    for combo in data:
        a = combo[0]
        b = combo[1]
        c = combo[2]
        if( gcd(a, b) == 1 or gcd(a, c) == 1 or gcd(b, c) == 1 ):
            coprime += 1
            
        else:
            continue
    
    # Calculates approximation and time elapsed
    approximation = combinations / coprime
    time_taken = int( round(time() * 1000) ) - start_time
    
    print()
    print( "# of Coprime: {}".format(coprime) )
    print( "Computed Approximation: {}".format(approximation) )
    print( "Actual Approximation: {}".format(ACTUAL_APPROXIMATION) )
    
    # Calculates percentage difference
    diff = abs( approximation - ACTUAL_APPROXIMATION ) 
    p_diff = (diff / ((approximation + ACTUAL_APPROXIMATION) / 2) ) * 100
    print()
    print( "Difference: {}".format(diff) ) 
    print( "% Difference: {:.2f}".format(p_diff) )
    
    # Prints time elapsed 
    print()
    print( "Took {} ms to complete!".format(time_taken) )

    
main()