SUBDIRS=PRU_RPMsg_Echo_Interrupt0 PRU_RPMsg_Echo_Interrupt1 \
	PRU_Halt PRU_MAC_Multiply_Accum \
	PRU_Direct_Connect0 PRU_Direct_Connect1

all: $(SUBDIRS)

$(SUBDIRS):
	@$(MAKE) -C $@

clean:
	@for d in $(SUBDIRS); do (cd $$d; $(MAKE) clean ); done

.PHONY: all clean $(SUBDIRS)
