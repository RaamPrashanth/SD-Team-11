class Vh:
    def __init__(self, mode, speed, noe, responseTime, nos, student):
        self.mode = mode
        self.speed = speed
        self.noe = noe
        self.responseTime = responseTime
        self.nos = nos
        self.student = student


class Vc:
    def __init__(self, velocity=0, lanepos=0, speed=0, steer=0, accel=0, brake=0, long_accel=0, headway_time=0,
                 headway_dist=0):
        self.velocity = velocity
        self.lanepos = lanepos
        self.speed = speed
        self.steer = steer
        self.accel = accel
        self.brake = brake
        self.longAccel = long_accel
        self.headwayTime = headway_time
        self.headwayDist = headway_dist

    def __add__(self, vc1):
        return Vc(self.velocity + vc1.velocity, self.lanepos + vc1.lanepos, self.speed + vc1.speed
                  , self.steer + vc1.steer, self.accel + vc1.accel, self.brake + vc1.brake
                  , self.longAccel + vc1.longAccel
                  , self.headwayTime + vc1.headwayTime, self.headwayDist + vc1.headwayDist)

    def __div__(self, value):
        return Vc(self.velocity / value, self.lanepos / value, self.speed / value
                  , self.steer / value, self.accel / value, self.brake / value
                  , self.longAccel / value, self.headwayTime / value, self.headwayDist / value)
