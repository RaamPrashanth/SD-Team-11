from model import Vh
from model import Vc
import csv
import constants
#reading
#input - csv files
#output -

#processing
#input -
#output - list of Vh, list of Vc both of size 40

#merging and generating csv
#input - list of Vh, list of Vc both of size 40
#output - csv file
output = Vh(1, 19.56165, 0, 9.29, 4, 1)
vhList = list()
vhList.append(output)
output = Vh(1, 16.48636, 0, 8.63, 4, 1)
vhList.append(output)
output = Vh(1, 19.95634, 1, 8.98, 3, 1)
vhList.append(output)

input = Vc(11.46408, 0.2665, 11.11, 4.025, 0.1825, 0.30355, 0.600525, 3.722925, 82.33)
vcList = list()
vcList.append(input)
input = Vc(18.1229, 0.1851, 10.83323, -12.47, 0.185525, 0.03245, -0.153975, 3.9523, 83.419)
vcList.append(input)
input = Vc(19.17278, 0.31885, 18.110, -7.9525, 0.23095, 0.010425, 0.130175, 1.218, 19.7908)
vcList.append(input)

with open('output.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL)
    wr.writerow([' ',constants.VELOCITY, constants.LANE_POS, constants.SPEED, constants.STEER, constants.ACCEL,
                  constants.BRAKE, constants.LONG_ACCEL, constants.HEADWAY_TIME, constants.HEADWAY_DIST, constants.USER, constants.MODE,
                  constants.SPEED, constants.NOE, constants.RESPONSE_TIME, constants.NOS])
    i=0;
    for vc, vh in zip(vcList, vhList):
        wr.writerow([i,vc.velocity, vc.lanepos, vc.speed, vc.steer, vc.accel, vc.brake, vc.longAccel, vc.headwayTime, vc.headwayDist,
                     vh.student, vh.mode, vh.speed, vh.noe, vh.responseTime, vh.nos])
        i += 1

