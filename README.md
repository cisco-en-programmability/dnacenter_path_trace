# Cisco DNA Center Path Trace


This Python script will perform Path Trace between two nodes in the Cisco DNA Center managed network.
Path Trace is a excellent tool to assist in troubleshooting connectivity between a source device and destination device.

**Cisco Products & Services:**

- Cisco DNA Center

**Tools & Frameworks:**

- Python environment

**Usage**

- $ python path_trace.py source_ip, source_port, destination_ip, destination_port, protocol

This script will use the Cisco DNA Center APIs to find out the path taken in the network between the source and destination devices specified.

mandatory parameters: source_ip and destination_ip

optional parameters: source_port, destination_port, protocol

- Sample output:
Input the source IPv4 Address:   10.93.140.35
Input the source port number (or Enter for none):   
Input the destination IPv4 Address:   10.93.130.46
Input the destination port number (or Enter for none):   80
Input the protocol number (or Enter for none):   6

Initiated Path Trace with these parameters:
{
    "destIP" : "10.93.130.46" , 
    "periodicRefresh" : false , 
    "sourceIP" : "10.93.140.35" , 
    "destPort" : 80 , 
    "protocol" : 6
}

Initiated Path Trace with the id: 
 90e4e253-dbd1-4dd8-852a-d91a3b939338

Path Trace status:  COMPLETED

Path Trace result:
[
    "10.93.140.35" , 
    "GigabitEthernet1/0/1" , 
    "NYC-9300" , 
    "GigabitEthernet1/0/48" , 
    "GigabitEthernet2" , 
    "NYC-RO" , 
    "GigabitEthernet3" , 
    "GigabitEthernet3" , 
    "SP" , 
    "GigabitEthernet2" , 
    "GigabitEthernet2" , 
    "PDX-RO" , 
    "GigabitEthernet1" , 
    "GigabitEthernet1/0/13" , 
    "PDX-CORE-3850" , 
    "10.93.130.46"
]


End of Application "path_trace.py" Run


**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).
