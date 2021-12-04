def selectActivity(activities):

    k = 0
    out = set()

    if(len(activities)):
        out.add(0)

    activities.sort(key = lambda x:x[1])

    for i in range(1,len(activities)):

        if(activities[i][0] >= activities[k][1]):
            out.add(i)
            k = i
    return out




if __name__ == '__main__':
 
    # List of given jobs. Each job has an identifier, a deadline, and a
    # profit associated with it
    #activities = [(3, 5),(1,4), (0, 6), (5, 7), (3, 8), (5, 9),(6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    activities = [(2,3),(9,14),(7,8),(1,6),(3,5)]
    result = selectActivity(activities)
    print([activities[i] for i in result])
