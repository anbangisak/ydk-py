""" Cisco_IOS_XR_ip_udp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-udp package operational data.

This module contains definitions
for the following management objects\:
  udp\: IP UDP Operational Data
  udp\-connection\: udp connection

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class AddrFamily_Enum(Enum):
    """
    AddrFamily_Enum

    Address Family Types

    """

    """

    Unspecified

    """
    UNSPECIFIED = 0

    """

    Local to host (pipes, portals)

    """
    LOCAL = 1

    """

    Internetwork\: UDP, TCP, etc.

    """
    INET = 2

    """

    arpanet imp addresses

    """
    IMPLINK = 3

    """

    Pup protocols\: e.g. BSP

    """
    PUP = 4

    """

    mit CHAOS protocols

    """
    CHAOS = 5

    """

    XEROX NS protocols

    """
    NS = 6

    """

    ISO protocols

    """
    ISO = 7

    """

    European computer manufacturers

    """
    ECMA = 8

    """

    Datakit protocols

    """
    DATA_KIT = 9

    """

    CCITT protocols, X.25 etc

    """
    CCITT = 10

    """

    IBM SNA

    """
    SNA = 11

    """

    DECnet

    """
    DE_CNET = 12

    """

    DEC Direct data link interface

    """
    DLI = 13

    """

    LAT

    """
    LAT = 14

    """

    NSC Hyperchannel

    """
    HYLINK = 15

    """

    Apple Talk

    """
    APPLETALK = 16

    """

    Internal Routing Protocol

    """
    ROUTE = 17

    """

    Link layer interface

    """
    LINK = 18

    """

    eXpress Transfer Protocol (no AF)

    """
    PSEUDO_XTP = 19

    """

    Connection\-oriented IP, aka ST II

    """
    COIP = 20

    """

    Computer Network Technology

    """
    CNT = 21

    """

    Help Identify RTIP packets

    """
    PSEUDO_RTIP = 22

    """

    Novell Internet Protocol

    """
    IPX = 23

    """

    Simple Internet Protocol

    """
    SIP = 24

    """

    Help Identify PIP packets

    """
    PSEUDO_PIP = 25

    """

    IP version 6

    """
    INET6 = 26

    """

    802.2 SNAP sockets

    """
    SNAP = 27

    """

    SAP\_CLNS + nlpid encaps

    """
    CLNL = 28

    """

    cisco HDLC on serial

    """
    CHDLC = 29

    """

    PPP sockets

    """
    PPP = 30

    """

    Host\-based CAS signaling

    """
    HOST_CAS = 31

    """

    DSP messaging

    """
    DSP = 32

    """

    SAP Sockets

    """
    SAP = 33

    """

    ATM Sockets

    """
    ATM = 34

    """

    Frame Relay sockets

    """
    FR = 35

    """

    Voice Media Stream Sockets

    """
    MSO = 36

    """

    ISDN D Channel Sockets

    """
    DCHAN = 37

    """

    Trunk Framer media IF Sockets

    """
    CAS = 38

    """

    Network Address Translation Sockets

    """
    NAT = 39

    """

    Generic Ethernet Sockets

    """
    ETHER = 40

    """

    Spatial Reuse Protocol Sockets

    """
    SRP = 41


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['AddrFamily_Enum']


class LptsPcbQuery_Enum(Enum):
    """
    LptsPcbQuery_Enum

    Lpts pcb query

    """

    """

    No filter

    """
    ALL = 0

    """

    Static policy filter

    """
    STATIC_POLICY = 1

    """

    Interface filter

    """
    INTERFACE = 2

    """

    Packet type filter

    """
    PACKET = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['LptsPcbQuery_Enum']


class MessageTypeIcmp_Enum(Enum):
    """
    MessageTypeIcmp_Enum

    LPTS ICMP message types

    """

    """

    ICMP Packet type\: Echo reply

    """
    ECHO_REPLY = 0

    """

    ICMP Packet type\: Destination unreachable

    """
    DESTINATION_UNREACHABLE = 3

    """

    ICMP Packet type\: Source quench

    """
    SOURCE_QUENCH = 4

    """

    ICMP Packet type\: Redirect

    """
    REDIRECT = 5

    """

    ICMP Packet type\: Alternate host address

    """
    ALTERNATE_HOST_ADDRESS = 6

    """

    ICMP Packet type\: Echo

    """
    ECHO = 8

    """

    ICMP Packet type\: Router advertisement

    """
    ROUTER_ADVERTISEMENT = 9

    """

    ICMP Packet type\: Router selection

    """
    ROUTER_SELECTION = 10

    """

    ICMP Packet type\: Time exceeded

    """
    TIME_EXCEEDED = 11

    """

    ICMP Packet type\: Parameter problem

    """
    PARAMETER_PROBLEM = 12

    """

    ICMP Packet type\: Time stamp

    """
    TIME_STAMP = 13

    """

    ICMP Packet type\: Time stamp reply

    """
    TIME_STAMP_REPLY = 14

    """

    ICMP Packet type\: Information request

    """
    INFORMATION_REQUEST = 15

    """

    ICMP Packet type\: Information reply

    """
    INFORMATION_REPLY = 16

    """

    ICMP Packet type\: Address mask request

    """
    ADDRESS_MASK_REQUEST = 17

    """

    ICMP Packet type\: Address mask reply

    """
    ADDRESS_MASK_REPLY = 18

    """

    ICMP Packet type\: Trace route

    """
    TRACE_ROUTE = 30

    """

    ICMP Packet type\: Datagram Conversion error

    """
    DATAGRAM_CONVERSION_ERROR = 31

    """

    ICMP Packet type\: Mobile host redirect

    """
    MOBILE_HOST_REDIRECT = 32

    """

    ICMP Packet type\: IPv6 where\-are\-you

    """
    WHERE_ARE_YOU = 33

    """

    ICMP Packet type\: IPv6 i\-am\-here

    """
    IAM_HERE = 34

    """

    ICMP Packet type\: Mobile registration request

    """
    MOBILE_REGISTRATION_REQUEST = 35

    """

    ICMP Packet type\: Mobile registration reply

    """
    MOBILE_REGISTRATION_REPLY = 36

    """

    ICMP Packet type\: Domain name request

    """
    DOMAIN_NAME_REQUEST = 37


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIcmp_Enum']


class MessageTypeIcmp_Enum(Enum):
    """
    MessageTypeIcmp_Enum

    LPTS ICMP message types

    """

    """

    ICMP Packet type\: Echo reply

    """
    ECHO_REPLY = 0

    """

    ICMP Packet type\: Destination unreachable

    """
    DESTINATION_UNREACHABLE = 3

    """

    ICMP Packet type\: Source quench

    """
    SOURCE_QUENCH = 4

    """

    ICMP Packet type\: Redirect

    """
    REDIRECT = 5

    """

    ICMP Packet type\: Alternate host address

    """
    ALTERNATE_HOST_ADDRESS = 6

    """

    ICMP Packet type\: Echo

    """
    ECHO = 8

    """

    ICMP Packet type\: Router advertisement

    """
    ROUTER_ADVERTISEMENT = 9

    """

    ICMP Packet type\: Router selection

    """
    ROUTER_SELECTION = 10

    """

    ICMP Packet type\: Time exceeded

    """
    TIME_EXCEEDED = 11

    """

    ICMP Packet type\: Parameter problem

    """
    PARAMETER_PROBLEM = 12

    """

    ICMP Packet type\: Time stamp

    """
    TIME_STAMP = 13

    """

    ICMP Packet type\: Time stamp reply

    """
    TIME_STAMP_REPLY = 14

    """

    ICMP Packet type\: Information request

    """
    INFORMATION_REQUEST = 15

    """

    ICMP Packet type\: Information reply

    """
    INFORMATION_REPLY = 16

    """

    ICMP Packet type\: Address mask request

    """
    ADDRESS_MASK_REQUEST = 17

    """

    ICMP Packet type\: Address mask reply

    """
    ADDRESS_MASK_REPLY = 18

    """

    ICMP Packet type\: Trace route

    """
    TRACE_ROUTE = 30

    """

    ICMP Packet type\: Datagram Conversion error

    """
    DATAGRAM_CONVERSION_ERROR = 31

    """

    ICMP Packet type\: Mobile host redirect

    """
    MOBILE_HOST_REDIRECT = 32

    """

    ICMP Packet type\: IPv6 where\-are\-you

    """
    WHERE_ARE_YOU = 33

    """

    ICMP Packet type\: IPv6 i\-am\-here

    """
    IAM_HERE = 34

    """

    ICMP Packet type\: Mobile registration request

    """
    MOBILE_REGISTRATION_REQUEST = 35

    """

    ICMP Packet type\: Mobile registration reply

    """
    MOBILE_REGISTRATION_REPLY = 36

    """

    ICMP Packet type\: Domain name request

    """
    DOMAIN_NAME_REQUEST = 37


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIcmp_Enum']


class MessageTypeIcmpv6_Enum(Enum):
    """
    MessageTypeIcmpv6_Enum

    LPTS ICMPv6 message types

    """

    """

    ICMPv6 Packet type\: Destination unreachable

    """
    DESTINATION_UNREACHABLE = 1

    """

    ICMPv6 Packet type\: packet too big

    """
    PACKET_TOO_BIG = 2

    """

    ICMPv6 Packet type\: Time exceeded

    """
    TIME_EXCEEDED = 3

    """

    ICMPv6 Packet type\: Parameter problem

    """
    PARAMETER_PROBLEM = 4

    """

    ICMPv6 Packet type\: Echo request

    """
    ECHO_REQUEST = 128

    """

    ICMPv6 Packet type\: Echo reply

    """
    ECHO_REPLY = 129

    """

    ICMPv6 Packet type\: Multicast listener query

    """
    MULTICAST_LISTENER_QUERY = 130

    """

    ICMPv6 Packet type\: Multicast listener report

    """
    MULTICAST_LISTENER_REPORT = 131

    """

    ICMPv6 Packet type\: Multicast listener done

    """
    MULTICAST_LISTENER_DONE = 132

    """

    ICMPv6 Packet type\: Router solicitation

    """
    ROUTER_SOLICITATION = 133

    """

    ICMPv6 Packet type\: Router advertisement

    """
    ROUTER_ADVERTISEMENT = 134

    """

    ICMPv6 Packet type\: Neighbor solicitation

    """
    NEIGHBOR_SOLICITATION = 135

    """

    ICMPv6 Packet type\: Neighbor advertisement

    """
    NEIGHBOR_ADVERTISEMENT = 136

    """

    ICMPv6 Packet type\: Redirect message

    """
    REDIRECT_MESSAGE = 137

    """

    ICMPv6 Packet type\: Router renumbering

    """
    ROUTER_RENUMBERING = 138

    """

    ICMPv6 Packet type\: Node information query

    """
    NODE_INFORMATION_QUERY = 139

    """

    ICMPv6 Packet type\: Node information reply

    """
    NODE_INFORMATION_REPLY = 140

    """

    ICMPv6 Packet type\: Inverse neighbor discovery
    solicitation message

    """
    INVERSE_NEIGHBOR_DISCOVERY_SOLICITAION = 141

    """

    ICMPv6 Packet type\: Inverse neighbor discovery
    advertisement message

    """
    INVERSE_NEIGHBOR_DISCOVER_ADVERTISEMENT = 142

    """

    ICMPv6 Packet type\: Version 2 multicast
    listener report

    """
    V2_MULTICAST_LISTENER_REPORT = 143

    """

    ICMPv6 Packet type\: Home agent address
    discovery request message

    """
    HOME_AGENT_ADDRESS_DISCOVERY_REQUEST = 144

    """

    ICMPv6 Packet type\: Home agent address
    discovery reply message

    """
    HOME_AGENT_ADDRESS_DISCOVERY_REPLY = 145

    """

    ICMPv6 Packet type\: Mobile prefix solicitation

    """
    MOBILE_PREFIX_SOLICITATION = 146

    """

    ICMPv6 Packet type\: Mobile prefix advertisement

    """
    MOBILE_PREFIX_ADVERTISEMENT = 147

    """

    ICMPv6 Packet type\: Certification path
    solicitation message

    """
    CERTIFICATION_PATH_SOLICITATION_MESSAGE = 148

    """

    ICMPv6 Packet type\: Certification path
    advertisement message

    """
    CERTIFICATION_PATH_ADVERTISEMENT_MESSAGE = 149

    """

    ICMPv6 Packet type\: ICMP messages utilized by
    experimental mobility  protocols such as
    seamoby

    """
    EXPERIMENTAL_MOBILITY_PROTOCOLS = 150

    """

    ICMPv6 Packet type\: Multicast router
    advertisement

    """
    MULTICAST_ROUTER_ADVERTISEMENT = 151

    """

    ICMPv6 Packet type\: Multicast router
    solicitation

    """
    MULTICAST_ROUTER_SOLICITATION = 152

    """

    ICMPv6 Packet type\: Multicast router
    termination

    """
    MULTICAST_ROUTER_TERMINATION = 153

    """

    ICMPv6 Packet type\: FMIPv6 messages

    """
    FMIPV6_MESSAGES = 154


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIcmpv6_Enum']


class MessageTypeIcmpv6_Enum(Enum):
    """
    MessageTypeIcmpv6_Enum

    LPTS ICMPv6 message types

    """

    """

    ICMPv6 Packet type\: Destination unreachable

    """
    DESTINATION_UNREACHABLE = 1

    """

    ICMPv6 Packet type\: packet too big

    """
    PACKET_TOO_BIG = 2

    """

    ICMPv6 Packet type\: Time exceeded

    """
    TIME_EXCEEDED = 3

    """

    ICMPv6 Packet type\: Parameter problem

    """
    PARAMETER_PROBLEM = 4

    """

    ICMPv6 Packet type\: Echo request

    """
    ECHO_REQUEST = 128

    """

    ICMPv6 Packet type\: Echo reply

    """
    ECHO_REPLY = 129

    """

    ICMPv6 Packet type\: Multicast listener query

    """
    MULTICAST_LISTENER_QUERY = 130

    """

    ICMPv6 Packet type\: Multicast listener report

    """
    MULTICAST_LISTENER_REPORT = 131

    """

    ICMPv6 Packet type\: Multicast listener done

    """
    MULTICAST_LISTENER_DONE = 132

    """

    ICMPv6 Packet type\: Router solicitation

    """
    ROUTER_SOLICITATION = 133

    """

    ICMPv6 Packet type\: Router advertisement

    """
    ROUTER_ADVERTISEMENT = 134

    """

    ICMPv6 Packet type\: Neighbor solicitation

    """
    NEIGHBOR_SOLICITATION = 135

    """

    ICMPv6 Packet type\: Neighbor advertisement

    """
    NEIGHBOR_ADVERTISEMENT = 136

    """

    ICMPv6 Packet type\: Redirect message

    """
    REDIRECT_MESSAGE = 137

    """

    ICMPv6 Packet type\: Router renumbering

    """
    ROUTER_RENUMBERING = 138

    """

    ICMPv6 Packet type\: Node information query

    """
    NODE_INFORMATION_QUERY = 139

    """

    ICMPv6 Packet type\: Node information reply

    """
    NODE_INFORMATION_REPLY = 140

    """

    ICMPv6 Packet type\: Inverse neighbor discovery
    solicitation message

    """
    INVERSE_NEIGHBOR_DISCOVERY_SOLICITAION = 141

    """

    ICMPv6 Packet type\: Inverse neighbor discovery
    advertisement message

    """
    INVERSE_NEIGHBOR_DISCOVER_ADVERTISEMENT = 142

    """

    ICMPv6 Packet type\: Version 2 multicast
    listener report

    """
    V2_MULTICAST_LISTENER_REPORT = 143

    """

    ICMPv6 Packet type\: Home agent address
    discovery request message

    """
    HOME_AGENT_ADDRESS_DISCOVERY_REQUEST = 144

    """

    ICMPv6 Packet type\: Home agent address
    discovery reply message

    """
    HOME_AGENT_ADDRESS_DISCOVERY_REPLY = 145

    """

    ICMPv6 Packet type\: Mobile prefix solicitation

    """
    MOBILE_PREFIX_SOLICITATION = 146

    """

    ICMPv6 Packet type\: Mobile prefix advertisement

    """
    MOBILE_PREFIX_ADVERTISEMENT = 147

    """

    ICMPv6 Packet type\: Certification path
    solicitation message

    """
    CERTIFICATION_PATH_SOLICITATION_MESSAGE = 148

    """

    ICMPv6 Packet type\: Certification path
    advertisement message

    """
    CERTIFICATION_PATH_ADVERTISEMENT_MESSAGE = 149

    """

    ICMPv6 Packet type\: ICMP messages utilized by
    experimental mobility  protocols such as
    seamoby

    """
    EXPERIMENTAL_MOBILITY_PROTOCOLS = 150

    """

    ICMPv6 Packet type\: Multicast router
    advertisement

    """
    MULTICAST_ROUTER_ADVERTISEMENT = 151

    """

    ICMPv6 Packet type\: Multicast router
    solicitation

    """
    MULTICAST_ROUTER_SOLICITATION = 152

    """

    ICMPv6 Packet type\: Multicast router
    termination

    """
    MULTICAST_ROUTER_TERMINATION = 153

    """

    ICMPv6 Packet type\: FMIPv6 messages

    """
    FMIPV6_MESSAGES = 154


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIcmpv6_Enum']


class MessageTypeIgmp_Enum(Enum):
    """
    MessageTypeIgmp_Enum

    LPTS IGMP message types

    """

    """

    IGMP Packet type\: Membership query

    """
    MEMBERSHIP_QUERY = 17

    """

    IGMP Packet type\: V1 membership report

    """
    V1_MEMBERSHIP_REPORT = 18

    """

    IGMP Packet type\: DVMRP

    """
    DVMRP = 19

    """

    IGMP Packet type\: PIM version 1

    """
    PI_MV1 = 20

    """

    IGMP Packet type\: Cisco Trace Messages

    """
    CISCO_TRACE_MESSAGES = 21

    """

    IGMP Packet type\: V2 membership report

    """
    V2_MEMBERSHIP_REPORT = 22

    """

    IGMP Packet type\: V2 leave group

    """
    V2_LEAVE_GROUP = 23

    """

    IGMP Packet type\: Multicast traceroute response

    """
    MULTICAST_TRACEROUTE_RESPONSE = 30

    """

    IGMP Packet type\: MulticastTraceroute

    """
    MULTICAST_TRACEROUTE = 31

    """

    IGMP Packet type\: V3 membership report

    """
    V3_MEMBERSHIP_REPORT = 34

    """

    IGMP Packet type\: Multicast router
    advertisement

    """
    MULTICAST_ROUTER_ADVERTISEMENT = 48

    """

    IGMP Packet type\: Multicast router solicitation

    """
    MULTICAST_ROUTER_SOLICITATION = 49

    """

    IGMP Packet type\: Multicast router termination

    """
    MULTICAST_ROUTER_TERMINATION = 50


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIgmp_Enum']


class MessageTypeIgmp_Enum(Enum):
    """
    MessageTypeIgmp_Enum

    LPTS IGMP message types

    """

    """

    IGMP Packet type\: Membership query

    """
    MEMBERSHIP_QUERY = 17

    """

    IGMP Packet type\: V1 membership report

    """
    V1_MEMBERSHIP_REPORT = 18

    """

    IGMP Packet type\: DVMRP

    """
    DVMRP = 19

    """

    IGMP Packet type\: PIM version 1

    """
    PI_MV1 = 20

    """

    IGMP Packet type\: Cisco Trace Messages

    """
    CISCO_TRACE_MESSAGES = 21

    """

    IGMP Packet type\: V2 membership report

    """
    V2_MEMBERSHIP_REPORT = 22

    """

    IGMP Packet type\: V2 leave group

    """
    V2_LEAVE_GROUP = 23

    """

    IGMP Packet type\: Multicast traceroute response

    """
    MULTICAST_TRACEROUTE_RESPONSE = 30

    """

    IGMP Packet type\: MulticastTraceroute

    """
    MULTICAST_TRACEROUTE = 31

    """

    IGMP Packet type\: V3 membership report

    """
    V3_MEMBERSHIP_REPORT = 34

    """

    IGMP Packet type\: Multicast router
    advertisement

    """
    MULTICAST_ROUTER_ADVERTISEMENT = 48

    """

    IGMP Packet type\: Multicast router solicitation

    """
    MULTICAST_ROUTER_SOLICITATION = 49

    """

    IGMP Packet type\: Multicast router termination

    """
    MULTICAST_ROUTER_TERMINATION = 50


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIgmp_Enum']


class Packet_Enum(Enum):
    """
    Packet_Enum

    Packet type

    """

    """

    ICMP packet type

    """
    ICMP = 0

    """

    ICMPv6 packet type

    """
    ICM_PV6 = 1

    """

    IGMP packet type

    """
    IGMP = 2

    """

    Packet type unknown

    """
    UNKNOWN = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['Packet_Enum']


class UdpAddressFamily_Enum(Enum):
    """
    UdpAddressFamily_Enum

    Address Family Type

    """

    """

    IPv4

    """
    IPV4 = 2

    """

    IPv6

    """
    IPV6 = 26


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['UdpAddressFamily_Enum']



class Udp(object):
    """
    IP UDP Operational Data
    
    .. attribute:: nodes
    
    	Node\-specific UDP operational data
    	**type**\: :py:class:`Nodes <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes>`
    
    

    """

    _prefix = 'ip-udp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Udp.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node\-specific UDP operational data
        
        .. attribute:: node
        
        	UDP operational data for a particular node
        	**type**\: list of :py:class:`Node <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node>`
        
        

        """

        _prefix = 'ip-udp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            UDP operational data for a particular node
            
            .. attribute:: node_name
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statistics
            
            	Statistical UDP operational data for a node
            	**type**\: :py:class:`Statistics <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ip-udp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.statistics = Udp.Nodes.Node.Statistics()
                self.statistics.parent = self


            class Statistics(object):
                """
                Statistical UDP operational data for a node
                
                .. attribute:: ipv4_traffic
                
                	UDP Traffic statistics for IPv4
                	**type**\: :py:class:`Ipv4Traffic <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node.Statistics.Ipv4Traffic>`
                
                .. attribute:: ipv6_traffic
                
                	UDP Traffic statistics for IPv6
                	**type**\: :py:class:`Ipv6Traffic <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node.Statistics.Ipv6Traffic>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ipv4_traffic = Udp.Nodes.Node.Statistics.Ipv4Traffic()
                    self.ipv4_traffic.parent = self
                    self.ipv6_traffic = Udp.Nodes.Node.Statistics.Ipv6Traffic()
                    self.ipv6_traffic.parent = self


                class Ipv4Traffic(object):
                    """
                    UDP Traffic statistics for IPv4
                    
                    .. attribute:: udp_bad_length_packets
                    
                    	UDP bad length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_checksum_error_packets
                    
                    	UDP Checksum Errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_dropped_packets
                    
                    	UDP drop for other reason
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_input_packets
                    
                    	UDP Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_no_port_packets
                    
                    	UDP No Port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_output_packets
                    
                    	UDP Transmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.udp_bad_length_packets = None
                        self.udp_checksum_error_packets = None
                        self.udp_dropped_packets = None
                        self.udp_input_packets = None
                        self.udp_no_port_packets = None
                        self.udp_output_packets = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:ipv4-traffic'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.udp_bad_length_packets is not None:
                            return True

                        if self.udp_checksum_error_packets is not None:
                            return True

                        if self.udp_dropped_packets is not None:
                            return True

                        if self.udp_input_packets is not None:
                            return True

                        if self.udp_no_port_packets is not None:
                            return True

                        if self.udp_output_packets is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['Udp.Nodes.Node.Statistics.Ipv4Traffic']['meta_info']


                class Ipv6Traffic(object):
                    """
                    UDP Traffic statistics for IPv6
                    
                    .. attribute:: udp_bad_length_packets
                    
                    	UDP bad length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_checksum_error_packets
                    
                    	UDP Checksum Errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_dropped_packets
                    
                    	UDP drop for other reason
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_input_packets
                    
                    	UDP Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_no_port_packets
                    
                    	UDP No Port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_output_packets
                    
                    	UDP Transmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.udp_bad_length_packets = None
                        self.udp_checksum_error_packets = None
                        self.udp_dropped_packets = None
                        self.udp_input_packets = None
                        self.udp_no_port_packets = None
                        self.udp_output_packets = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:ipv6-traffic'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.udp_bad_length_packets is not None:
                            return True

                        if self.udp_checksum_error_packets is not None:
                            return True

                        if self.udp_dropped_packets is not None:
                            return True

                        if self.udp_input_packets is not None:
                            return True

                        if self.udp_no_port_packets is not None:
                            return True

                        if self.udp_output_packets is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['Udp.Nodes.Node.Statistics.Ipv6Traffic']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ipv4_traffic is not None and self.ipv4_traffic._has_data():
                        return True

                    if self.ipv4_traffic is not None and self.ipv4_traffic.is_presence():
                        return True

                    if self.ipv6_traffic is not None and self.ipv6_traffic._has_data():
                        return True

                    if self.ipv6_traffic is not None and self.ipv6_traffic.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                    return meta._meta_table['Udp.Nodes.Node.Statistics']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYDataValidationError('Key property node_name is None')

                return '/Cisco-IOS-XR-ip-udp-oper:udp/Cisco-IOS-XR-ip-udp-oper:nodes/Cisco-IOS-XR-ip-udp-oper:node[Cisco-IOS-XR-ip-udp-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.node_name is not None:
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                if self.statistics is not None and self.statistics.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                return meta._meta_table['Udp.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-udp-oper:udp/Cisco-IOS-XR-ip-udp-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
            return meta._meta_table['Udp.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-udp-oper:udp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.nodes is not None and self.nodes._has_data():
            return True

        if self.nodes is not None and self.nodes.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['Udp']['meta_info']


class UdpConnection(object):
    """
    udp connection
    
    .. attribute:: nodes
    
    	List of UDP connections nodes
    	**type**\: :py:class:`Nodes <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes>`
    
    

    """

    _prefix = 'ip-udp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = UdpConnection.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of UDP connections nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of :py:class:`Node <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node>`
        
        

        """

        _prefix = 'ip-udp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Information about a particular node
            
            .. attribute:: node_name
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: lpts
            
            	LPTS statistical data
            	**type**\: :py:class:`Lpts <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts>`
            
            .. attribute:: pcb_briefs
            
            	Brief information for list of UDP connections
            	**type**\: :py:class:`PcbBriefs <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs>`
            
            .. attribute:: pcb_details
            
            	Detail information for list of UDP connections 
            	**type**\: :py:class:`PcbDetails <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails>`
            
            .. attribute:: statistics
            
            	Statistics of UDP connections
            	**type**\: :py:class:`Statistics <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ip-udp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.lpts = UdpConnection.Nodes.Node.Lpts()
                self.lpts.parent = self
                self.pcb_briefs = UdpConnection.Nodes.Node.PcbBriefs()
                self.pcb_briefs.parent = self
                self.pcb_details = UdpConnection.Nodes.Node.PcbDetails()
                self.pcb_details.parent = self
                self.statistics = UdpConnection.Nodes.Node.Statistics()
                self.statistics.parent = self


            class Lpts(object):
                """
                LPTS statistical data
                
                .. attribute:: queries
                
                	List of query options
                	**type**\: :py:class:`Queries <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.queries = UdpConnection.Nodes.Node.Lpts.Queries()
                    self.queries.parent = self


                class Queries(object):
                    """
                    List of query options
                    
                    .. attribute:: query
                    
                    	Query option
                    	**type**\: list of :py:class:`Query <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.query = YList()
                        self.query.parent = self
                        self.query.name = 'query'


                    class Query(object):
                        """
                        Query option
                        
                        .. attribute:: query_name
                        
                        	Query option
                        	**type**\: :py:class:`LptsPcbQuery_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.LptsPcbQuery_Enum>`
                        
                        .. attribute:: pcbs
                        
                        	List of PCBs
                        	**type**\: :py:class:`Pcbs <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs>`
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.query_name = None
                            self.pcbs = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs()
                            self.pcbs.parent = self


                        class Pcbs(object):
                            """
                            List of PCBs
                            
                            .. attribute:: pcb
                            
                            	A PCB information
                            	**type**\: list of :py:class:`Pcb <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb>`
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.pcb = YList()
                                self.pcb.parent = self
                                self.pcb.name = 'pcb'


                            class Pcb(object):
                                """
                                A PCB information
                                
                                .. attribute:: pcb_address
                                
                                	PCB address
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: common
                                
                                	Common PCB information
                                	**type**\: :py:class:`Common <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common>`
                                
                                .. attribute:: foreign_address
                                
                                	Remote IP address
                                	**type**\: :py:class:`ForeignAddress <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress>`
                                
                                .. attribute:: foreign_port
                                
                                	Remote port
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: l4_protocol
                                
                                	Layer 4 protocol
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: local_address
                                
                                	Local IP address
                                	**type**\: :py:class:`LocalAddress <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress>`
                                
                                .. attribute:: local_port
                                
                                	Local port
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ip-udp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.pcb_address = None
                                    self.common = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common()
                                    self.common.parent = self
                                    self.foreign_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress()
                                    self.foreign_address.parent = self
                                    self.foreign_port = None
                                    self.l4_protocol = None
                                    self.local_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress()
                                    self.local_address.parent = self
                                    self.local_port = None


                                class Common(object):
                                    """
                                    Common PCB information
                                    
                                    .. attribute:: af_name
                                    
                                    	Address Family
                                    	**type**\: :py:class:`AddrFamily_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.AddrFamily_Enum>`
                                    
                                    .. attribute:: lpts_pcb
                                    
                                    	LPTS PCB information
                                    	**type**\: :py:class:`LptsPcb <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb>`
                                    
                                    

                                    """

                                    _prefix = 'ip-udp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.af_name = None
                                        self.lpts_pcb = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb()
                                        self.lpts_pcb.parent = self


                                    class LptsPcb(object):
                                        """
                                        LPTS PCB information
                                        
                                        .. attribute:: accept_mask
                                        
                                        	AcceptMask
                                        	**type**\: :py:class:`AcceptMask <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask>`
                                        
                                        .. attribute:: filter
                                        
                                        	Interface Filters
                                        	**type**\: list of :py:class:`Filter <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter>`
                                        
                                        .. attribute:: flow_types_info
                                        
                                        	flow information
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lpts_flags
                                        
                                        	LPTS flags
                                        	**type**\: :py:class:`LptsFlags <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags>`
                                        
                                        .. attribute:: options
                                        
                                        	Receive options
                                        	**type**\: :py:class:`Options <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options>`
                                        
                                        .. attribute:: ttl
                                        
                                        	Minimum TTL
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ip-udp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.accept_mask = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask()
                                            self.accept_mask.parent = self
                                            self.filter = YList()
                                            self.filter.parent = self
                                            self.filter.name = 'filter'
                                            self.flow_types_info = None
                                            self.lpts_flags = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags()
                                            self.lpts_flags.parent = self
                                            self.options = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options()
                                            self.options.parent = self
                                            self.ttl = None


                                        class AcceptMask(object):
                                            """
                                            AcceptMask
                                            
                                            .. attribute:: is_interface
                                            
                                            	Set interface
                                            	**type**\: bool
                                            
                                            .. attribute:: is_local_address
                                            
                                            	Set Local Address
                                            	**type**\: bool
                                            
                                            .. attribute:: is_local_port
                                            
                                            	Set Local Port
                                            	**type**\: bool
                                            
                                            .. attribute:: is_packet_type
                                            
                                            	Set packet type
                                            	**type**\: bool
                                            
                                            .. attribute:: is_remote_address
                                            
                                            	Set Remote address
                                            	**type**\: bool
                                            
                                            .. attribute:: is_remote_port
                                            
                                            	Set Remote Port
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'ip-udp-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.is_interface = None
                                                self.is_local_address = None
                                                self.is_local_port = None
                                                self.is_packet_type = None
                                                self.is_remote_address = None
                                                self.is_remote_port = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:accept-mask'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.is_interface is not None:
                                                    return True

                                                if self.is_local_address is not None:
                                                    return True

                                                if self.is_local_port is not None:
                                                    return True

                                                if self.is_packet_type is not None:
                                                    return True

                                                if self.is_remote_address is not None:
                                                    return True

                                                if self.is_remote_port is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask']['meta_info']


                                        class Filter(object):
                                            """
                                            Interface Filters
                                            
                                            .. attribute:: flow_types_info
                                            
                                            	flow information
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: interface_name
                                            
                                            	Interface name
                                            	**type**\: str
                                            
                                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                            
                                            .. attribute:: local_address
                                            
                                            	Local address
                                            	**type**\: :py:class:`LocalAddress <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress>`
                                            
                                            .. attribute:: local_length
                                            
                                            	Local address length
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: packet_type
                                            
                                            	Protocol\-specific packet type
                                            	**type**\: :py:class:`PacketType <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType>`
                                            
                                            .. attribute:: priority
                                            
                                            	Priority
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: receive_local_port
                                            
                                            	Receive Local port
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: receive_remote_port
                                            
                                            	Receive Remote port
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: remote_address
                                            
                                            	Remote address
                                            	**type**\: :py:class:`RemoteAddress <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress>`
                                            
                                            .. attribute:: remote_length
                                            
                                            	Remote address length
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: ttl
                                            
                                            	Minimum TTL
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'ip-udp-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.flow_types_info = None
                                                self.interface_name = None
                                                self.local_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress()
                                                self.local_address.parent = self
                                                self.local_length = None
                                                self.packet_type = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType()
                                                self.packet_type.parent = self
                                                self.priority = None
                                                self.receive_local_port = None
                                                self.receive_remote_port = None
                                                self.remote_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress()
                                                self.remote_address.parent = self
                                                self.remote_length = None
                                                self.ttl = None


                                            class LocalAddress(object):
                                                """
                                                Local address
                                                
                                                .. attribute:: af_name
                                                
                                                	AFName
                                                	**type**\: :py:class:`AddrFamily_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.AddrFamily_Enum>`
                                                
                                                .. attribute:: ipv4_address
                                                
                                                	IPv4 address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: ipv6_address
                                                
                                                	IPv6 address
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                

                                                """

                                                _prefix = 'ip-udp-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.af_name = None
                                                    self.ipv4_address = None
                                                    self.ipv6_address = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:local-address'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.is_presence():
                                                        return True
                                                    if self.af_name is not None:
                                                        return True

                                                    if self.ipv4_address is not None:
                                                        return True

                                                    if self.ipv6_address is not None:
                                                        return True

                                                    return False

                                                def is_presence(self):
                                                    ''' Returns True if this instance represents presence container else returns False '''
                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                    return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress']['meta_info']


                                            class PacketType(object):
                                                """
                                                Protocol\-specific packet type
                                                
                                                .. attribute:: icm_pv6_message_type
                                                
                                                	ICMPv6 message type
                                                	**type**\: :py:class:`MessageTypeIcmpv6_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.MessageTypeIcmpv6_Enum>`
                                                
                                                .. attribute:: icmp_message_type
                                                
                                                	ICMP message type
                                                	**type**\: :py:class:`MessageTypeIcmp_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.MessageTypeIcmp_Enum>`
                                                
                                                .. attribute:: igmp_message_type
                                                
                                                	IGMP message type
                                                	**type**\: :py:class:`MessageTypeIgmp_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.MessageTypeIgmp_Enum>`
                                                
                                                .. attribute:: message_id
                                                
                                                	Message type in number
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: type
                                                
                                                	Type
                                                	**type**\: :py:class:`Packet_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.Packet_Enum>`
                                                
                                                

                                                """

                                                _prefix = 'ip-udp-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.icm_pv6_message_type = None
                                                    self.icmp_message_type = None
                                                    self.igmp_message_type = None
                                                    self.message_id = None
                                                    self.type = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:packet-type'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.is_presence():
                                                        return True
                                                    if self.icm_pv6_message_type is not None:
                                                        return True

                                                    if self.icmp_message_type is not None:
                                                        return True

                                                    if self.igmp_message_type is not None:
                                                        return True

                                                    if self.message_id is not None:
                                                        return True

                                                    if self.type is not None:
                                                        return True

                                                    return False

                                                def is_presence(self):
                                                    ''' Returns True if this instance represents presence container else returns False '''
                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                    return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType']['meta_info']


                                            class RemoteAddress(object):
                                                """
                                                Remote address
                                                
                                                .. attribute:: af_name
                                                
                                                	AFName
                                                	**type**\: :py:class:`AddrFamily_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.AddrFamily_Enum>`
                                                
                                                .. attribute:: ipv4_address
                                                
                                                	IPv4 address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: ipv6_address
                                                
                                                	IPv6 address
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                

                                                """

                                                _prefix = 'ip-udp-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.af_name = None
                                                    self.ipv4_address = None
                                                    self.ipv6_address = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:remote-address'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.is_presence():
                                                        return True
                                                    if self.af_name is not None:
                                                        return True

                                                    if self.ipv4_address is not None:
                                                        return True

                                                    if self.ipv6_address is not None:
                                                        return True

                                                    return False

                                                def is_presence(self):
                                                    ''' Returns True if this instance represents presence container else returns False '''
                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                    return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:filter'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.flow_types_info is not None:
                                                    return True

                                                if self.interface_name is not None:
                                                    return True

                                                if self.local_address is not None and self.local_address._has_data():
                                                    return True

                                                if self.local_address is not None and self.local_address.is_presence():
                                                    return True

                                                if self.local_length is not None:
                                                    return True

                                                if self.packet_type is not None and self.packet_type._has_data():
                                                    return True

                                                if self.packet_type is not None and self.packet_type.is_presence():
                                                    return True

                                                if self.priority is not None:
                                                    return True

                                                if self.receive_local_port is not None:
                                                    return True

                                                if self.receive_remote_port is not None:
                                                    return True

                                                if self.remote_address is not None and self.remote_address._has_data():
                                                    return True

                                                if self.remote_address is not None and self.remote_address.is_presence():
                                                    return True

                                                if self.remote_length is not None:
                                                    return True

                                                if self.ttl is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter']['meta_info']


                                        class LptsFlags(object):
                                            """
                                            LPTS flags
                                            
                                            .. attribute:: is_ignore_vrf_filter
                                            
                                            	Ignore VRF Filter
                                            	**type**\: bool
                                            
                                            .. attribute:: is_local_address_ignore
                                            
                                            	Sent drop packets
                                            	**type**\: bool
                                            
                                            .. attribute:: is_pcb_bound
                                            
                                            	PCB bound
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'ip-udp-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.is_ignore_vrf_filter = None
                                                self.is_local_address_ignore = None
                                                self.is_pcb_bound = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:lpts-flags'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.is_ignore_vrf_filter is not None:
                                                    return True

                                                if self.is_local_address_ignore is not None:
                                                    return True

                                                if self.is_pcb_bound is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags']['meta_info']


                                        class Options(object):
                                            """
                                            Receive options
                                            
                                            .. attribute:: is_ip_sla
                                            
                                            	IP SLA
                                            	**type**\: bool
                                            
                                            .. attribute:: is_receive_filter
                                            
                                            	Receive filter enabled
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'ip-udp-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.is_ip_sla = None
                                                self.is_receive_filter = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:options'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.is_ip_sla is not None:
                                                    return True

                                                if self.is_receive_filter is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:lpts-pcb'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.accept_mask is not None and self.accept_mask._has_data():
                                                return True

                                            if self.accept_mask is not None and self.accept_mask.is_presence():
                                                return True

                                            if self.filter is not None:
                                                for child_ref in self.filter:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.flow_types_info is not None:
                                                return True

                                            if self.lpts_flags is not None and self.lpts_flags._has_data():
                                                return True

                                            if self.lpts_flags is not None and self.lpts_flags.is_presence():
                                                return True

                                            if self.options is not None and self.options._has_data():
                                                return True

                                            if self.options is not None and self.options.is_presence():
                                                return True

                                            if self.ttl is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                            return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:common'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.af_name is not None:
                                            return True

                                        if self.lpts_pcb is not None and self.lpts_pcb._has_data():
                                            return True

                                        if self.lpts_pcb is not None and self.lpts_pcb.is_presence():
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                        return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common']['meta_info']


                                class ForeignAddress(object):
                                    """
                                    Remote IP address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\: :py:class:`AddrFamily_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.AddrFamily_Enum>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-udp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.af_name = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:foreign-address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.af_name is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                        return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress']['meta_info']


                                class LocalAddress(object):
                                    """
                                    Local IP address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\: :py:class:`AddrFamily_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.AddrFamily_Enum>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-udp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.af_name = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:local-address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.af_name is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                        return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.pcb_address is None:
                                        raise YPYDataValidationError('Key property pcb_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb[Cisco-IOS-XR-ip-udp-oper:pcb-address = ' + str(self.pcb_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.pcb_address is not None:
                                        return True

                                    if self.common is not None and self.common._has_data():
                                        return True

                                    if self.common is not None and self.common.is_presence():
                                        return True

                                    if self.foreign_address is not None and self.foreign_address._has_data():
                                        return True

                                    if self.foreign_address is not None and self.foreign_address.is_presence():
                                        return True

                                    if self.foreign_port is not None:
                                        return True

                                    if self.l4_protocol is not None:
                                        return True

                                    if self.local_address is not None and self.local_address._has_data():
                                        return True

                                    if self.local_address is not None and self.local_address.is_presence():
                                        return True

                                    if self.local_port is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                    return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcbs'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.pcb is not None:
                                    for child_ref in self.pcb:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.query_name is None:
                                raise YPYDataValidationError('Key property query_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:query[Cisco-IOS-XR-ip-udp-oper:query-name = ' + str(self.query_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.query_name is not None:
                                return True

                            if self.pcbs is not None and self.pcbs._has_data():
                                return True

                            if self.pcbs is not None and self.pcbs.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:queries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.query is not None:
                            for child_ref in self.query:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:lpts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.queries is not None and self.queries._has_data():
                        return True

                    if self.queries is not None and self.queries.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                    return meta._meta_table['UdpConnection.Nodes.Node.Lpts']['meta_info']


            class PcbBriefs(object):
                """
                Brief information for list of UDP connections.
                
                .. attribute:: pcb_brief
                
                	Brief information about a UDP connection
                	**type**\: list of :py:class:`PcbBrief <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.pcb_brief = YList()
                    self.pcb_brief.parent = self
                    self.pcb_brief.name = 'pcb_brief'


                class PcbBrief(object):
                    """
                    Brief information about a UDP connection
                    
                    .. attribute:: pcb_address
                    
                    	Protocol Control Block address
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: af_name
                    
                    	Address family
                    	**type**\: :py:class:`UdpAddressFamily_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily_Enum>`
                    
                    .. attribute:: foreign_address
                    
                    	Foreign address
                    	**type**\: :py:class:`ForeignAddress <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress>`
                    
                    .. attribute:: foreign_port
                    
                    	Foreign port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\: :py:class:`LocalAddress <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress>`
                    
                    .. attribute:: local_port
                    
                    	Local port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: receive_queue
                    
                    	Receive queue count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_queue
                    
                    	Send queue count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.pcb_address = None
                        self.af_name = None
                        self.foreign_address = UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress()
                        self.foreign_address.parent = self
                        self.foreign_port = None
                        self.local_address = UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress()
                        self.local_address.parent = self
                        self.local_port = None
                        self.receive_queue = None
                        self.send_queue = None


                    class ForeignAddress(object):
                        """
                        Foreign address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\: :py:class:`UdpAddressFamily_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily_Enum>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:foreign-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress']['meta_info']


                    class LocalAddress(object):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\: :py:class:`UdpAddressFamily_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily_Enum>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:local-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.pcb_address is None:
                            raise YPYDataValidationError('Key property pcb_address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb-brief[Cisco-IOS-XR-ip-udp-oper:pcb-address = ' + str(self.pcb_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.pcb_address is not None:
                            return True

                        if self.af_name is not None:
                            return True

                        if self.foreign_address is not None and self.foreign_address._has_data():
                            return True

                        if self.foreign_address is not None and self.foreign_address.is_presence():
                            return True

                        if self.foreign_port is not None:
                            return True

                        if self.local_address is not None and self.local_address._has_data():
                            return True

                        if self.local_address is not None and self.local_address.is_presence():
                            return True

                        if self.local_port is not None:
                            return True

                        if self.receive_queue is not None:
                            return True

                        if self.send_queue is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb-briefs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.pcb_brief is not None:
                        for child_ref in self.pcb_brief:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                    return meta._meta_table['UdpConnection.Nodes.Node.PcbBriefs']['meta_info']


            class PcbDetails(object):
                """
                Detail information for list of UDP connections
                .
                
                .. attribute:: pcb_detail
                
                	Detail information about a UDP connection
                	**type**\: list of :py:class:`PcbDetail <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails.PcbDetail>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.pcb_detail = YList()
                    self.pcb_detail.parent = self
                    self.pcb_detail.name = 'pcb_detail'


                class PcbDetail(object):
                    """
                    Detail information about a UDP connection
                    
                    .. attribute:: pcb_address
                    
                    	Protocol Control Block address
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: af_name
                    
                    	Address family
                    	**type**\: :py:class:`UdpAddressFamily_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily_Enum>`
                    
                    .. attribute:: foreign_address
                    
                    	Foreign address
                    	**type**\: :py:class:`ForeignAddress <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress>`
                    
                    .. attribute:: foreign_port
                    
                    	Foreign port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\: :py:class:`LocalAddress <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress>`
                    
                    .. attribute:: local_port
                    
                    	Local port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_process_id
                    
                    	ID of local process
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_queue
                    
                    	Receive queue count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_queue
                    
                    	Send queue count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.pcb_address = None
                        self.af_name = None
                        self.foreign_address = UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress()
                        self.foreign_address.parent = self
                        self.foreign_port = None
                        self.local_address = UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress()
                        self.local_address.parent = self
                        self.local_port = None
                        self.local_process_id = None
                        self.receive_queue = None
                        self.send_queue = None


                    class ForeignAddress(object):
                        """
                        Foreign address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\: :py:class:`UdpAddressFamily_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily_Enum>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:foreign-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress']['meta_info']


                    class LocalAddress(object):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\: :py:class:`UdpAddressFamily_Enum <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily_Enum>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:local-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.pcb_address is None:
                            raise YPYDataValidationError('Key property pcb_address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb-detail[Cisco-IOS-XR-ip-udp-oper:pcb-address = ' + str(self.pcb_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.pcb_address is not None:
                            return True

                        if self.af_name is not None:
                            return True

                        if self.foreign_address is not None and self.foreign_address._has_data():
                            return True

                        if self.foreign_address is not None and self.foreign_address.is_presence():
                            return True

                        if self.foreign_port is not None:
                            return True

                        if self.local_address is not None and self.local_address._has_data():
                            return True

                        if self.local_address is not None and self.local_address.is_presence():
                            return True

                        if self.local_port is not None:
                            return True

                        if self.local_process_id is not None:
                            return True

                        if self.receive_queue is not None:
                            return True

                        if self.send_queue is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb-details'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.pcb_detail is not None:
                        for child_ref in self.pcb_detail:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                    return meta._meta_table['UdpConnection.Nodes.Node.PcbDetails']['meta_info']


            class Statistics(object):
                """
                Statistics of UDP connections
                
                .. attribute:: clients
                
                	Table listing clients
                	**type**\: :py:class:`Clients <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Clients>`
                
                .. attribute:: pcb_statistics
                
                	Table listing the UDP connections for which statistics are provided
                	**type**\: :py:class:`PcbStatistics <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics>`
                
                .. attribute:: summary
                
                	Summary statistics across all UDP connections
                	**type**\: :py:class:`Summary <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Summary>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.clients = UdpConnection.Nodes.Node.Statistics.Clients()
                    self.clients.parent = self
                    self.pcb_statistics = UdpConnection.Nodes.Node.Statistics.PcbStatistics()
                    self.pcb_statistics.parent = self
                    self.summary = UdpConnection.Nodes.Node.Statistics.Summary()
                    self.summary.parent = self


                class Clients(object):
                    """
                    Table listing clients
                    
                    .. attribute:: client
                    
                    	Describing Client ID
                    	**type**\: list of :py:class:`Client <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Clients.Client>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.client = YList()
                        self.client.parent = self
                        self.client.name = 'client'


                    class Client(object):
                        """
                        Describing Client ID
                        
                        .. attribute:: client_id
                        
                        	Displaying client's aggregated statistics
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: client_jid
                        
                        	Job ID of the transport client
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: client_name
                        
                        	Transport client name
                        	**type**\: str
                        
                        	**range:** 0..21
                        
                        .. attribute:: ipv4_received_packets
                        
                        	Total IPv4 packets received from client
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv4_sent_packets
                        
                        	Total IPv4 packets sent to client
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv6_received_packets
                        
                        	Total IPv6 packets received from app
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv6_sent_packets
                        
                        	Total IPv6 packets sent to app
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.client_id = None
                            self.client_jid = None
                            self.client_name = None
                            self.ipv4_received_packets = None
                            self.ipv4_sent_packets = None
                            self.ipv6_received_packets = None
                            self.ipv6_sent_packets = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.client_id is None:
                                raise YPYDataValidationError('Key property client_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:client[Cisco-IOS-XR-ip-udp-oper:client-id = ' + str(self.client_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.client_id is not None:
                                return True

                            if self.client_jid is not None:
                                return True

                            if self.client_name is not None:
                                return True

                            if self.ipv4_received_packets is not None:
                                return True

                            if self.ipv4_sent_packets is not None:
                                return True

                            if self.ipv6_received_packets is not None:
                                return True

                            if self.ipv6_sent_packets is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.Statistics.Clients.Client']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:clients'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.client is not None:
                            for child_ref in self.client:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['UdpConnection.Nodes.Node.Statistics.Clients']['meta_info']


                class PcbStatistics(object):
                    """
                    Table listing the UDP connections for which
                    statistics are provided
                    
                    .. attribute:: pcb_statistic
                    
                    	Satistics associated with a particular PCB
                    	**type**\: list of :py:class:`PcbStatistic <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.pcb_statistic = YList()
                        self.pcb_statistic.parent = self
                        self.pcb_statistic.name = 'pcb_statistic'


                    class PcbStatistic(object):
                        """
                        Satistics associated with a particular PCB
                        
                        .. attribute:: pcb_address
                        
                        	Protocol Control Block address
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_paw_socket
                        
                        	True if paw socket
                        	**type**\: bool
                        
                        .. attribute:: receive
                        
                        	UDP receive statistics
                        	**type**\: :py:class:`Receive <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive>`
                        
                        .. attribute:: send
                        
                        	UDP send statistics
                        	**type**\: :py:class:`Send <ydk.models.ip.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send>`
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.pcb_address = None
                            self.is_paw_socket = None
                            self.receive = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive()
                            self.receive.parent = self
                            self.send = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send()
                            self.send.parent = self


                        class Receive(object):
                            """
                            UDP receive statistics
                            
                            .. attribute:: failed_queued_application_packets
                            
                            	Packets failed queued to application
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: failed_queued_application_socket_packets
                            
                            	Packet that couldn't be queued to application.on socket
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: queued_application_packets
                            
                            	Packets queued to application
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: queued_application_socket_packets
                            
                            	Packets queued to application on socket
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: received_network_packets
                            
                            	Packets received from network
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.failed_queued_application_packets = None
                                self.failed_queued_application_socket_packets = None
                                self.queued_application_packets = None
                                self.queued_application_socket_packets = None
                                self.received_network_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:receive'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.failed_queued_application_packets is not None:
                                    return True

                                if self.failed_queued_application_socket_packets is not None:
                                    return True

                                if self.queued_application_packets is not None:
                                    return True

                                if self.queued_application_socket_packets is not None:
                                    return True

                                if self.received_network_packets is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                return meta._meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive']['meta_info']


                        class Send(object):
                            """
                            UDP send statistics
                            
                            .. attribute:: failed_queued_net_io_packets
                            
                            	Packets failed getting queued to network (NetIO)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: failed_queued_network_packets
                            
                            	Packets failed getting queued to network (v4/v6 IO)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: received_application_bytes
                            
                            	Bytes received from application
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: received_xipc_pulses
                            
                            	XIPC pulses received from application
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_net_io_packets
                            
                            	Packets sent to network (NetIO)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_network_packets
                            
                            	Packets sent to network (v4/v6 IO)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.failed_queued_net_io_packets = None
                                self.failed_queued_network_packets = None
                                self.received_application_bytes = None
                                self.received_xipc_pulses = None
                                self.sent_net_io_packets = None
                                self.sent_network_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:send'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.failed_queued_net_io_packets is not None:
                                    return True

                                if self.failed_queued_network_packets is not None:
                                    return True

                                if self.received_application_bytes is not None:
                                    return True

                                if self.received_xipc_pulses is not None:
                                    return True

                                if self.sent_net_io_packets is not None:
                                    return True

                                if self.sent_network_packets is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                return meta._meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.pcb_address is None:
                                raise YPYDataValidationError('Key property pcb_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb-statistic[Cisco-IOS-XR-ip-udp-oper:pcb-address = ' + str(self.pcb_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.pcb_address is not None:
                                return True

                            if self.is_paw_socket is not None:
                                return True

                            if self.receive is not None and self.receive._has_data():
                                return True

                            if self.receive is not None and self.receive.is_presence():
                                return True

                            if self.send is not None and self.send._has_data():
                                return True

                            if self.send is not None and self.send.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.pcb_statistic is not None:
                            for child_ref in self.pcb_statistic:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics']['meta_info']


                class Summary(object):
                    """
                    Summary statistics across all UDP connections
                    
                    .. attribute:: cloned_packets
                    
                    	Total cloned packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: failed_clone_packets
                    
                    	Total failed cloned packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: forward_broadcast_packets
                    
                    	Total forwarding broadcast packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_bad_checksum_packets
                    
                    	Packets received has bad checksum
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_drop_packets
                    
                    	Packets dropped for other reasons
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_no_port_packets
                    
                    	Packets received when no wild listener
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_too_short_packets
                    
                    	Packets received is too short
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_total_packets
                    
                    	Total packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent_error_packets
                    
                    	Total send erorr packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent_total_packets
                    
                    	Total packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.cloned_packets = None
                        self.failed_clone_packets = None
                        self.forward_broadcast_packets = None
                        self.received_bad_checksum_packets = None
                        self.received_drop_packets = None
                        self.received_no_port_packets = None
                        self.received_too_short_packets = None
                        self.received_total_packets = None
                        self.sent_error_packets = None
                        self.sent_total_packets = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.cloned_packets is not None:
                            return True

                        if self.failed_clone_packets is not None:
                            return True

                        if self.forward_broadcast_packets is not None:
                            return True

                        if self.received_bad_checksum_packets is not None:
                            return True

                        if self.received_drop_packets is not None:
                            return True

                        if self.received_no_port_packets is not None:
                            return True

                        if self.received_too_short_packets is not None:
                            return True

                        if self.received_total_packets is not None:
                            return True

                        if self.sent_error_packets is not None:
                            return True

                        if self.sent_total_packets is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['UdpConnection.Nodes.Node.Statistics.Summary']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.clients is not None and self.clients._has_data():
                        return True

                    if self.clients is not None and self.clients.is_presence():
                        return True

                    if self.pcb_statistics is not None and self.pcb_statistics._has_data():
                        return True

                    if self.pcb_statistics is not None and self.pcb_statistics.is_presence():
                        return True

                    if self.summary is not None and self.summary._has_data():
                        return True

                    if self.summary is not None and self.summary.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                    return meta._meta_table['UdpConnection.Nodes.Node.Statistics']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYDataValidationError('Key property node_name is None')

                return '/Cisco-IOS-XR-ip-udp-oper:udp-connection/Cisco-IOS-XR-ip-udp-oper:nodes/Cisco-IOS-XR-ip-udp-oper:node[Cisco-IOS-XR-ip-udp-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.node_name is not None:
                    return True

                if self.lpts is not None and self.lpts._has_data():
                    return True

                if self.lpts is not None and self.lpts.is_presence():
                    return True

                if self.pcb_briefs is not None and self.pcb_briefs._has_data():
                    return True

                if self.pcb_briefs is not None and self.pcb_briefs.is_presence():
                    return True

                if self.pcb_details is not None and self.pcb_details._has_data():
                    return True

                if self.pcb_details is not None and self.pcb_details.is_presence():
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                if self.statistics is not None and self.statistics.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                return meta._meta_table['UdpConnection.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-udp-oper:udp-connection/Cisco-IOS-XR-ip-udp-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
            return meta._meta_table['UdpConnection.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-udp-oper:udp-connection'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.nodes is not None and self.nodes._has_data():
            return True

        if self.nodes is not None and self.nodes.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['UdpConnection']['meta_info']

