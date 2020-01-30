import requests
import smtplib
import time

with open("essay.txt", "r") as file:
    # file.write("\n test est est today is the day")
    x = 0
    while x <= 5:
        x += 1
        print(f"line {x}: {file.readline()}")
        #sleep for short periods in general.
        time.sleep(2)
        #input("[press enter]")

    # for x in file:
    #     print(x)
    #     input(">")  # Press enter to continue
    # Read 5 lines from a file
