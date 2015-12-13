
from itertools import permutations

def read_input():
    lines = open('day9.input','r').readlines()
    places = set()
    distances = {}
    for l in lines:
        parts = l.strip().split()
        place1,place2,dist = parts[0],parts[2],int(parts[4])

        places.add(place1)
        places.add(place2)
        distances[(place1,place2)] = dist
        distances[(place2,place1)] = dist
    return list(places),distances

def main():
    places, distances = read_input()

    shortest = 9999999999999999
    for p in permutations(places):
        total = 0 
        for i in range(len(p)-1):
            total += distances[(p[i],p[i+1])]

        if total < shortest:
            shortest = total

    print shortest

if __name__ == '__main__':
    main()
