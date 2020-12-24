import socket, pickle

s = socket.socket()
s.bind(('', 12600))
s.listen(5)

c, addr = s.accept()

while True:
    msg = c.recv(4096)
    time_ms, lon, lat, slick_quantity, lon_vel, lat_vel, prediction = pickle.loads(msg)

    print("Time: ", time_ms)
    print("GPS: ", lon, lat)
    print("Pollution quantity: ",slick_quantity)
    print("Slick velocity: ", lon_vel, lat_vel)
    print("Predicted: ", prediction)
    print("\n")

c.close()
s.close()
