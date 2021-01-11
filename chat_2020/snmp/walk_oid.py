from pysnmp.hlapi import *

def walk_mib(ipaddress, oid):
    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(SnmpEngine(),
               CommunityData('rpublic'),
               UdpTransportTarget((ipaddress, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)),
               ):

        if not errorIndication and not errorStatus:
            for varBind in varBinds:
                result = ' = '.join([x.prettyPrint() for x in varBind])
                print(result)

if __name__ == "__main__":
    start_oid = ".1.3.6.1.2.1.1"
    walk_mib('192.168.9.1', start_oid)
