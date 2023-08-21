SUBDIRS=MyFirst_PRU_Assembler_Program \
	MyFirst_PRU_C_Program \
	MyFirst_PRU_mixed_Program \
        PRU_FastGpio_PRG0 \
        PRU_FastGpio_PRG1 \
        Ultrafast_broadside

all: $(SUBDIRS)

$(SUBDIRS):
	@$(MAKE) -C $@

clean:
	@for d in $(SUBDIRS); do (cd $$d; $(MAKE) clean ); done

.PHONY: all clean $(SUBDIRS)
