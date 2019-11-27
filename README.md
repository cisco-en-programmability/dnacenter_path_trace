# Cisco DNA Center Path Trace


This Python script will perform Path Trace between two clients in the Cisco DNA Center managed network.

Path Trace is a excellent tool to assist in troubleshooting connectivity between a source device and destination device.

Path Trace will collect the path information for specified source and destination IPv4 addresses, and optional, source and destination port numbers, and protocol number.
It will collect also information about in-path interface statistics, device statistics, ACLs and QoS Policies

**Cisco Products & Services:**

- Cisco DNA Center

**Tools & Frameworks:**

- Python environment

**Usage**

This app will ask the user to input the following:

- Source IPv4 Address
- Source port number (or Enter for none)
- Destination IPv4 Address
- Destination port number (or Enter for none)
- Protocol number (or Enter for none)

$ python path_trace.py 

*Sample output:*

    Input the source IPv4 Address:   10.93.140.35
    Input the source port number (or Enter for none):   5500
    Input the destination IPv4 Address:   10.93.234.96
    Input the destination port number (or Enter for none):   80
    Input the protocol number (or Enter for none):   6
    
    Initiated Path Trace with these parameters:
    {
        "destIP" : "10.93.234.96" , 
        "sourceIP" : "10.93.140.35" , 
        "periodicRefresh" : false , 
        "inclusions" : [
            "INTERFACE-STATS" , 
            "DEVICE-STATS" , 
            "ACL-TRACE" , 
            "QOS-STATS"
        ] , 
        "sourcePort" : 5500 , 
        "destPort" : 80 , 
        "protocol" : 6
    }
    
    Initiated Path Trace with the id: 
    a1bba53b-5d80-4aba-9372-573645077ee9
    
    
    The complete path trace info is: 
    
    {
        "request" : {
            "sourceIP" : "10.93.140.35" , 
            "sourcePort" : "5500" , 
            "destIP" : "10.93.234.96" , 
            "destPort" : "80" , 
            "protocol" : "6" , 
            "periodicRefresh" : false , 
            "inclusions" : [
                "INTERFACE-STATS" , 
                "ACL-TRACE" , 
                "DEVICE-STATS" , 
                "QOS-STATS"
            ] , 
            "id" : "a1bba53b-5d80-4aba-9372-573645077ee9" , 
            "status" : "COMPLETED" , 
            "createTime" : 1574879612290 , 
            "lastUpdateTime" : 1574879612878 , 
            "controlPath" : false
            .....
            .....
            .....
            }
    
    Path Trace status:  COMPLETED
    
    Path Trace result:
    [
        "10.93.140.35" , 
        "TenGigabitEthernet1/0/1" , 
        "NYC-ACCESS" , 
        "TenGigabitEthernet1/0/24" , 
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
        "PDX-M" , 
        "GigabitEthernet1/0/20" , 
        "FastEthernet0" , 
        "PDX-DMZ" , 
        "10.93.234.96"
    ]
    
    
    End of Application "path_trace.py" Run


**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).
