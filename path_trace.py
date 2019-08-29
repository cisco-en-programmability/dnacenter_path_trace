#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Cisco DNA Center Get Auth Token

Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Gabriel Zapodeanu TME, ENB"
__email__ = "gzapodea@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import sys
import requests
import json
import urllib3
import time
import ipaddress

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
from requests.auth import HTTPBasicAuth  # for Basic Auth

from config import DNAC_URL, DNAC_PASS, DNAC_USER

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)


def pprint(json_data):
    """
    Pretty print JSON formatted data
    :param json_data: data to pretty print
    :return None
    """
    print(json.dumps(json_data, indent=4, separators=(' , ', ' : ')))

def get_dnac_jwt_token(dnac_auth):
    """
    Create the authorization token required to access DNA C
    Call to Cisco DNA C - /api/system/v1/auth/login
    :param dnac_auth - DNA C Basic Auth string
    :return Cisco DNA C Auth Token
    """

    url = DNAC_URL + '/dna/system/api/v1/auth/token'
    header = {'content-type': 'application/json'}
    response = requests.post(url, auth=dnac_auth, headers=header, verify=False)
    response_json = response.json()
    dnac_jwt_token = response_json['Token']
    return dnac_jwt_token


def create_path_trace(src_ip, dest_ip, dnac_jwt_token):
    """
    This function will create a new Path Trace between the source IP address {src_ip} and the
    destination IP address {dest_ip}
    :param src_ip: Source IP address
    :param dest_ip: Destination IP address
    :param dnac_jwt_token: DNA C token
    :return: DNA C path visualisation id
    """

    param = {
        'destIP': dest_ip,
        'periodicRefresh': False,
        'sourceIP': src_ip
    }

    url = DNAC_URL + '/dna/intent/api/v1/flow-analysis'
    header = {'accept': 'application/json', 'content-type': 'application/json', 'x-auth-token': dnac_jwt_token}
    path_response = requests.post(url, data=json.dumps(param), headers=header, verify=False)
    path_json = path_response.json()
    path_id = path_json['response']['flowAnalysisId']
    return path_id


def get_path_trace_info(path_id, dnac_jwt_token):
    """
    This function will return the path trace details for the path visualisation {id}
    :param path_id: DNA C path visualisation id
    :param dnac_jwt_token: DNA C token
    :return: Path visualisation status, and the details in a list [device,interface_out,interface_in,device...]
    """

    url = DNAC_URL + '/dna/intent/api/v1/flow-analysis/' + path_id
    header = {'accept': 'application/json', 'content-type': 'application/json', 'x-auth-token': dnac_jwt_token}
    path_response = requests.get(url, headers=header, verify=False)
    path_json = path_response.json()
    path_info = path_json['response']
    path_status = path_info['request']['status']
    path_list = []
    if path_status == 'COMPLETED':
        network_info = path_info['networkElementsInfo']
        path_list.append(path_info['request']['sourceIP'])
        for elem in network_info:
            try:
                path_list.append(elem['ingressInterface']['physicalInterface']['name'])
            except:
                pass
            try:
                path_list.append(elem['name'])
            except:
                pass
            try:
                path_list.append(elem['egressInterface']['physicalInterface']['name'])
            except:
                pass
        path_list.append(path_info['request']['destIP'])
    return path_status, path_list


def validate_ipv4_address(ipv4_address):
    """
    This function will validate if the provided string is a valid IPv4 address
    :param ipv4_address: string with the IPv4 address
    :return: true/false
    """
    try:
        ipaddress.ip_address(ipv4_address)
        return True
    except:
        return False


def main():
    """
    This sample script will:
    - ask the user to enter the source and destination node IPv4 address and optional the source and destination port,
    optional protocol
    - start the Cisco DNA Center Path Trace for the above endpoints
    - retrieve the Path Trace result
    """

    # obtain the Cisco DNA C Auth Token
    dnac_token = get_dnac_jwt_token(DNAC_AUTH)

    # ask user for the inout of the IPv4 addresses and ports, protocol
    # validate if the entered IPv4 addresses are valid

    while True:
        source_ip = input('Input the source IPv4 Address:   ')
        if validate_ipv4_address(source_ip) is True:
            break
        else:
            print('IPv4 address is not valid')

    source_port = input('Input the source port (or Enter for none):   ')

    while True:
        destination_ip = input('Input the destination IPv4 Address:   ')
        if validate_ipv4_address(destination_ip) is True:
            break
        else:
            print('IPv4 address is not valid')

    destination_port = input('Input the destination port (or Enter for none):   ')

    protocol = input('Input the protocol (or Enter for none):   ')




    print('\n\nEnd of Application "path_trace.py" Run')


if __name__ == "__main__":
    main()

