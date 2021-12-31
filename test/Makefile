CC=g++
TARGETS=exception no_exception 
SUBDIR1= ccpp-vtable-except
SUBDIR2= ccpp-vtable 

all:: exception no_exception learn
	mv exception bin/
	mv no_exception bin/
	./test

.PHONY: clean

learn:
	$(MAKE) -C $(SUBDIR1) 
	$(MAKE) -C $(SUBDIR2) 

exception: exception.o
no_exception: no_exception.o

exception.o: exception.cpp
no_exception.o: no_exception.cpp

clean_subdirs:
	$(MAKE) -C $(SUBDIR1) clean
	$(MAKE) -C $(SUBDIR2) clean

clean: clean_subdirs
	rm -rf *.o $(TARGETS)
	rm -rf bin/*


