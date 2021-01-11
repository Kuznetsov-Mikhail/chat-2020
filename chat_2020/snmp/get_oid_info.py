from pysnmp.hlapi import *
from ipaddress import *
from datetime import datetime

community_string = 'rpublic'  # From file
ip_address_host = '192.168.9.1'  # From file
port_snmp = 161
OID_sysName = '.1.3.6.1.2.1.1.1.0'  # From SNMPv2-MIB hostname/sysname
OID_blank = '.1.3.6.1.2.1.1.7.0'  # From SNMPv2-MIB hostname/sysname

def snmp_getcmd(community, ip, port, OID):
    return (getCmd(SnmpEngine(),
                   CommunityData(community),
                   UdpTransportTarget((ip, port)),
                   ContextData(),
                   ObjectType(ObjectIdentity(OID))))

def snmp_get_next(community, ip, port, OID):
    errorIndication, errorStatus, errorIndex, varBinds = next(snmp_getcmd(community, ip, port, OID))
    buffer = []
    for name, val in varBinds:
        return val.prettyPrint()

if __name__ == "__main__":
	sysname = str(snmp_get_next(community_string, ip_address_host, port_snmp, OID_sysName))
	print(sysname)


