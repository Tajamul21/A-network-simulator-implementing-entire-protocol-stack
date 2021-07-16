import random
import time

import urllib3


class EndDevice:

    def Generate_mac_address():
        mac_addresss = [str(random.randint(0x00, 0xFF)) for x in range(5)]
        return ("00:" + ":".join(mac_addresss))
    """GENERATES RANDOM MAC ADDRESS ANS ASSIGNS TO END-DEVICES"""


    def __init__(self, i,p,d,s):
        self.ip = ""
        self.mac = EndDevice.Generate_mac_address()
        self.port = p
        self.data = d
        self.seq_no = s
        self.subnet = ""
        self.gateway = ""
        self.dynamic = 0
        self.message= ""


    def display(Gen):
        print("ip address is " + str(Gen.ip))
        print("mac address is " + EndDevice.Generate_mac_address() )
        print("port value = " + str(Gen.port))


e1 = EndDevice("192.168.0.10", 0, "No data", 1)
e2 = EndDevice("192.168.0.11", 0, "No data", 2)
e3 = EndDevice("192.168.0.12", 0, "No data", 3)
e4 = EndDevice("192.168.0.13", 0, "No data", 4)
e5 = EndDevice("192.168.0.14", 0, "No data", 5)
e6 = EndDevice("192.168.0.15", 0, "No data", 6)
e7 = EndDevice("192.168.0.16", 0, "No data", 7)
e8 = EndDevice("192.168.0.17", 0, "No data", 8)
e9 = EndDevice("192.168.0.18", 0, "No data", 9)
e10 = EndDevice("192.168.0.19", 0, "No data", 10)


