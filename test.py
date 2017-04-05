from gst import *
tomo=gst(['Gi'])
tomo.read_data('data.txt')
print(tomo)
print("")
print(tomo.get_feducials())
print("")
print(tomo.get_exp_data())
