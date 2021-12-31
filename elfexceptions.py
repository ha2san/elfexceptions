#!/usr/bin/env python3

import sys
from elftools.elf.elffile import ELFFile
from elftools.elf.relocation import RelocationSection


def process_file(fname):
    with open(fname, 'rb') as f:
        e = ELFFile(f)
        section = e.get_section_by_name(".rela.plt")
        #for section in e.iter_sections():
        if not isinstance(section, RelocationSection):
            return False 
        symbol_table = e.get_section(section['sh_link'])
        for relocation in section.iter_relocations():
            symbol = symbol_table.get_symbol(relocation['r_info_sym'])
            if(symbol.name == "__cxa_allocate_exception"):
                #print("youpi found:",symbol.name)
                return True


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if process_file(sys.argv[1]):
            print("uses exception")
        else:
            print("does not use exception")
