# Aa-network-simulator-implementing-entire-protocol-stack
A simulated model which demonstrates the working of the TCP/IP Networking Model. This project shows proper working of the all layers:


1.Physical Layer: The physical layer is responsible for sending and receiving packets from one physical interface to others.



2.Data Link Layer: The data link layer controls the flow of reception, delimitation and transmission of frames and establishes a communication protocol (Media Access Control) between directly connected systems 



3.Network layer: Handles the routing and sending of data between different networks. The most important protocols at this layer are IP and ICMP. We have implemented the Routing Information Protocol-(RIP) in the project for shortest path. 


4.Transport layer: Provides the means for transmitting data between the two connected parties, as well as controlling the quality of service. The main protocols used here are TCP and UDP. We have set a probability for packet drop in UDP to show that this protocol is unreliable. TCP is a reliable protocol where no packet drop is shown. A server class is made to enable the 3 services we have included HTTP, SSH, SMTP.


5.Application Layer: The application layer is the highest abstraction layer of the TCP/IP model that provides the interfaces and protocols needed by the users. It combines the functionalities of the session layer, the presentation layer and the application layer of the OSI model. We have included two application layer services DHCP and HTTP
