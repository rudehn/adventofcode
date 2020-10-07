def main():
    data_range = [387638, 919123]

    candidates = range(data_range[0], data_range[1]+1)
    candidates1 = map(str, candidates)

    print(len(candidates))

    candidates2 = filter(lambda x: all(map(lambda y, z: z>=y, x[:-1], x[1:])), candidates1)

    print(len(candidates2))

    candidates3 = filter(lambda x: 
        any(map(lambda y, z: int(z) - int(y) == 0, x[:-1], x[1:])), candidates2)

    print(len(candidates3))
    print(candidates3)

    candidates4 = filter(lambda x: { x.count(i): i for i in set(x)}.get(2, None) != None, candidates3)

    print(len(candidates4))
    print(candidates4)

if __name__=="__main__":
    main()