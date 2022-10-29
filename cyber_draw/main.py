import argparse
from cyber_record.record import Record
from cyber_draw.draw import draw_line, show
from cyber_draw.data_classes import * 


def draw_path(line):
   draw_line(line, has_color=True)
   show()

def read_path_chassis(filename):
   total_line = []
   canbus_chassis_line = apollo_canbus_chassis_data()
   control_line = apollo_control_data()

   record = Record(filename)
   for topic, msg, t in record.read_messages('/apollo/canbus/chassis'):
      timestamp = msg.header.timestamp_sec
      canbus_chassis_line.add_brake_percentage(msg.brake_percentage, timestamp)
      canbus_chassis_line.add_speed_mps(msg.speed_mps, timestamp)
      canbus_chassis_line.add_steering_percentage(msg.steering_percentage, timestamp)
      canbus_chassis_line.add_throttle_percentage(msg.throttle_percentage, timestamp)

   for topic, msg, t in record.read_messages('/apollo/control'):
      timestamp = msg.header.timestamp_sec
      control_line.add_throttle(msg.throttle, timestamp)
      control_line.add_brake(msg.brake, timestamp)
      control_line.add_steering_rate(msg.steering_rate, timestamp)
      control_line.add_steering_target(msg.steering_target, timestamp)


   total_line.append(canbus_chassis_line.generate_lines())
   total_line.append(control_line.generate_lines())

   return total_line

def main():
   parser = argparse.ArgumentParser()
   parser.description='please input your record file location'
   parser.add_argument("-f", "--file_name", help="this is your record file location", type=str)
   args = parser.parse_args()

   line = read_path_chassis(args.file_name)
   draw_path(line)
 

# if __name__ == "__main__":

#    parser = argparse.ArgumentParser()
#    parser.description='please input your record file location'
#    parser.add_argument("-f", "--file_name", help="this is your record file location", type=str)
#    args = parser.parse_args()

#    line = read_path_chassis(args.file_name)
#    draw_path(line)
