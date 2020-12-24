import socket, pickle, time

s = socket.socket()
s.connect(("localhost", 12600))

while True:
    time_ms = 0
    lon, lat = 0, 0
    slick_quantity = 0
    lon_vel, lat_vel = 0, 0
    prediction = 0

    msg = (time_ms, lon, lat, slick_quantity, lon_vel, lat_vel, prediction)

    data_string = pickle.dumps(msg)

    s.send(data_string)
    time.sleep(1)
 
s.close()
