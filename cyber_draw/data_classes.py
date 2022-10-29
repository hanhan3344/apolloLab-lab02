class Point:
   def __init__(self, x=None, y=None):
      self.x = x
      self.y = y

   def __str__(self):
      return "{},{}".format(self.x, self.y)



class apollo_canbus_chassis_data:
    def __init__(self):
        # self.engine_started = []
        self.speed_mps = []
        self.throttle_percentage = []
        self.brake_percentage = []
        self.steering_percentage = []
        # self.parking_brake = []
        # self.driving_mode = []
        # self.header = []
        # self.timestamp_sec = []

    # def add_engine_started(self, engine_started, timestamp_sec):
    #    self.engine_started.append(Point(timestamp_sec, engine_started))
   
    def add_speed_mps(self, speed_mps, timestamp_sec):
        self.speed_mps.append(Point(timestamp_sec, speed_mps))
   
    def add_throttle_percentage(self, throttle_percentage, timestamp_sec):
        self.throttle_percentage.append(Point(timestamp_sec, throttle_percentage))

    def add_brake_percentage(self, brake_percentage, timestamp_sec):
        self.brake_percentage.append(Point(timestamp_sec, brake_percentage))

    def add_steering_percentage(self, steering_percentage, timestamp_sec):
        self.steering_percentage.append(Point(timestamp_sec, steering_percentage))

    # def add_parking_brake(self, parking_brake, timestamp_sec):
    #    self.parking_brake.append(Point(timestamp_sec, parking_brake))

    # def add_driving_mode(self, driving_mode, timestamp_sec):
    #    self.driving_mode.append(Point(timestamp_sec, driving_mode))

    # def add_header(self, header, timestamp_sec):
    #    self.header.append(Point(timestamp_sec, header))
    def generate_lines(self):
        res = []
        res.append(self.speed_mps)
        res.append(self.throttle_percentage)
        res.append(self.brake_percentage)
        res.append(self.steering_percentage)

        return res

class apollo_control_data:
    def __init__(self):
        self.throttle = []
        self.brake = []
        self.steering_rate = []
        self.steering_target = []


    def add_throttle(self, throttle, timestamp_sec):
        self.throttle.append(Point(timestamp_sec, throttle))
   
    def add_brake(self, brake, timestamp_sec):
        self.brake.append(Point(timestamp_sec, brake))

    def add_steering_rate(self, steering_rate, timestamp_sec):
        self.steering_rate.append(Point(timestamp_sec, steering_rate))

    def add_steering_target(self, steering_target, timestamp_sec):
        self.steering_target.append(Point(timestamp_sec, steering_target))

    def generate_lines(self):
        res = []
        res.append(self.throttle)
        res.append(self.brake)
        res.append(self.steering_rate)
        res.append(self.steering_target)

        return res