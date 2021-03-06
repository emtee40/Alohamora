#The path of the fuzz_zone binary used to send SCMs
FUZZ_ZONE_PATH = "/data/local/tmp/fuzz_zone"

#The number of currently supported arguments in register SCM commands via fuzz_zone
REGISTER_SCM_SUPPORTED_ARGS = 3

#The remote path of the binary dump file which is temporarily used to read from memory
REMOTE_TEMP_DUMP_PATH = "/data/local/tmp/dump.bin"

#The local path of the binary dump file which is temporarily used to read from memory
LOCAL_TEMP_DUMP_PATH = "dump.bin"

#The path of the shellcode written to the code cave
SHELLCODE_PATH = "shellcode.bin"

#Whether or not the written shellcode is THUMB code (or ARM)
IS_SHELLCODE_THUMB = 0

#Snipped from scm.h
SCM_SVC_ES = 0x10
SCM_IS_ACTIVATED_ID = 0x2
SCM_SVC_UTIL = 0x3
TZ_UTIL_SEC_ALLOWS_MEMDUMP = 0xB
SCM_SVC_INFO = 0x6
TZ_INFO_GET_FEATURE_VERSION_ID = 0x3
TZ_INFO_GET_DIAG = 0x2
QFPROM_SVC_ID = 0x8
QFPROM_WRITE_CMD = 0x3


#The clock speed for QFPROM operations
QFPROM_CLOCK = 0x40*1000

#Undocumented
SCM_SVC_PRNG = 0xA
SCM_PRNG_GETDATA = 1

#The maximal length of the generated random value
MAX_RANDOM_LEN = 0x200

#A physical address that will be treated as scrap space
JUNK_PHYSICAL_ADDRESS = 0xA000

