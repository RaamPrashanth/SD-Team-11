class Vh:
    def __init__(self, mode, speed, noe, responseTime, nos, student):
        self.mode = mode
        self.speed = speed
        self.noe = noe
        self.responseTime = responseTime
        self.nos = nos
        self.student = student

class Vc:
    def __init__(self, velocity, lanepos, speed, steer, accel, brake, longAccel, headwayTime, headwayDist):
        self.velocity = velocity
        self.lanepos = lanepos
        self.speed = speed
        self.steer = steer
        self.accel = accel
        self.brake = brake
        self.longAccel = longAccel
        self.headwayTime = headwayTime
        self.headwayDist = headwayDist
