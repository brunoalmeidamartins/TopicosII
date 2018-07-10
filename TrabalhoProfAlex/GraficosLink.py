import matplotlib.pyplot as plt
import commands
import time

i = 0
tempo =600

x=list()
y1 = list()
y2 = list()
y3 = list()
y4 = list()
y5 = list()
y6 = list()

plt.ion() #Turn interactive mode on

fig = plt.figure()
rect = fig.patch
rect.set_facecolor('#31312e')

ax1 = fig.add_subplot(1,1,1, axisbg='grey')


while i <tempo:
    #S3 {1,6,2}
    tx311=int(commands.getoutput("ovs-ofctl dump-ports s3 11 | grep tx | awk -F= '{print $2}' | awk -F, '{print $1}'"))
    rx311=int(commands.getoutput("ovs-ofctl dump-ports s3 11 | grep rx | awk -F= '{print $2}' | awk -F, '{print $1}'"))

    tx314=int(commands.getoutput("ovs-ofctl dump-ports s3 14 | grep tx | awk -F= '{print $2}' | awk -F, '{print $1}'"))
    rx314=int(commands.getoutput("ovs-ofctl dump-ports s3 14 | grep rx | awk -F= '{print $2}' | awk -F, '{print $1}'"))

    tx312=int(commands.getoutput("ovs-ofctl dump-ports s3 12 | grep tx | awk -F= '{print $2}' | awk -F, '{print $1}'"))
    rx312=int(commands.getoutput("ovs-ofctl dump-ports s3 12 | grep rx | awk -F= '{print $2}' | awk -F, '{print $1}'"))

    #s2 {4,3}
    tx211=int(commands.getoutput("ovs-ofctl dump-ports s2 11 | grep tx | awk -F= '{print $2}' | awk -F, '{print $1}'"))
    rx211=int(commands.getoutput("ovs-ofctl dump-ports s2 11 | grep rx | awk -F= '{print $2}' | awk -F, '{print $1}'"))

    tx214=int(commands.getoutput("ovs-ofctl dump-ports s2 14 | grep tx | awk -F= '{print $2}' | awk -F, '{print $1}'"))
    rx214=int(commands.getoutput("ovs-ofctl dump-ports s2 14 | grep rx | awk -F= '{print $2}' | awk -F, '{print $1}'"))

    #s1 {5}
    tx114=int(commands.getoutput("ovs-ofctl dump-ports s1 14 | grep tx | awk -F= '{print $2}' | awk -F, '{print $1}'"))
    rx114=int(commands.getoutput("ovs-ofctl dump-ports s1 14 | grep rx | awk -F= '{print $2}' | awk -F, '{print $1}'"))

    x.append(i)
    y1.append(tx311+rx311)
    y2.append(tx314+rx314)
    y3.append(tx214+rx214)
    y4.append(tx211+rx211)
    y5.append(tx114+rx114)
    y6.append(tx312+rx312)

    ax1.plot(x,y1,'c',linewidth=3.3,linestyle='-', label='Link1')
    ax1.plot(x,y2,'red',linewidth=3.3,linestyle='-', label='Link2')
    ax1.plot(x,y3,'green',linewidth=3.3,linestyle='-', label='Link3')
    ax1.plot(x,y4,'blue',linewidth=3.3,linestyle='-', label='Link4')
    ax1.plot(x,y5,'yellow',linewidth=3.3,linestyle='-', label='Link5')
    ax1.plot(x,y6,'gray',linewidth=3.3,linestyle='-', label='Link6')
    #ax1.plot(x1,y1,'r',linewidth=2.5,linestyle='--', label='Teste2')
    if i == 0:
        ax1.legend(loc='lower right') #"upper left" Esqueda Cima

    ax1.tick_params(axis='x', colors='c')
    ax1.tick_params(axis='y', colors='c')
    ax1.spines['bottom'].set_color('w')
    ax1.spines['top'].set_color('w')
    ax1.spines['left'].set_color('w')
    ax1.spines['right'].set_color('w')
    ax1.yaxis.label.set_color('c')
    ax1.xaxis.label.set_color('c')

    ax1.set_title('Links', color='c')
    ax1.set_xlabel('Tempo (s)')
    ax1.set_ylabel('Pacotes')

    plt.show()
    plt.pause(0.0001)
    i+=1
    time.sleep(1)