endDevices = [-1, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
processes = [1, 2, 3]


def End_Device_Vacant():
    eport = [e1.port, e2.port, e3.port, e4.port, e5.port, e6.port, e7.port, e8.port, e9.port, e10.port]
    for i in range(0, 11):
        if eport[i] == 0:
            return 0
        else:
            return 1
    """CHECKS IF END-DEVICE IS VACANT OR NOT"""


class Hub:
    def __init__(self):
       self.port1 = 0
       self.port2 = 0
       self.port3 = 0
       self.port4 = 0
       self.port5 = 0
       self.port6 = 0
    def Hub_vacant(self):
        plist = [self.port1, self.port2, self.port3, self.port4, self.port5, self.port6]
        for i in range(0, 6):
            if plist[i] == 0:
                return 0
            else:
                return 1
    """CHECKS WHETHER HUB HAS ANY PORT VACANT OR NOT"""


Hub1 = Hub()
Hub2 = Hub()


class Switch:

    def __init__(self):
        self.port1 = 0
        self.port2 = 0
        self.port3 = 0
        self.port4 = 0
        self.port5 = 0
        self.port6 = 0
        self.port7 = 0

    def Switch_vacant(self):
        slist = [self.port1, self.port2, self.port3, self.port4, self.port5, self.port6, self.port7]
        for i in range(0,8):
            if slist[i] == 0:
                return 0
            else:
                return 1
    """CHECKS WHETHER SWITCH HAS ANY PORT VACANT OR NOT"""

    maclist1 = [0, 0, 0, 0, 0]
    maclist2 = [0, 0, 0, 0, 0]
    """MAC ADDRESS LIST FOR ADDRESS LEARNING"""


Switch1 = Switch()

Switch2 = Switch()


class Router:

    def __init__(self):
        self.interface1 = []
        self.interface2 = []
        self.interface3 = []
        self.max_ex = 2;
        self.max_p = 2
        self.max_conf = 2
        self.max_i1 = 1
        self.max_i2 = 1
        self.max_i3 = 1
        self.flag = 0

    def user_executive_mode(self):


        print("User Executive mode")
        user = str(input())
        if user == "en" or user == "enable":
            self.privilegde_mode()

        user = str(input())
        if user == "ex":
            return




    def privilegde_mode(self):


        print("Priviledge mode")
        while (True):
            user = str(input())
            if user == "ex" or user == "exit":

                print("User Executive Mode")
                break
            elif user == "conf t" or user == "configure terminal":
                self.global_conf()
            elif user == 'write memory':
                print("Settings Saved")
            elif user == 'showip route':
                Router1.R_table
            else:
                print("Invalid Command")

    def global_conf(self):

        while (True):
            print("Global Configuration Mode")
            user = str(input())
            if user == 'ex' or user == 'exit':

                print("Privilege Mode")
                return

            elif user == "int 1":
                self.Interface1()
            elif user == "int 2":
                self.Interface2()
            elif user == "int 3":
                self.Interface3()

            # default routing
            elif user == 'iproute 0.0.0.0 0.0.0.0 ipaddress main router':
                Router1.R_table

            # static routing
            elif user == 'iproute 10.0.0.0 255.255.255.0 20.0.0.3':
                routing(Router1)

            # dynamic routing
            elif user == 'router rip':
                RIP()
                print("Enter IP of Directly connected neighbours")
                user1 = str(input())
                if user1 == 'network':
                    print("Implementing rip on first one")
                    print("Implementing rip on second one")
            else:
                print("Invalid command!")

    def Interface1(self):
        while (True):
            user = str(input())
            if user == 'ip address':
                print("Enter  Ip address")
                user1 = str(input())
                self.interface1.append(user1)
                print("Enter  Network bits")
                user2 = str(input())
                self.interface1.append(user2)

                # Assigning IP
            elif user == "noshutdown":
                print("No shutdown")
            elif user == "ex":
                return
            else:
                print("Invalid Command")

    def Interface2(self):
        while (True):
            user = str(input())
            if user == 'ip address':
                print("Enter  Ip address")
                user1 = str(input())
                self.interface2.append(user1)
                print("Enter  Network bits")
                user2 = str(input())
                self.interface2.append(user2)


                # Assigning IP
            elif user == "noshutdown":
                print("No shutdown")
            elif user == "ex":
                self.global_conf()
                break
            else:
                print("Invalid Command")

    def Interface3(self):
        while (True):
            user = str(input())
            if user == 'ip address':
                print("Enter  Ip address")
                user1 = str(input())
                self.interface3.append(user1)
                print("Enter  Network bits")
                user2 = str(input())
                self.interface3.append(user2)

                # Assigning IP
            elif user == "noshutdown":
                print("No shutdown")
            elif user == "ex":
                self.global_conf()
                break
            else:
                print("Invalid Command")

    R_table = []



Router1 = Router()

Router2 = Router()

Router3 = Router()






"""-------------------------------------------------SERVER----------------------------------------------------"""






class Server:

    def __init__(self,n, p,s,ip):
        self.name = n
        self.port = p
        self.ip = ip
        self.mac = EndDevice.Generate_mac_address()
        self.seq_no = s
        self.message = ""


HTTP = Server("http", 80, 1, "10.0.0.6")
SSH = Server("ssh", 22, 2, "20.0.0.6")
SMTP = Server("smtp", 25, 3, "30.0.0.6")
s_list = [HTTP, SSH, SMTP]



def messtrf(message, endD, server):
    server.message = message

"""-----------------------------------------------UDP--------------------------------------------------------"""

def udp(n, p, ip, e, m):
    for i in s_list:
        if n == i.name:
            if ip == i.ip and p == i.port:
                x = random.randint(0, 10)
                if x >= 8:
                    messtrf(m, e, i)
                    print(i.message)
                    return
                else:
                    print("Packed got dropped because of unreliability of UDP")
                    return
            else:
                print("port or ip does not matched")
                return
    print("Invalid Server!")



"""-----------------------------------------------------TCP-------------------------------------------------------"""


def tcp(n,p,ip,e,m):

    for i in s_list:
        if n == i.name:
            if ip == i.ip and p == i.port:
                buffer = m
                messtrf(buffer,e,i)
                print(i.message)
                return
            else:
                print("port or ip does not matched")
                return
    print("Invalid Server!")



'''-----------------------------------Conversion of IP and NID------------------------------------------------'''




def get_nid(ip_address, subnet):

    x = ""
    binary = ""
    for i in range(0, len(ip_address)):
        if ip_address[i] != '.':
            x = x + ip_address[i]
        else:
            binary = binary + bin(int(x))[2:].zfill(8)
            x = ""
        if i == len(ip_address) - 1 and ip_address[i] != '.':
            binary = binary + bin(int(x))[2:].zfill(8)

    s = ""
    for i in range (0, subnet):
        s = s + binary[i]

    for i in range (0, 32 - subnet):
        s = s + '0'

    return s

    #print("IP in binary : ", binary)
    #print("NID in binary : ", s)





"""---------------------------------------------PING--------------------------------------------------------"""




def ping(src, dest):



    if Router1.flag == 0 and num4 == 7:
        print("Timeout Occured")

    elif get_nid(endDevices[src].ip, endDevices[src].subnet) == get_nid(endDevices[dest].ip, endDevices[src].subnet):
        print("Searching the mac address of destination in ARP Cache...")
        print("Found the IP address in ARP Cache")
        for i in range(0, 4):
            print("Reply from : ", endDevices[dest].ip, "bytes=32 time<1ms TTL=128")

    else:
        print("Searching the mac address of destination in ARP Cache...")
        print("Couldn't Find the mac address of destination in the ARP Cache")
        print("Default Gateway is ", endDevices[src].gateway)
        for i in range(0, len(Router1.R_table)):
            if get_nid(endDevices[dest].ip, endDevices[dest].subnet) == get_nid(Router1.R_table[i][0], Router1.R_table[i][1]):
                print("Searching the mac address of destination in ARP Cache...")
                print("Found the IP address in ARP Cache")
                for i in range(0, 4):
                    print("Reply from : ", endDevices[dest].ip, "bytes=32 time<1ms TTL=128")
                return

        print("New Timeout occurred")






"""------------------------------------Routing----------------------------------------------------------------------"""





def routing(router):

    list = [get_nid(endDevices[1].ip, endDevices[1].subnet), endDevices[1].subnet, router.interface1[0]]
    router.R_table.append(list)
    list = [get_nid(endDevices[2].ip, endDevices[2].subnet), endDevices[2].subnet, router.interface2[0]]
    router.R_table.append(list)




"""-------------------------------------------------RIP------------------------------------------------------"""




def RIP():

    temp1 = []
    temp2 = []
    temp3 = []
    temp1 = Router1.R_table
    Router1.flag = 1
    temp2 = Router2.R_table
    temp3 = Router3.R_table

    for i in range(0, 5):
        if Router1.R_table[i][4] > 1 + temp2[i][4]:
            Router1.R_table[i][4] = 1 + temp2[i][4]
            Router1.R_table[i][3] = "40.0.0.2"

        if Router1.R_table[i][4] > 1 + temp3[i][4]:
            Router1.R_table[i][4] = 1 + temp3[i][4]
            Router1.R_table[i][3] = "30.0.0.2"

        if Router2.R_table[i][4] > 1 + temp1[i][4]:
            Router2.R_table[i][4] = 1 + temp1[i][4]
            Router2.R_table[i][3] = "40.0.0.1"

        if Router2.R_table[i][4] > 1 + temp3[i][4]:
            Router2.R_table[i][4] = 1 + temp3[i][4]
            Router2.R_table[i][3] = "50.0.0.1"

        if Router3.R_table[i][4] > 1 + temp1[i][4]:
            Router3.R_table[i][4] = 1 + temp1[i][4]
            Router3.R_table[i][3] = "30.0.0.1"

        if Router3.R_table[i][4] > 1 + temp2[i][4]:
            Router3.R_table[i][4] = 1 + temp2[i][4]
            Router3.R_table[i][3] = "50.0.0.2"

    print(*Router1.R_table, sep = "\n")




"""----------------------------------------------DHCP--------------------------------------------------------"""

def DHCP(enddevice):

    if enddevice == 1 or enddevice == 2 or enddevice == 3:
        ran = random.randint(2, 254)
        r = str(ran)
        p = ""
        dots = 0
        for i in Router1.interface1[0]:
            if i == '.':
                dots = dots + 1
            if dots >= 3:
                p=p+i
                break
            else:
                p = p + i
        p = p + r
        print("The generated address is ", p)

    else:
        ran = random.randint(2, 254)
        r = str(ran)
        p = ""
        dots = 0
        for i in Router1.interface2[0]:
            if i == '.':
                dots = dots + 1
            if dots >= 3:
                p=p+i
                break
            else:
                p = p + i
        p = p + r
        print("The generated address is ", p)




"""-----------------------------------------------------HTTP------------------------------------------"""

def HTTP():


    http = urllib3.PoolManager()

    resp = http.request('GET', 'http://tutorialspoint.com/robots.txt')
    print(resp.data)

    # get the status of the response
    print(resp.status)


"""-----------------------------FLOW CONTROL PROTOCOL: STOP AND WAIT ARQ------------------------------------"""





def stop_and_wait_arq_HUb(a, b, c):

    sender = 0
    receiver = 0
    s = 0
    ack = 0
    for i in range(0, len(c)):
        if i % 2 == 0:
            s = 0
            ack = 1
        else:
            s = 1
            ack = 0
        c1 = Switch1.maclist1.count(endDevices[b].mac)
        c2 = Switch1.maclist2.count(endDevices[b].mac)
        if c1 == 0 and c2 == 0:
            print("Mac Address of End Device", b, "not found in the MAC table")
            print("Switch will broadcast the message\n")

            if i != 0 and i % 4 == 0:
                print("Time out occurred, Sending the", i, "th frame again. Sequence number :", s)
            print("Sending First packet  -----", c[0], "-----")
            for j in range(1, 11):
                if j != a:
                    endDevices[j].data = c[i]
                    print("Message sent to End Device", j)
                if j == b:
                    print("Ack received by End Device", b, "ACK NO :", ack)
            print("\n")
            if a < 6:
                Switch1.maclist1[a - 1] = endDevices[a].mac
            else:
                Switch1.maclist2[a - 6] = endDevices[a].mac
            if b < 6:
                Switch1.maclist1[b - 1] = endDevices[b].mac
            else:
                Switch1.maclist2[b - 6] = endDevices[b].mac
        else:
            if (a < 6 and b < 6):
               print("Mac Address found, Both Devices in Hub 1")
               print("Sending  packet -----", c[i], "-----")
               if i != 0 and i % 4 == 0:
                  print("Time out occurred, Sending the", i, "th frame again. Sequence number :", s)
               for j in range(1, 6):
                    if j != a:
                       endDevices[j].data = c[i]
                       print("Message sent to End Device", j)
                    if j == b:
                       print("Ack received by End Device", b, "ACK NO :", ack)
               print("\n")
            elif a > 6 and b > 6:
                print("Mac Address found, Both Devices in Hub 2")
                print("Sending  packet -----", c[i], "-----")
                if i != 0 and i % 4 == 0:
                    print("time out occurred, Sending the", i, "th frame again. Sequence number :", s)
                for j in range(6, 11):
                    if j != a:
                        endDevices[j].data = c[i]
                        print("Message sent to End Device", j)
                    if j == b:
                        print("Ack received by End Device", b, "ACK NO :", ack)
                print("\n")
            else:
                print("Mac Address of End Device", b, "  found in the MAC table")
                print("Sending  packet -----", c[i], "-----")
                print("Sending to other port")
                if i != 0 and i % 4 == 0:
                    print("time out occurred, Sending the", i, "th frame again. Sequence number :", s)
                for j in range(1, 11):
                    if j != a:
                        endDevices[j].data = c[i]
                        print("Message sent to End Device", j)
                    if j == b:
                        print("Ack received by End Device", b, "ACK NO :", ack)
                print("\n")
                if a < 6:
                    Switch1.maclist1[a - 1] = endDevices[a].mac
                else:
                    Switch1.maclist2[a - 6] = endDevices[a].mac
                if b < 6:
                    Switch1.maclist1[b - 1] = endDevices[b].mac
                else:
                    Switch1.maclist2[b - 6] = endDevices[b].mac



def stop_and_wait_arq(a, b, c):

    sender = 0
    receiver = 0
    s = 0
    ack = 0
    for i in range(0, len(c)):
        if i % 2 == 0:
            s = 0
            ack = 1
        else:
            s = 1
            ack = 0
        c1 = Switch1.maclist1.count(endDevices[b].mac)
        if c1 == 0:
            print("Mac Address of End Device", b, "not found in the MAC table")
            print("Switch will broadcast the message\n")
            print("Sending  packet -----", c[i], "-----")
            if i != 0 and i % 4 == 0:
                print("time out occurred, Sending the", i, "th frame again. Sequence number :", s)
            for j in range(1, 6):
                if j != a:
                    endDevices[j].data = c[i]
                    print("Message sent to End Device", j)
                if j == b:
                    print("Ack received by End Device", b, "ACK NO :", ack)
            print("\n")
            Switch1.maclist1[a - 1] = endDevices[a].mac
            Switch1.maclist1[b - 1] = endDevices[b].mac


        else:
                print("Mac Address of End Device", b, "found in the MAC table")
                print("Sending  packet -----", c[i], "-----")
                if i != 0 and i % 4 == 0:
                    print("time out occurred, Sending the", i, "th frame again. Sequence number :", s)
                print("Message sent to End Device", b)
                print("ACK received from End Device ", b)
                print("\n")
                Switch1.maclist1[a - 1] = endDevices[a].mac
                Switch1.maclist1[b - 1] = endDevices[b].mac






"""-----------------------------FLOW CONTROL PROTOCOL: SELECTIVE REPEAT------------------------------------"""






def Selective_Repeat_Hub(a,b,c):

    print("Enter the reserved bit size for Seq no")
    m = int(input())
    sf = 0
    sn = 0
    x = len(c)
    Window_Size = 2**(m-1)
    Seq_no = 2**m
    array = [0]*x
    visited = [0]*x
    while x != 0:
        marker = 0
        while sn < sf + Window_Size and sn < len(c):
          if array[sn] == 0:
            if sn % 3 == 0 and visited[sn] == 0:
                    print(sn, "-th packet lost, Sending next packet\n")
                    visited[sn] = 1
                    if marker == 0:
                      sf = sn
                      marker = marker + 1
            else:
                array[sn] = 1

                c1 = Switch1.maclist1.count(endDevices[b].mac)
                c2 = Switch1.maclist2.count(endDevices[b].mac)
                if c1 == 0 and c2 == 0:
                    print("Mac Address of End Device", b, "not found in the MAC table")
                    print("Switch will broadcast the message\n")
                    print("Sending  packet -----", c[sn], "-----")
                    for j in range(1, 11):
                        if j != a:
                            endDevices[j].data = c[sn]
                            print("Message sent to End Device", j)
                        if j == b:
                            print("Ack received by End Device", b, "ACK NO :", sn%Seq_no)
                    print("\n")
                    if a < 6:
                        Switch1.maclist1[a - 1] = endDevices[a].mac
                    else:
                        Switch1.maclist2[a - 6] = endDevices[a].mac
                    if b < 6:
                        Switch1.maclist1[b - 1] = endDevices[b].mac
                    else:
                        Switch1.maclist2[b - 6] = endDevices[b].mac
                else:
                    if (a < 6 and b < 6):
                        print("Mac Address found, Both Devices in Hub 1")
                        print("Sending  packet -----", c[sn], "-----")
                        for j in range(1, 6):
                            if j != a:
                                endDevices[j].data = c[sn]
                                print("Message sent to End Device", j)
                            if j == b:
                                print("Ack received by End Device", b, "ACK NO :", sn%Seq_no)
                        print("\n")
                    elif a > 6 and b > 6:
                        print("Mac Address found, Both Devices in Hub 2")
                        print("Sending  packet -----", c[sn], "-----")
                        for j in range(6, 11):
                            if j != a:
                                endDevices[j].data = c[sn]
                                print("Message sent to End Device", j)
                            if j == b:
                                print("Ack received by End Device", b, "ACK NO :", sn%Seq_no)
                        print("\n")
                    else:
                        print("Mac Address of End Device", b, "found in the MAC table")
                        if sn != 0 and sn % 4 == 0:
                            print("time out occurred, Sending the", i, "th frame again. Sequence number :", sn%Seq_no)
                        print("Sending  packet -----", c[sn], "-----")
                        for j in range(1, 11):
                            if j != a:
                                endDevices[j].data = c[sn]
                                print("Message sent to End Device", j)
                            if j == b:
                                print("Ack received by End Device", b, "ACK NO :", sn % Seq_no)
                        print("\n")
                        if a > 5:
                           Switch1.maclist1[a - 6] = endDevices[a].mac
                        else:
                            Switch1.maclist1[a - 1] = endDevices[a].mac
                        if b > 5:
                            Switch1.maclist2[b - 6] = endDevices[b].mac
                        else:
                            Switch1.maclist2[b - 1] = endDevices[b].mac


                x = x - 1
                if sf == sn:
                   for i in range(sf, len(c)):
                       if array[i] == 0:
                           sf = i
                           sn = sf - 1
                           break
          sn = sn + 1
        if sn < len(c):
              print("Restart the timer, sending the outstanding packets again")
        sn = sf




def Selective_Repeat(a,b,c):

    print("Enter the reserved bit size for Seq no")
    m = int(input())
    sf = 0
    sn = 0
    x = len(c)
    Window_Size = 2**(m-1)
    Seq_no = 2**m
    array = [0]*x
    visited = [0]*x
    while x != 0:
        marker = 0
        while sn < sf + Window_Size and sn<len(c):
          if array[sn] == 0:
            if sn % 2 == 0 and visited[sn] == 0:
                    print(sn, "th packet lost, Sending next packet\n")
                    visited[sn] = 1
                    if marker == 0:
                      sf = sn
                      marker = marker + 1
            else:
                array[sn] = 1

                c1 = Switch1.maclist1.count(endDevices[b].mac)
                if c1 == 0:
                    print("Mac Address of End Device", b, "  not found in the MAC table")
                    print("Switch will Broadcast the message")
                    print("Sending  packet -----", c[sn], "-----")

                    for j in range(1, 6):
                        if j != a:
                            endDevices[j].data = c[sn]
                            print("Message sent to End Device", j)
                        if j == b:
                            print("Ack received by End Device", b, "ACK NO :", sn%Seq_no)
                    Switch1.maclist1[a - 1] = endDevices[a].mac
                    Switch1.maclist1[b - 1] = endDevices[b].mac

                else:
                           print("Mac Address of End Device", b, "found in the MAC table")
                           print("Sending  packet -----", c[sn], "-----")
                           if sn != 0 and sn % 4 == 0:
                               print("time out occurred, Sending the", sn, "th frame again.")
                           print("Message sent to End Device", b)
                           print("ACK received from End Device ", b)
                           print("\n")
                           Switch1.maclist1[a - 1] = endDevices[a].mac
                           Switch1.maclist1[b - 1] = endDevices[b].mac


                x = x - 1
                if sf == sn:
                   for i in range(sf, len(c)):
                       if array[i] == 0:
                           sf = i
                           sn = sf - 1
                           break
          sn = sn + 1
        if sn < len(c):
              print("Restart the timer, sending the outstanding packets again")
        sn = sf







""""----------------------------------------------------ACCESS CONTROL-----------------------------------------"""




end_Devices = [e1.seq_no, e2.seq_no, e3.seq_no, e4.seq_no, e5.seq_no, e6.seq_no, e7.seq_no, e8.seq_no, e9.seq_no, e10.seq_no]


def token_passing(token, num1):

    t = token
    s = num1
    if t == s:
        print("Sender has the access already!")
    elif t < s:
        print("End Device", t, "Has access ")
        print("------Passing the Token ")
        for i in end_Devices:
            #endDevices[i] = t
            print("End Device ", i+t, "Has access now")

            if s == i+t:
                print("----------------------------Access granted-----------------------------------")
                break
            if i != s:
                print("------Passing the Token ")
    else:
        print("End Device", t, "Has access ")
        print("------Passing the Token ")
        for i in endDevices:
            endDevices[i] = t
            print("End Device ", t-i, "Has access now")

            if s == t-i:
                print("----------------------------Access granted-----------------------------------")
                break
            if i != s:
                print("------Passing the Token ")





def collision_broadcast():
    if 1 == num4 or 2 == num4:
        print("Collision Domain : 1")
        print("Broadcast Domain : 1")
    elif 3 == num4 or 4 == num4:
        print("Collision Domain : 2")
        print("Broadcast Domain : 1")
    elif 5 == num4:
        print("Collision domain : 5")
        print("Broadcast Domain : 1")
    elif 6 == num4 :
        print("Collision Domain : 5")
        print("Broadcast Domain : 1")
    elif 7 == num4:
        print("Collision domain : 6")
        print("Broadcast Domain : 1")


"""-------------------------------------------------MENU---------------------------------------------------------"""

print("Following Simulations can be carried out. Enter the respective number of the simulation:")
print("1. Dedicated Link")
print("2. Simulation through Hub--------STAR TOPOLOGY------")
print("3. Simulation through Switch-----ADDRESS LEARNING---")
print("4. Complete Simulation --Implementing Access and Flow Control Protocols--")
print("5. Switch and 5 End Devices ")
print("6. EndDevice --- Switch---Router---Switch----EndDevice ")
print("7. Implementing RIP----end to end connection-----")
print("8. Process to process-Transport layer")
print("9. Application layer services")
num4 = int(input())



def Connections():

    if 1 == num4:

        print("Enter Sender Device no")
        num1 = int(input())
        print("Enter Receiver Device no")
        num2 = int(input())
        print("you have selected these two End Devices:", num1, "and", num2)
        if e1.port == e2.port:
           print("Enter the message to be transmitted")
           num3 = str(input())
           print("Message : ", num3)
           e1.data = num3
           print("Connection Made between two End devices")
           e1.port = 1
           e2.port = 2
           e2.data = e1.data
           print("Message sent successfully : ", num3)
           if e2.data == e1.data:
             print("                                                     ----ACK RECEIVED FROM END DEVICE", num2, "---")
           else:
             print("---ACK LOST---")

        else:
           print("No connection possible, already occupied")




    elif 2 == num4:

        print("Enter Sender Device no:")
        num1 = int(input())
        print("Enter Receiver Device no:")
        num2 = int(input())
        print("you have selected these two End Devices within same HUB:", num1, "and", num2)
        if End_Device_Vacant() == 0 and Hub1.Hub_vacant() == 0:
           print("Connection made between Sender-End device and HUB")
           e1.port = 1
           Hub1.port1 = 9
           if Hub1.port2 == 0 and Hub1.port3 == 0:
             print("Connection made between Hub and other End Devices")
             print("Enter the message")
             num3 = str(input())
             print("Message : ", num3)
             e1.data = num3
             e2.data = e1.data
             print("Message sent to End Device 2 successfully : ", e2.data)
             e3.data = e1.data
             print("Message sent to End Device 3 successfully : ", e3.data)
             e4.data = e1.data
             print("Message sent to End Device 4 successfully : ", e4.data)
             e5.data = e1.data
             print("Message sent to End Device 5 successfully : ", e5.data)
             e2.port = 7
             e3.port = 2
             e4.port = 5
             e5.port = 62
             Hub1.port2 = 5
             Hub1.port3 = 8
             Hub1.port4 = 4
             Hub1.port5 = 1
             if num2 == 2:
                 print("                                                     ---ACK RECEIVED  from End Device 2---")
             elif num2 == 3:
                 print("                                                     ---ACK RECEIVED  from End Device 3---")
             elif num2 == 4:
                 print("                                                     ---ACK RECEIVED  from End Device 4---")
             elif num2 == 5:
                 print("                                                     ---ACK RECEIVED  from End Device 5---")
             else:
                 print("ACK lost, no connection")
           else:
                 print("No Port vacant in HUB")
        else:
            print("---No port available in HUB---")





    elif 3 == num4:

        if Hub1.Hub_vacant() == 0 and Switch1.Switch_vacant() ==0 and Hub2.Hub_vacant() == 0:
            print("Connection made between --Hub1------Switch------Hub2-- ")
            Switch1.port1 = 2
            Hub1.port6 = 6
            Hub2.port6 = 4
            if End_Device_Vacant() == 0 and Hub1.Hub_vacant() == 0:
                print("......................HUB 1  CONNECTING.......................")

                print("Connection made between Hub1 and  End Device 1")
                e1.port = 1
                Hub1.port1 = 9
                if  Hub1.port2 == 0 and Hub1.port3 == 0 and Hub1.port4 == 0 and Hub1.port5 == 0:
                    print("Connection made between Hub1 and  End Device 2")
                    print("Connection made between Hub1 and  End Device 3")
                    print("Connection made between Hub1 and  End Device 4")
                    print("Connection made between Hub1 and  End Device 5")
                    e2.port = 7
                    e3.port = 2
                    e4.port = 8
                    e5.port = 1
                    Hub1.port2 = 5
                    Hub1.port3 = 8
                    Hub1.port4 = 52
                    Hub1.port5 = 80
                else:
                    print("No Port vacant in HUB")
            else:
                print("---No end device vacant---")


            if End_Device_Vacant() == 0 or Hub2.Hub_vacant() == 0:
                    print("......................HUB 2  CONNECTING.......................")
                    print("Connection made between Hub2 and  End Device 6")
                    e6.port = 1
                    Hub2.port1 = 9
                    if Hub2.port2 == 0 and Hub2.port3 == 0 and Hub2.port4 == 0 and Hub2.port5 == 0:
                        print("Connection made between Hub2 and  End Device 7")
                        print("Connection made between Hub2 and  End Device 8")
                        print("Connection made between Hub2 and  End Device 9")
                        print("Connection made between Hub2 and  End Device 10")
                        e7.port = 71
                        e8.port = 22
                        e9.port = 71
                        e10.port = 22
                        Hub2.port2 = 50
                        Hub2.port3 = 801
                        Hub2.port4 = 501
                        Hub2.port5 = 800
                    else:
                        print("No Port vacant in HUB")

            else:
                    print("---No end Device vacant---")

            print("Enter the message")
            num3 = str(input())
            print("Message : ", num3)
            e1.data = num3
            print(" Sender Device is 1" )
            print(" Receiver Device is 2")
            print("Searching for MAC address of End Device : 2 ")
            print("Mac Address of End Device 2 is =", e2.mac)
            for i in range(0,5):
                if Switch1.maclist1[i] == e2.mac:
                    print("MAC address found in MAC table within same port")
                    e2.data = e1.data
                    print("Message sent to End Device 2")
                    e3.data = e1.data
                    print("Message sent to End Device 3")
                    e4.data = e1.data
                    print("Message sent to End Device 4")
                    e5.data = e1.data
                    print("Message sent to End Device 5")

                    print("                                        ---ACK RECEIVED  from End Device 2---")
                    break
                if i == 4:
                    print("Mac Address of End Device 2 not found in the MAC table")
                    e2.data = e1.data
                    print("Message sent to End Device 2")
                    e3.data = e1.data
                    print("Message sent to End Device 3")
                    e4.data = e1.data
                    print("Message sent to End Device 4")
                    e5.data = e1.data
                    print("Message sent to End Device 5")
                    e6.data = e1.data
                    print("Message sent to End Device 6")
                    e7.data = e1.data
                    print("Message sent to End Device 7")
                    e8.data = e1.data
                    print("Message sent to End Device 8")
                    e9.data = e1.data
                    print("Message sent to End Device 9")
                    e10.data = e1.data
                    print("Message sent to End Device 10")

                    print("                                        ---ACK RECEIVED  from End Device 2---")

            Switch1.maclist1[0] = e1.mac
            Switch1.maclist1[1] = e2.mac

            print("Enter the message")
            num3 = str(input())
            print("Message : ", num3)
            e3.data = num3
            print(" Sender Device is 3")
            print(" Receiver Device is 2")
            print("Searching for MAC address of End Device : 2 ")
            print("Mac Address of End Device 2 is =", e2.mac)
            for i in range(0, 5):
                if Switch1.maclist1[i] == e2.mac:
                    print("MAC address found in MAC table within same port")
                    e2.data = e3.data
                    print("Message sent to End Device 1")
                    e1.data = e3.data
                    print("Message sent to End Device 2")
                    e4.data = e3.data
                    print("Message sent to End Device 4")
                    e5.data = e3.data
                    print("Message sent to End Device 5")

                    print("                                        ---ACK RECIEVED  from End Device 2---")
                    break
                if i == 4:
                    print("Mac Address of End Device 2 not found in the MAC table")
                    e2.data = e3.data
                    print("Message sent to End Device 1")
                    e1.data = e3.data
                    print("Message sent to End Device 3")
                    e4.data = e3.data
                    print("Message sent to End Device 4")
                    e5.data = e3.data
                    print("Message sent to End Device 5")
                    e6.data = e3.data
                    print("Message sent to End Device 6")
                    e7.data = e3.data
                    print("Message sent to End Device 7")
                    e8.data = e3.data
                    print("Message sent to End Device 8")
                    e9.data = e3.data
                    print("Message sent to End Device 9")
                    e10.data = e3.data
                    print("Message sent tp End Device 10")
                    print("                                        ---ACK RECIEVED  from End Device 2---")
            Switch1.maclist1[2] = e3.mac

            print("Enter the message")
            num3 = str(input())
            print("Message : ", num3)
            e1.data = num3
            print(" Sender Device is 1")
            print(" Receiver Device is 5")
            print("Searching for MAC address of End Device : 5 ")
            print("Mac Address of End Device 2 is =", e5.mac)
            for i in range(0, 5):
                if Switch1.maclist1[i] == e5.mac:
                    print("MAC address found in MAC table within same port")
                    e2.data = e1.data
                    print("Message sent to End Device 2")
                    e3.data = e1.data
                    print("Message sent to End Device 3")
                    e4.data = e1.data
                    print("Message sent to End Device 4")
                    e5.data = e1.data
                    print("Message sent to End Device 5")

                    print("                                            ---ACK RECEIVED  from End Device 5---")
                    break
                if i == 4:
                    print("Mac Address of End Device 5 not found in the MAC table")
                    e2.data = e1.data
                    print("Message sent to End Device 2")
                    e3.data = e1.data
                    print("Message sent to End Device 3")
                    e4.data = e1.data
                    print("Message sent to End Device 4")
                    e5.data = e1.data
                    print("Message sent to End Device 5")
                    e6.data = e1.data
                    print("Message sent to End Device 6")
                    e7.data = e1.data
                    print("Message sent to End Device 7")
                    e8.data = e1.data
                    print("Message sent to End Device 8")
                    e9.data = e1.data
                    print("Message sent to End Device 9")
                    e10.data = e1.data
                    print("Message sent to End Device 10")
                    print("                                           ---ACK RECEIVED  from End Device 5---")
            Switch1.maclist1[4] = e5.mac


            print("Enter the message")
            num3 = str(input())
            print("Message : ", num3)
            e1.data = num3
            print(" Sender Device is 1")
            print(" Receiver Device is 6")
            print("Searching for MAC address of End Device : 6 ")
            print("Mac Address of End Device 2 is =", e6.mac)
            for i in range(0, 5):
                if Switch1.maclist1[i] == e6.mac or Switch1.maclist2[i] == e6.mac:
                    print("MAC address found in MAC table in Different port")
                    e2.data = e1.data
                    print("Message sent to End Device 2")
                    e3.data = e1.data
                    print("Message sent to End Device 3")
                    e4.data = e1.data
                    print("Message sent to End Device 4")
                    e5.data = e1.data
                    print("Message sent to End Device 5")
                    e6.data = e1.data
                    print("Message sent to End Device 6")
                    e7.data = e1.data
                    print("Message sent to End Device 7")
                    e8.data = e1.data
                    print("Message sent to End Device 8")
                    e9.data = e1.data
                    print("Message sent to End Device 9")
                    e10.data = e1.data
                    print("Message sent to End Device 10")

                    print("                                       ---ACK RECEIVED  from End Device 6---")
                    break
                if i == 4:
                    print("Mac Address of End Device 6 not found in the MAC table")
                    e2.data = e1.data
                    print("Message sent to End Device 2")
                    e3.data = e1.data
                    print("Message sent to End Device 3")
                    e4.data = e1.data
                    print("Message sent to End Device 4")
                    e5.data = e1.data
                    print("Message sent to End Device 5")
                    e6.data = e1.data
                    print("Message sent to End Device 6")
                    e7.data = e1.data
                    print("Message sent to End Device 7")
                    e8.data = e1.data
                    print("Message sent to End Device 8")
                    e9.data = e1.data
                    print("Message sent to End Device 9")
                    e10.data = e1.data
                    print("Message sent to End Device 10")
                    print("                                          ---ACK RECEIVED  from End Device 6---")

            Switch1.maclist2[0] = e6.mac


            print("Enter the message")
            num3 = str(input())
            print("Message : ", num3)
            e8.data = num3
            print(" Sender Device is 8")
            print(" Receiver Device is 10")
            print("Searching for MAC address of End Device : 10 ")
            print("Mac Address of End Device 10 is =", e10.mac)
            for i in range(0, 5):
                if Switch1.maclist2[i] == e10.mac:
                    print("MAC address found in MAC table within same port")
                    e6.data = e8.data
                    print("Message sent to End Device 2")
                    e7.data = e8.data
                    print("Message sent to End Device 3")
                    e9.data = e8.data
                    print("Message sent to End Device 4")
                    e10.data = e8.data
                    print("Message sent to End Device 5")

                    print("                                          ---ACK RECEIVED  from End Device 10---")
                    break
                if i == 4:
                    print("Mac Address of End Device 2 not found in the MAC table")
                    e2.data = e8.data
                    print("Message sent to End Device 10")
                    e3.data = e8.data
                    print("Message sent to End Device 9")
                    e4.data = e8.data
                    print("Message sent to End Device 7")
                    e5.data = e8.data
                    print("Message sent to End Device 6")
                    e6.data = e8.data
                    print("Message sent to End Device 5")
                    e7.data = e8.data
                    print("Message sent to End Device 4")
                    e8.data = e8.data
                    print("Message sent to End Device 3")
                    e9.data = e8.data
                    print("Message sent to End Device 2")
                    e10.data = e8.data
                    print("Message sent to End Device 1")
                    print("                                          ---ACK RECEIVED  from End Device 10---")

            Switch1.maclist2[2] = e8.mac
            Switch1.maclist2[4] = e10.mac

            print("Enter the message")
            num3 = str(input())
            print("Message : ", num3)
            e10.data = num3
            print(" Sender Device is 10")
            print(" Receiver Device is 6")
            print("Searching for MAC address of End Device : 6 ")
            print("Mac Address of End Device 6 is =", e6.mac)
            for i in range(0, 5):
                if Switch1.maclist2[i] == e6.mac or Switch1.maclist1[i] == e6.mac :
                    print("MAC address found in MAC table within same port")
                    e6.data = e10.data
                    print("Message sent to End Device 2")
                    e7.data = e10.data
                    print("Message sent to End Device 3")
                    e8.data = e10.data
                    print("Message sent to End Device 4")
                    e9.data = e10.data
                    print("Message sent yo End Device 5")

                    print("                                               ---ACK RECEIVED  from End Device 6---")
                    break
                if i == 4:
                    print("Mac Address of End Device 6 not found in the MAC table")
                    e9.data = e10.data
                    print("Message sent to End Device 1")
                    e8.data = e10.data
                    print("Message sent to End Device 3")
                    e7.data = e10.data
                    print("Message sent to End Device 4")
                    e6.data = e10.data
                    print("Message sent to End Device 5")
                    e6.data = e10.data
                    print("Message sent to End Device 6")
                    e5.data = e10.data
                    print("Message sent to End Device 7")
                    e4.data = e10.data
                    print("Message sent to End Device 8")
                    e3.data = e10.data
                    print("Message sent to End Device 9")
                    e2.data = e10.data
                    print("Message sent to End Device 2")
                    print("                                           ---ACK RECEIVED  from End Device 6---")
            Switch1.maclist2[4] = e10.mac


            print("Mac Address Table of Port1")
            for i in range(0, 5):
                print("                                             END DEVICE ", i+1, "-", Switch1.maclist1[i])
            print("Mac Address Table of Port2")
            for i in range(0, 5):
                print("                                             END DEVICE ", i+6, "-", Switch1.maclist2[i])





    elif 4 == num4:
        if Hub1.Hub_vacant() == 0 and Switch1.Switch_vacant() ==0 and Hub2.Hub_vacant() == 0:
            print("Connection made between --Hub1------Switch------Hub2-- ")
            Switch1.port1 = 2
            Hub1.port6 = 6
            Hub2.port6 = 4
        if End_Device_Vacant() == 0 and Hub1.Hub_vacant() == 0:
            print("......................HUB 1  CONNECTING.......................")

            print("Connection made between Hub1 and  End Device 1")
            e1.port = 1
            Hub1.port1 = 9
            if Hub1.port2 == 0 and Hub1.port3 == 0 and Hub1.port4 == 0 and Hub1.port5 == 0:
                print("Connection made between Hub1 and  End Device 2")
                print("Connection made between Hub1 and  End Device 3")
                print("Connection made between Hub1 and  End Device 4")
                print("Connection made between Hub1 and  End Device 5")
                e2.port = 7
                e3.port = 2
                e4.port = 8
                e5.port = 1
                Hub1.port2 = 5
                Hub1.port3 = 8
                Hub1.port4 = 52
                Hub1.port5 = 80
            else:
                print("No Port vacant in HUB")
        else:
            print("---No end device vacant---")

        if End_Device_Vacant() == 0 or Hub2.Hub_vacant() == 0:
            print("......................HUB 2  CONNECTING.......................")
            print("Connection made between Hub2 and  End Device 6")
            e6.port = 1
            Hub2.port1 = 9
            if Hub2.port2 == 0 and Hub2.port3 == 0 and Hub2.port4 == 0 and Hub2.port5 == 0:
                print("Connection made between Hub2 and  End Device 7")
                print("Connection made between Hub2 and  End Device 8")
                print("Connection made between Hub2 and  End Device 9")
                print("Connection made between Hub2 and  End Device 10")
                e7.port = 71
                e8.port = 22
                e9.port = 71
                e10.port = 22
                Hub2.port2 = 50
                Hub2.port3 = 801
                Hub2.port4 = 501
                Hub2.port5 = 800
            else:
                print("No Port vacant in HUB")

        else:
            print("---No end Device vacant---")
        print("Enter token value")
        token = int(input())
        print("Enter Sender Device no")
        num1 = int(input())
        token_passing(token, num1)
        print("Enter receiver Device no")
        num2 = int(input())
        print("Enter message :")
        num3 = str(input())

        print("Choose the flow control protocol ")
        print("1.STOP AND WAIT ARQ")
        print("2.SELECTIVE REPEAT")
        num5 = int(input())
        if 1 == num5:
            stop_and_wait_arq_HUb(num1, num2, num3)
        else:
            Selective_Repeat_Hub(num1, num2, num3)




    elif 5 == num4:
        if Switch1.Switch_vacant() == 0 and  End_Device_Vacant() ==0:
           print("-----------CONNECTING TO SWITCH------------")
           for i in range(1, 6):
               print("End Device", i, " Connected to Switch" )
           print("Enter token value")
           token = int(input())
           print("Enter Sender Device no")
           num1 = int(input())
           token_passing(token, num1)
           print("Enter receiver Device no")
           num2 = int(input())
           print("Enter message :")
           num3 = str(input())
        if num2 != num1:
           print("Choose the flow control protocol ")
           print("1.STOP AND WAIT ARQ")
           print("2.SELECTIVE REPEAT ")
           num5 = int(input())
           if 1 == num5:
               stop_and_wait_arq(num1, num2, num3)
           else:
               Selective_Repeat(num1, num2, num3)
        else:
            print(" Enter valid number. No communication possible!")





    elif 6 == num4:

        if  Switch1.Switch_vacant() == 0 and  Switch2.Switch_vacant() == 0:
            print("Connection made between --Switch1------Router------Switch2-- ")
            Switch1.port1 = 1
            Switch2.port1 = 1
        if End_Device_Vacant() == 0 or Switch1.Switch_vacant() == 0:
            print("......................SWITCH 1  CONNECTING.......................")

            print("Connection made between Switch1 and  End Device 1")
            e1.port = 1
            Switch2.port1 = 9
            if Hub1.port2 == 0 and Hub1.port3 == 0 and Hub1.port4 == 0 and Hub1.port5 == 0:
                print("Connection made between Switch1 and  End Device 2")

                e2.port = 7
            else:
                print("No Port vacant in SWITCH")
        else:
            print("---No end device vacant---")

        if End_Device_Vacant() != 0 or Switch2.Switch_vacant() == 0:
            print("......................SWITCH 2  CONNECTING.......................")
            print("Connection made between SWITCH 2 and  End Device 3")
            e3.port = 1
            Switch2.port1 = 9
            if Hub2.port2 == 0 and Hub2.port3 == 0 and Hub2.port4 == 0 and Hub2.port5 == 0:
                print("Connection made between SWITCH 2 and  End Device 4")
                e4.port = 7
            else:
                print("No Port vacant in SWITCH")
        else:
            print("error")

        for i in range(0, 4):
            print("Enter IP Address of End Device", i + 1)
            user = str(input())
            endDevices[i + 1].ip = user
            print("Enter Network Prefix Length of device ", i + 1)
            user = int(input())
            endDevices[i + 1].subnet = user
            print("Enter Default gateway of device ", i + 1)
            user = str(input())
            endDevices[i + 1].gateway = user

        if get_nid(endDevices[1].ip, endDevices[1].subnet) != get_nid(endDevices[2].ip, endDevices[2].subnet) or get_nid(endDevices[3].ip, endDevices[3].subnet) != get_nid(endDevices[4].ip, endDevices[4].subnet):
            print("Enter valid IP addresses")


        Router1.user_executive_mode()
        ping(1,4)






    elif 7 == num4:

        if  Switch1.Switch_vacant() == 0 and  Switch2.Switch_vacant() == 0:
            print("Connection made between --Switch1------Router1----Router2------Switch2-- ")
            print("Connection made between ---Router1----Router3------Router2----- ")
            print("   E1                                E3   \n"
                  "    |                                |    \n"
                  "   S1---------R1 - - - - -R2---------S2   \n"
                  "    |           -        -           |    \n"
                  "   E2             -    -             E4   \n"
                  "                    R3                    \n"
                  )
            Switch1.port1 = 1
            Switch2.port1 = 1
        if End_Device_Vacant() == 0 or Switch1.Switch_vacant() == 0:
            print("......................SWITCH 1  CONNECTING.......................")

            print("Connection made between Switch1 and  End Device 1")
            e1.port = 1
            Switch2.port1 = 9
            if Hub1.port2 == 0 and Hub1.port3 == 0 and Hub1.port4 == 0 and Hub1.port5 == 0:
                print("Connection made between Switch1 and  End Device 2")

                e2.port = 7
            else:
                print("No Port vacant in SWITCH")
        else:
            print("---No end device vacant---")

        if End_Device_Vacant() != 0 or Switch2.Switch_vacant() == 0:
            print("......................SWITCH 2  CONNECTING.......................")
            print("Connection made between SWITCH 2 and  End Device 3")
            e3.port = 1
            Switch2.port1 = 9
            if Hub2.port2 == 0 and Hub2.port3 == 0 and Hub2.port4 == 0 and Hub2.port5 == 0:
                print("Connection made between SWITCH 2 and  End Device 4")
                e4.port = 7
            else:
                print("No Port vacant in SWITCH")
        else:
            print("error")

        for i in range(0, 4):
            print("Enter IP Address of End Device", i + 1)
            user = str(input())
            endDevices[i + 1].ip = user
            print("Enter Network Prefix Length of device ", i + 1)
            user = int(input())
            endDevices[i + 1].subnet = user
            print("Enter Default gateway of device ", i + 1)
            user = str(input())
            endDevices[i + 1].gateway = user

        if get_nid(endDevices[1].ip, endDevices[1].subnet) != get_nid(endDevices[2].ip, endDevices[2].subnet) or get_nid(endDevices[3].ip, endDevices[3].subnet) != get_nid(endDevices[4].ip, endDevices[4].subnet):
            print("Enter valid IP addresses")

        Router1.R_table = []
        list1 = ["10.0.0.0", 24, "10.0.0.3", "", 1]
        Router1.R_table.append(list1)
        list2 = ["20.0.0.0", 24, "20.0.0.2", "", 5]
        Router1.R_table.append(list2)
        list3 = ["30.0.0.0", 23, "30.0.0.1", "", 1]
        Router1.R_table.append(list3)
        list4 = ["40.0.0.0", 22, "40.0.0.1", "", 1]
        Router1.R_table.append(list4)
        list5 = ["50.0.0.0", 22, "30.0.0.1", "", 5]
        Router1.R_table.append(list5)

        Router2.R_table = []
        list6 = ["10.0.0.0", 24, "30.0.0.2", "", 5]
        Router2.R_table.append(list6)
        list7 = ["20.0.0.0", 24, "20.0.0.3", "", 1]
        Router2.R_table.append(list7)
        list8 = ["30.0.0.0", 23, "30.0.0.2", "", 1]
        Router2.R_table.append(list8)
        list9 = ["50.0.0.0", 22, "50.0.0.1", "", 1]
        Router2.R_table.append(list9)
        list12 = ["40.0.0.0", 22, "40.0.0.2", "", 5]
        Router2.R_table.append(list12)

        Router3.R_table = []

        list10 = ["10.0.0.0", 24, "10.0.0.2", "", 5]
        Router3.R_table.append(list10)
        list11 = ["20.0.0.0", 24, "20.0.0.3", "", 1]
        Router3.R_table.append(list11)
        list13 = ["30.0.0.0", 23, "30.0.0.2", "", 5]
        Router3.R_table.append(list13)
        list14 = ["40.0.0.0", 22, "40.0.0.2", "", 1]
        Router3.R_table.append(list14)
        list15 = ["50.0.0.0", 22, "50.0.0.2", "", 1]
        Router3.R_table.append(list15)
        Router1.user_executive_mode()
        Router2.user_executive_mode()
        Router3.user_executive_mode()

        Router1.R_table = []
        list1 = ["10.0.0.0", 24, "10.0.0.3", "", 1]
        Router1.R_table.append(list1)
        list2 = ["20.0.0.0", 24, "20.0.0.2", "", 5]
        Router1.R_table.append(list2)
        list3 = ["30.0.0.0", 23, "30.0.0.1", "", 1]
        Router1.R_table.append(list3)
        list4 = ["40.0.0.0", 22, "40.0.0.1", "", 1]
        Router1.R_table.append(list4)
        list5 = ["50.0.0.0", 22, "30.0.0.1", "", 5]
        Router1.R_table.append(list5)

        Router2.R_table = []
        list6 = ["10.0.0.0", 24, "30.0.0.2", "", 5]
        Router2.R_table.append(list6)
        list7 = ["20.0.0.0", 24, "20.0.0.3", "", 1]
        Router2.R_table.append(list7)
        list8 = ["30.0.0.0", 23, "30.0.0.2", "", 1]
        Router2.R_table.append(list8)
        list9 = ["50.0.0.0", 22, "50.0.0.1", "", 1]
        Router2.R_table.append(list9)
        list12 = ["40.0.0.0", 22, "40.0.0.2", "", 5]
        Router2.R_table.append(list12)

        Router3.R_table = []

        list10 = ["10.0.0.0", 24, "10.0.0.2", "", 5]
        Router3.R_table.append(list10)
        list11 = ["20.0.0.0", 24, "20.0.0.3", "", 1]
        Router3.R_table.append(list11)
        list13 = ["30.0.0.0", 23, "30.0.0.2", "", 5]
        Router3.R_table.append(list13)
        list14 = ["40.0.0.0", 22, "40.0.0.2", "", 1]
        Router3.R_table.append(list14)
        list15 = ["50.0.0.0", 22, "50.0.0.2", "", 1]
        Router3.R_table.append(list15)



        ping(1, 4)

        RIP()

    elif 8 == num4:
        if End_Device_Vacant() ==0:
           print("-----------CONNECTING TO ROUTER------------")
           for i in range(1, 4):
               print("End Device", i, " Connected to  Router on Interface 1" )
           for i in range(4, 7):
                   print("End Device", i, " Connected to  Router on Interface 2")

           print("            E3              E4            \n"
                 "                -         -               \n"
                 "   E1- - - - - - - -R1- - - - - - - -E5   \n"
                 "                -        -                \n"
                 "            E2               E6           \n"
                 "                                          \n"
                 )


           print("Enter the respective number for the transport layer protocols")
           print("1.UDP")
           print("2.TCP")
           x = int(input())
           if x == 1:
               print("Enter the Name of the Server")
               n = str((input()))
               print("Enter the port no of the server you want to communicate")
               p = int(input())
               print("Enter the ip address of server")
               i = str(input())
               print("Enter the Device from which you want to communicate")
               e = int(input())
               print("Enter the Message")
               m = str(input())
               udp(n,p,i,e,m)
           else:
               print("Enter the Name of the Server")
               n = str((input()))
               print("Enter the port no of the server you want to communicate")
               p = int(input())
               print("Enter the ip address of server")
               i = str(input())
               print("Enter the Device from which you want to communicate")
               e = int(input())
               print("Enter the Message")
               m = str(input())
               tcp(n,p,i,e,m)





        else:
            print(" Enter valid number. No communication possible!")


    elif 9 == num4:
        print("Press the following number the protocols\n"
              "1.DHCP\n"
              "2.HTTP\n"
              )
        x = int(input())
        if x == 1:
            if End_Device_Vacant() == 0:
                print("-----------CONNECTING TO ROUTER------------")
                for i in range(1, 4):
                    print("End Device", i, " Connected to  Router on Interface 1")
                for i in range(4, 7):
                    print("End Device", i, " Connected to  Router on Interface 2")

                print("            E3                           E4           \n"
                      "                -                    -                \n"
                      "      E1- - - - - - S1----R1-----S2 - - - - - -E5     \n"
                      "                -                    -                \n"
                      "            E2                           E6           \n"
                      "                                                      \n"
                      )

                print("Configuring the router")
                Router1.user_executive_mode()

                for i in range(1, 7):
                    print("For End Device ", i," ")
                    DHCP(i)

        else:
            HTTP()
    else:
        print("Error, Enter valid number")




















Connections()

#  if num4 < 8:
#    collision_broadcast()
#  else:
#     print("Enter valid Number")



