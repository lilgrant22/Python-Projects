

import csv, math, os

# Phase 1 - Write data to a file
file_path = os.path.join("data", "complexity.csv")
with open(file_path, 'wt') as file:
    writer = csv.writer(file)
    for i in range(1, 20):
        writer.writerow([i, i*i, i*i*i, math.pow(2, i), math.log(i), math.log(i)*i])



# Phase 2 - Read the complexity data from a file
n=[]
n2=[]
n3=[]
nexp = []
logn = []
nlogn= []
with open(file_path, "rt") as file:
    reader = csv.reader(file)
    for line in reader:
        n.append(float(line[0]))
        n2.append(float(line[1]))
        n3.append(float(line[2]))
        nexp.append(float(line[3]))
        logn.append(float(line[4]))
        nlogn.append(float(line[5]))


#Phase 3 Visualization
import matplotlib.pyplot as plt
fig = plt.figure()
plt.xkcd()  # Fun style after PCSE's favorite cartoonist (Alumni Randall Monroe)
plt.plot(n,n,'r.', label='linear')
plt.plot(n,n2,'g*:', label='n^2')
plt.grid()
plt.legend()
plt.title('Complexity Plot')
fig.savefig("data/plot_squared.png")
# plt.plot(n,logn,label='log(n)')
# plt.plot(n,nlogn,label='n log(n)')
# plt.legend()
# fig.savefig("data/plot_log.png")
# # plt.plot(n, n3,  label='n^3')  # Start with simple data, then add in full complexity, then limit range
# # plt.plot(n, nexp,label='2^n')
# # fig.savefig("data/plot_complexity.png")
plt.grid()
plt.legend()
plt.show()
#
