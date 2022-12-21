def get(arg):

    #make from string a list
    arg = list(arg)

    #get len list
    lenarg = len(arg)

    #get middle of len list
    middle_of_lenarg = float(lenarg/2)

    #if str(middle_of_lenarg) is full int it will return the 2 middle chars
    #else it will return the item arg
    if '.0 ' in str(middle_of_lenarg):
        return [arg[int(middle_of_lenarg-0.5)],arg[int(middle_of_lenarg+0.5)]]
    else:
        return [arg[int(middle_of_lenarg)]]

print(get(input('~>')))