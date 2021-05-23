import csv
import os
import random
ip_list = []
dict_check_most = {}
the_range = int(input("Enter Range Of Ip To Generate: "))
for i in range(the_range):
    first = random.randint(1, 254)
    second = random.randint(0, 254)
    third = random.randint(0, 254)
    forth = random.randint(0, 254)
    ip = str(first) + "." + str(second) + "." + str(third) + "." + str(forth)
    ip_list.append(ip)
csv_file = open("The_IPs.csv", "w")
writer = csv.writer(csv_file)
writer.writerow(ip_list)
csv_file.close()
ips = open("The_IPs.csv", "r")
for one in ips:
    the_ip = one.split(',')
    for i in the_ip:
        value = the_ip.count(i)
        key = i.strip("\n")
        dict_check_most[key] = value
    break
sorted(dict_check_most, key=dict_check_most.get, reverse=True)
count = 0
for key, value in dict_check_most.items():  #accessing values
    print(str(key) + " In There: " + str(value) + " Times" )
    count += 1
    if count == 3:
        break
