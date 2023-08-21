################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Each subdirectory must supply rules for building sources it contributes
%.obj: ../%.c $(GEN_OPTS) | $(GEN_FILES) $(GEN_MISC_FILES)
	@echo 'Building file: "$<"'
	@echo 'Invoking: PRU Compiler'
	"/home/rik/ti/ccs1240/ccs/tools/compiler/ti-cgt-pru_2.3.3/bin/clpru" -v3 --include_path="/home/rik/ti/ccs1240/ccs/tools/compiler/ti-cgt-pru_2.3.3/include" --include_path="../../../../include" --include_path="../../../../include/am335x" -g --define=am3359 --define=pru0 --display_error_number --diag_warning=225 --diag_wrap=off --hardware_mac=on --endian=little --preproc_with_compile --preproc_dependency="$(basename $(<F)).d_raw" $(GEN_OPTS__FLAG) "$(shell echo $<)"
	@echo 'Finished building: "$<"'
	@echo ' '


