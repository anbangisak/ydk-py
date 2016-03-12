""" Cisco_IOS_XR_ip_iep_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-iep package operational data.

This module contains definitions
for the following management objects\:
  explicit\-paths\: Configured IP explicit paths

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class IepAddress_Enum(Enum):
    """
    IepAddress_Enum

    Address types

    """

    """

    Address type is next

    """
    NEXT = 0

    """

    Address type is exclude

    """
    EXCLUDE = 1

    """

    Address type is exclude SRLG

    """
    EXCLUDE_SRLG = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_oper as meta
        return meta._meta_table['IepAddress_Enum']


class IepHop_Enum(Enum):
    """
    IepHop_Enum

    Hop types of the next\-address configured

    """

    """

    Hop type is strict

    """
    STRICT = 0

    """

    Hop type is loose

    """
    LOOSE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_oper as meta
        return meta._meta_table['IepHop_Enum']


class IepStatus_Enum(Enum):
    """
    IepStatus_Enum

    Status of the path

    """

    """

    Status is enabled

    """
    ENABLED = 0

    """

    Status is disabled

    """
    DISABLED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_oper as meta
        return meta._meta_table['IepStatus_Enum']



class ExplicitPaths(object):
    """
    Configured IP explicit paths
    
    .. attribute:: identifiers
    
    	List of configured IP explicit path identifiers
    	**type**\: :py:class:`Identifiers <ydk.models.ip.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Identifiers>`
    
    .. attribute:: names
    
    	List of configured IP explicit path names
    	**type**\: :py:class:`Names <ydk.models.ip.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Names>`
    
    

    """

    _prefix = 'ip-iep-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.identifiers = ExplicitPaths.Identifiers()
        self.identifiers.parent = self
        self.names = ExplicitPaths.Names()
        self.names.parent = self


    class Identifiers(object):
        """
        List of configured IP explicit path identifiers
        
        .. attribute:: identifier
        
        	IP explicit path configured for a particular identifier
        	**type**\: list of :py:class:`Identifier <ydk.models.ip.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Identifiers.Identifier>`
        
        

        """

        _prefix = 'ip-iep-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.identifier = YList()
            self.identifier.parent = self
            self.identifier.name = 'identifier'


        class Identifier(object):
            """
            IP explicit path configured for a particular
            identifier
            
            .. attribute:: identifier_id
            
            	Identifier ID
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: address
            
            	List of IP addresses configured in the explicit path
            	**type**\: list of :py:class:`Address <ydk.models.ip.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Identifiers.Identifier.Address>`
            
            .. attribute:: status
            
            	Status of the path
            	**type**\: :py:class:`IepStatus_Enum <ydk.models.ip.Cisco_IOS_XR_ip_iep_oper.IepStatus_Enum>`
            
            

            """

            _prefix = 'ip-iep-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.identifier_id = None
                self.address = YList()
                self.address.parent = self
                self.address.name = 'address'
                self.status = None


            class Address(object):
                """
                List of IP addresses configured in the explicit
                path
                
                .. attribute:: address
                
                	IPv4 unicast address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: address_type
                
                	Specifies the address type
                	**type**\: :py:class:`IepAddress_Enum <ydk.models.ip.Cisco_IOS_XR_ip_iep_oper.IepAddress_Enum>`
                
                .. attribute:: hop_type
                
                	Specifies the next unicast address in the path as a strict or loose hop
                	**type**\: :py:class:`IepHop_Enum <ydk.models.ip.Cisco_IOS_XR_ip_iep_oper.IepHop_Enum>`
                
                .. attribute:: if_index
                
                	Interface Index of the path
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: index
                
                	Index number at which the path entry is inserted or modified
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-iep-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.address_type = None
                    self.hop_type = None
                    self.if_index = None
                    self.index = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-oper:address'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.address is not None:
                        return True

                    if self.address_type is not None:
                        return True

                    if self.hop_type is not None:
                        return True

                    if self.if_index is not None:
                        return True

                    if self.index is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_oper as meta
                    return meta._meta_table['ExplicitPaths.Identifiers.Identifier.Address']['meta_info']

            @property
            def _common_path(self):
                if self.identifier_id is None:
                    raise YPYDataValidationError('Key property identifier_id is None')

                return '/Cisco-IOS-XR-ip-iep-oper:explicit-paths/Cisco-IOS-XR-ip-iep-oper:identifiers/Cisco-IOS-XR-ip-iep-oper:identifier[Cisco-IOS-XR-ip-iep-oper:identifier-id = ' + str(self.identifier_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.identifier_id is not None:
                    return True

                if self.address is not None:
                    for child_ref in self.address:
                        if child_ref._has_data():
                            return True

                if self.status is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_oper as meta
                return meta._meta_table['ExplicitPaths.Identifiers.Identifier']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-iep-oper:explicit-paths/Cisco-IOS-XR-ip-iep-oper:identifiers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.identifier is not None:
                for child_ref in self.identifier:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_oper as meta
            return meta._meta_table['ExplicitPaths.Identifiers']['meta_info']


    class Names(object):
        """
        List of configured IP explicit path names
        
        .. attribute:: name
        
        	IP explicit path configured for a particular path name
        	**type**\: list of :py:class:`Name <ydk.models.ip.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Names.Name>`
        
        

        """

        _prefix = 'ip-iep-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.name = YList()
            self.name.parent = self
            self.name.name = 'name'


        class Name(object):
            """
            IP explicit path configured for a particular
            path name
            
            .. attribute:: path_name
            
            	Path name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: address
            
            	List of IP addresses configured in the explicit path
            	**type**\: list of :py:class:`Address <ydk.models.ip.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Names.Name.Address>`
            
            .. attribute:: status
            
            	Status of the path
            	**type**\: :py:class:`IepStatus_Enum <ydk.models.ip.Cisco_IOS_XR_ip_iep_oper.IepStatus_Enum>`
            
            

            """

            _prefix = 'ip-iep-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.path_name = None
                self.address = YList()
                self.address.parent = self
                self.address.name = 'address'
                self.status = None


            class Address(object):
                """
                List of IP addresses configured in the explicit
                path
                
                .. attribute:: address
                
                	IPv4 unicast address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: address_type
                
                	Specifies the address type
                	**type**\: :py:class:`IepAddress_Enum <ydk.models.ip.Cisco_IOS_XR_ip_iep_oper.IepAddress_Enum>`
                
                .. attribute:: hop_type
                
                	Specifies the next unicast address in the path as a strict or loose hop
                	**type**\: :py:class:`IepHop_Enum <ydk.models.ip.Cisco_IOS_XR_ip_iep_oper.IepHop_Enum>`
                
                .. attribute:: if_index
                
                	Interface Index of the path
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: index
                
                	Index number at which the path entry is inserted or modified
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-iep-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.address_type = None
                    self.hop_type = None
                    self.if_index = None
                    self.index = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-oper:address'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.address is not None:
                        return True

                    if self.address_type is not None:
                        return True

                    if self.hop_type is not None:
                        return True

                    if self.if_index is not None:
                        return True

                    if self.index is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_oper as meta
                    return meta._meta_table['ExplicitPaths.Names.Name.Address']['meta_info']

            @property
            def _common_path(self):
                if self.path_name is None:
                    raise YPYDataValidationError('Key property path_name is None')

                return '/Cisco-IOS-XR-ip-iep-oper:explicit-paths/Cisco-IOS-XR-ip-iep-oper:names/Cisco-IOS-XR-ip-iep-oper:name[Cisco-IOS-XR-ip-iep-oper:path-name = ' + str(self.path_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.path_name is not None:
                    return True

                if self.address is not None:
                    for child_ref in self.address:
                        if child_ref._has_data():
                            return True

                if self.status is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_oper as meta
                return meta._meta_table['ExplicitPaths.Names.Name']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-iep-oper:explicit-paths/Cisco-IOS-XR-ip-iep-oper:names'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.name is not None:
                for child_ref in self.name:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_oper as meta
            return meta._meta_table['ExplicitPaths.Names']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-iep-oper:explicit-paths'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.identifiers is not None and self.identifiers._has_data():
            return True

        if self.identifiers is not None and self.identifiers.is_presence():
            return True

        if self.names is not None and self.names._has_data():
            return True

        if self.names is not None and self.names.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_oper as meta
        return meta._meta_table['ExplicitPaths']['meta_info']

