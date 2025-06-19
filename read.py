def readCsv(filename = 'data.csv', sep=';'):
    file = open(filename, 'r' )
    lines = file.readlines()
    res =[[] for i in lines[0].split(';')]
    for line in lines[1:]:
        l = line.split(';')
        for i in range(len(res)):
            res[i].append(float(l[i]))
            
    return res
def readVector():
    t, x, y, z, *r = readCsv()
    dt = [ t[i] - t[i-1] for i in range(len(t))]
    dt[0] = t[0]
    v = [np.array([x[i], y[i], z[i]]) for i in range(N)]
    return dt, v
a_dt, a = readVector("Accelerometer.csv")
w_dt, w = readVector("Gyroscope.csv")


