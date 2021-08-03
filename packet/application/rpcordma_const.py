#===============================================================================
# Copyright 2017 NetApp, Inc. All Rights Reserved,
# contribution by Jorge Mora <mora@netapp.com>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#===============================================================================
# Generated by process_xdr.py from packet/application/rpcordma.x on Tue Aug 03 11:30:52 2021
"""
RPCORDMA constants module
"""
import nfstest_config as c

# Module constants
__author__    = "Jorge Mora (%s)" % c.NFSTEST_AUTHOR_EMAIL
__copyright__ = "Copyright (C) 2017 NetApp, Inc."
__license__   = "GPL v2"
__version__   = "1.0"

# Enum rpc_rdma_errcode
ERR_VERS  = 1  # Value fixed for all versions
ERR_CHUNK = 2

rpc_rdma_errcode = {
    1 : "ERR_VERS",
    2 : "ERR_CHUNK",
}

# Enum rdma_proc
RDMA_MSG   = 0  # Value fixed for all versions
RDMA_NOMSG = 1  # Value fixed for all versions
RDMA_MSGP  = 2  # Not to be used
RDMA_DONE  = 3  # Not to be used
RDMA_ERROR = 4  # Value fixed for all versions

rdma_proc = {
    0 : "RDMA_MSG",
    1 : "RDMA_NOMSG",
    2 : "RDMA_MSGP",
    3 : "RDMA_DONE",
    4 : "RDMA_ERROR",
}
