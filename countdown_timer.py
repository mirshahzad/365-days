# This program shows the Countdown Timer function

# importing time module
import time

# defining countdown function with user_time argument
def countdown(user_time):
    while user_time >= 0:
        mins, secs = divmod(user_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        user_time -= 1
    print('Lift off!')

if __name__ == '__main__':
    user_time = int(input("Enter a time in seconds: "))
    countdown(user_time)