import datetime
import random
import time


def main():
    file = open("listofAccessTiming.xml", "w")
    file.write('<?xml version ="1.0" encoding ="UTF-8" standalone="no" ?>\n')
    file.write('<Plot title = "Average List Element Access Time">\n')
    

    xmin = 1000
    xmax = 200000

    xList = []
    yList = []

    

    for x in range(xmin, xmax+1, 1000):
        xList.append(x)
        prod = 0

        lst = [0] * x
        time.sleep(1)
        
        starttime = datetime.datetime.now()

        for v in range(1000):
            index = random.randint(0, x-1)
            val = lst[index]
            prod = prod * val


        endtime = datetime.datetime.now()
        deltaT = endtime - starttime

        accessTime = deltaT.total_seconds() * 1000

        yList.append(accessTime)

    file.write('    <Axes>\n')
    file.write('    <XAxis min= "' + str(xmin)+ '" max="' +str(xmax) + '">List Size </XAxis>\n')
    file.write('    <XAxis min= "' + str(min(yList))+ '" max="' +str(60) + '">Microseconds</YAxis>\n')
    file.write('    </Axes>\n')

    file.write('    <Sequence title="Average Access Time vs List Size" color ="red">\n')

    for i in range(len(xList)):
        file.write('    <DataPoint x="' + str(xList[i]) + '" y="' + str(yList[i])+ '"/>\n')

    file.write('    </Sequence>\n')

    #Testing for 200 000 elements 

    xList = lst
    yList = [0]*200000
    time.sleep(2)


    for i in range(100):
        starttime = datetime.datetime.now()

        index = random.randint(0,200000-1)
        xList[index] = xList[index] + 1
        
        endtime = datetime.datetime.now()
        deltaT = endtime-starttime

        yList[index] = yList[index] + deltaT.total_seconds()*1000000

        file.write('    <Sequnece Title = "Access Time Distribution" color = "blue">\n')

        for i in range(len(xList)):
            if xList[i] > 0:
                file.write('    <DataPoint x="' + str(i)+ '" y= "' + str(yList[i]/xList[i])+ '" />')

        file.write('    </Sequence>\n')
        file.write('    </Plot>\n')
        file.close()

if __name__ == "__main__":
    main()


