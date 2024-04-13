import sys 
secret_code, place, time = sys.stdin.readline().strip().split()

class Zero:
    def __init__(self, secret_code, place, time):
        self.secret_code = secret_code
        self.place = place
        self.time = int(time)

test = Zero(secret_code, place, time)
print("secret code :", test.secret_code)
print("meeting point :", test.place)
print("time :", test.time)