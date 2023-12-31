# PRU_CGT environment variable must point to the TI PRU code gen tools directory.
# The latest PRU CGT can be found at https://www.ti.com/tool/PRU-CGT or in Code
# Composer Studio (CCS) App Center.

ifndef PRU_CGT
define ERROR_BODY

*******************************************************************************
PRU_CGT environment variable is not set. For example:
(Desktop Linux) export PRU_CGT=/path/to/pru/code/gen/tools/ti-cgt-pru_2.3.3
(Windows) set PRU_CGT=C:/path/to/pru/code/gen/tools/ti-cgt-pru_2.3.3
(ARM Linux*) export PRU_CGT=/usr/share/ti/cgt-pru

*ARM Linux also needs to create a symbolic link to the /usr/bin/ directory in
order to use the same Makefile
(ARM Linux) ln -s /usr/bin/ /usr/share/ti/cgt-pru/bin

The latest PRU CGT can be found at https://www.ti.com/tool/PRU-CGT or in Code
Composer Studio (CCS) App Center.
*******************************************************************************

endef
$(error $(ERROR_BODY))
endif

SLICE ?= 0
MKFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
CURRENT_DIR := $(notdir $(patsubst %/,%,$(dir $(MKFILE_PATH))))
PROJ_NAME=$(CURRENT_DIR)
LINKER_COMMAND_FILE ?= ./AM64x_PRU.cmd
LIBS= #No libraries in this project. See RPMsg_Echo_Interrupt for example usage
INCLUDE=--include_path=../../../include --include_path=../../../include/am64x
STACK_SIZE=0x100
HEAP_SIZE=0x100
GEN_DIR=gen/PRU$(SLICE)

#Common compiler and linker flags (Defined in 'PRU Optimizing C/C++ Compiler User's Guide)
CFLAGS=-v4 -Ooff --display_error_number --endian=little --hardware_mac=on --asm_directory=$(GEN_DIR) --obj_directory=$(GEN_DIR) --pp_directory=$(GEN_DIR) -ppd -ppa
#Linker flags (Defined in 'PRU Optimizing C/C++ Compiler User's Guide)
LFLAGS=--reread_libs --warn_sections --stack_size=$(STACK_SIZE) --heap_size=$(HEAP_SIZE)

#DCFLAGS pass instance specific defines to the program (see --define in 'PRU Optimizing C/C++ Compiler User's Guide')
DCFLAGS= #No DCFLAGS in this project. See RPMsg_Echo_Interrupt for example usage

TARGET=$(GEN_DIR)/$(PROJ_NAME)_$(SLICE).out
MAP=$(GEN_DIR)/$(PROJ_NAME)_$(SLICE).map
OBJECTS=$(patsubst %.asm,$(GEN_DIR)/%.object,$(wildcard *.asm))
OBJECTS+=$(patsubst %.c,$(GEN_DIR)/%.object,$(wildcard *.c))

all: .printStart .build_all .printEnd

.build_all:
	@make --no-print-directory .build_one SLICE=0 LINKER_COMMAND_FILE=./AM64x_PRU.cmd
	@echo ''
#	@make --no-print-directory .build_one SLICE=1 LINKER_COMMAND_FILE=./AM64x_PRU1.cmd
#	@echo ''

.printStart:
	@echo ''
	@echo '************************************************************'
	@echo 'Building project: $(PROJ_NAME)'
	@echo ''

.printEnd:
	@echo ''
	@echo 'Finished building project: $(PROJ_NAME)'
	@echo '************************************************************'
	@echo ''

.build_one: $(TARGET)

# Invokes the linker (-z flag) to make the .out file
$(TARGET): $(OBJECTS) $(LINKER_COMMAND_FILE)
	@echo ''
	@echo 'Building target: $@'
	@echo 'Invoking: PRU Linker'
	$(PRU_CGT)/bin/clpru $(CFLAGS) -z -i$(PRU_CGT)/lib -i$(PRU_CGT)/include $(LFLAGS) -o $(TARGET) $(OBJECTS) -m$(MAP) $(LINKER_COMMAND_FILE) --library=libc.a $(LIBS)

	@echo 'Finished building target: $@'
# Invokes the compiler on all assembly files in the directory to create the object files
$(GEN_DIR)/%.object: %.asm
	@mkdir -p $(GEN_DIR)
	@echo ''
	@echo 'Building file: $<'
	@echo 'Invoking: PRU Compiler'
	$(PRU_CGT)/bin/clpru --include_path=$(PRU_CGT)/include $(INCLUDE) $(CFLAGS) -fe $@ $<

# Invokes the compiler on all c files in the directory to create the object files
$(GEN_DIR)/%.object: %.c
	@mkdir -p $(GEN_DIR)
	@echo '###### Building for PRU$(SLICE) ######'
	@echo 'Building file: $<'
	@echo 'Invoking: PRU Compiler'
	$(PRU_CGT)/bin/clpru --include_path=$(PRU_CGT)/include $(INCLUDE) $(CFLAGS) $(DCFLAGS) -fe $@ $<

.PHONY: all clean

# Remove the $(GEN_DIR) directory
clean:
	@echo ''
	@echo '************************************************************'
	@echo 'Cleaning project: $(PROJ_NAME)'
	@echo ''
	@make --no-print-directory .clean_one SLICE=0
	@echo ''
	@make --no-print-directory .clean_one SLICE=1
	@echo ''
	@echo 'Removing the generated "gen" directory'
	@rm -rf gen
	@echo ''
	@echo 'Finished cleaning project: $(PROJ_NAME)'
	@echo '************************************************************'
	@echo ''

.clean_one:
	@echo 'Removing files in the "$(GEN_DIR)" directory'
	@rm -rf $(GEN_DIR)

# Includes the dependencies that the compiler creates (-ppd and -ppa flags)
-include $(OBJECTS:%.object=%.pp)