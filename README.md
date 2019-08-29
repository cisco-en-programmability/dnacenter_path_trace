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

Sample output:


**License**

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
