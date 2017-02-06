

all:mcu_wc mcu_wl

mcu_wc: mcu_wc.o mcu_readl.o
	gcc -o mcu_wc mcu_readl.o mcu_wc.o

mcu_wl: mcu_wl.o mcu_readl.o
	gcc -o mcu_wl mcu_readl.o mcu_wl.o

mcu_wc.o: mcu_wc.c
	gcc -c mcu_wc.c

mcu_wl.o: mcu_wl.c
	gcc -c mcu_wl.c

mcu_readl.o: mcu_readl.c
	gcc -c mcu_readl.c

clean:
	-rm -f *.o *~ mcu_wc mcu_wl
