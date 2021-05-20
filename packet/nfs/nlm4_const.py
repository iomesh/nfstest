#===============================================================================
# Copyright 2014 NetApp, Inc. All Rights Reserved,
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
# Generated by process_xdr.py from packet/nfs/nlm4.x on Thu May 20 14:00:23 2021
"""
NLMv4 constants module
"""
import nfstest_config as c

# Module constants
__author__    = "Jorge Mora (%s)" % c.NFSTEST_AUTHOR_EMAIL
__copyright__ = "Copyright (C) 2014 NetApp, Inc."
__license__   = "GPL v2"
__version__   = "4.0"

# Enum nfs_bool
FALSE = 0
TRUE  = 1

nfs_bool = {
    0 : "FALSE",
    1 : "TRUE",
}

# Sizes
LM_MAXSTRLEN = 1024
MAXNAMELEN   = 1025  # LM_MAXSTRLEN + 1
MAXNETOBJ_SZ = 1024

# Enum nlm4_stats
NLM4_GRANTED             = 0
NLM4_DENIED              = 1
NLM4_DENIED_NOLOCKS      = 2
NLM4_BLOCKED             = 3
NLM4_DENIED_GRACE_PERIOD = 4
NLM4_DEADLCK             = 5
NLM4_ROFS                = 6
NLM4_STALE_FH            = 7
NLM4_FBIG                = 8
NLM4_FAILED              = 9

nlm4_stats = {
    0 : "NLM4_GRANTED",
    1 : "NLM4_DENIED",
    2 : "NLM4_DENIED_NOLOCKS",
    3 : "NLM4_BLOCKED",
    4 : "NLM4_DENIED_GRACE_PERIOD",
    5 : "NLM4_DEADLCK",
    6 : "NLM4_ROFS",
    7 : "NLM4_STALE_FH",
    8 : "NLM4_FBIG",
    9 : "NLM4_FAILED",
}

# Enum fsh4_mode
fsm_DN  = 0
fsm_DR  = 1
fsm_DW  = 2
fsm_DRW = 3

fsh4_mode = {
    0 : "fsm_DN",
    1 : "fsm_DR",
    2 : "fsm_DW",
    3 : "fsm_DRW",
}

# Enum fsh4_access
fsa_NONE = 0
fsa_R    = 1
fsa_W    = 2
fsa_RW   = 3

fsh4_access = {
    0 : "fsa_NONE",
    1 : "fsa_R",
    2 : "fsa_W",
    3 : "fsa_RW",
}

# Enum nlm_proc4
NLMPROC4_NULL        = 0
NLMPROC4_TEST        = 1
NLMPROC4_LOCK        = 2
NLMPROC4_CANCEL      = 3
NLMPROC4_UNLOCK      = 4
NLMPROC4_GRANTED     = 5
NLMPROC4_TEST_MSG    = 6
NLMPROC4_LOCK_MSG    = 7
NLMPROC4_CANCEL_MSG  = 8
NLMPROC4_UNLOCK_MSG  = 9
NLMPROC4_GRANTED_MSG = 10
NLMPROC4_TEST_RES    = 11
NLMPROC4_LOCK_RES    = 12
NLMPROC4_CANCEL_RES  = 13
NLMPROC4_UNLOCK_RES  = 14
NLMPROC4_GRANTED_RES = 15
NLMPROC4_SHARE       = 20
NLMPROC4_UNSHARE     = 21
NLMPROC4_NM_LOCK     = 22
NLMPROC4_FREE_ALL    = 23

nlm_proc4 = {
     0 : "NLMPROC4_NULL",
     1 : "NLMPROC4_TEST",
     2 : "NLMPROC4_LOCK",
     3 : "NLMPROC4_CANCEL",
     4 : "NLMPROC4_UNLOCK",
     5 : "NLMPROC4_GRANTED",
     6 : "NLMPROC4_TEST_MSG",
     7 : "NLMPROC4_LOCK_MSG",
     8 : "NLMPROC4_CANCEL_MSG",
     9 : "NLMPROC4_UNLOCK_MSG",
    10 : "NLMPROC4_GRANTED_MSG",
    11 : "NLMPROC4_TEST_RES",
    12 : "NLMPROC4_LOCK_RES",
    13 : "NLMPROC4_CANCEL_RES",
    14 : "NLMPROC4_UNLOCK_RES",
    15 : "NLMPROC4_GRANTED_RES",
    20 : "NLMPROC4_SHARE",
    21 : "NLMPROC4_UNSHARE",
    22 : "NLMPROC4_NM_LOCK",
    23 : "NLMPROC4_FREE_ALL",
}
