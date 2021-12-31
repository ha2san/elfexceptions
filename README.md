I tried:
    ltrace ./path
    objdump -d ./path
    readelf -r ./path 


__cxa_begin_catch@plt
__cxa_allocate_exception@plt in objdump
__cxa_end_catch@plt

output of readelf -r 
    binary with exception :
        Relocation section '.rela.plt' at offset 0x9a8 contains 10 entries:
          Offset          Info           Type           Sym. Value    Sym. Name + Addend
        000000004018  000100000007 R_X86_64_JUMP_SLO 0000000000000000 __cxa_begin_catch@CXXABI_1.3 + 0
        000000004020  000300000007 R_X86_64_JUMP_SLO 0000000000000000 __cxa_allocate_ex[...]@CXXABI_1.3 + 0
        000000004028  000400000007 R_X86_64_JUMP_SLO 0000000000000000 __cxa_atexit@GLIBC_2.2.5 + 0
        000000004030  000500000007 R_X86_64_JUMP_SLO 0000000000000000 _ZStlsISt11char_t[...]@GLIBCXX_3.4 + 0
        000000004038  000600000007 R_X86_64_JUMP_SLO 0000000000000000 _ZStlsISt11char_t[...]@GLIBCXX_3.4 + 0
        000000004040  000700000007 R_X86_64_JUMP_SLO 0000000000000000 _ZNSt8ios_base4In[...]@GLIBCXX_3.4 + 0
        000000004048  000800000007 R_X86_64_JUMP_SLO 0000000000000000 __cxa_end_catch@CXXABI_1.3 + 0
        000000004050  000a00000007 R_X86_64_JUMP_SLO 0000000000000000 __cxa_throw@CXXABI_1.3 + 0
        000000004058  000b00000007 R_X86_64_JUMP_SLO 0000000000000000 _ZNSolsEi@GLIBCXX_3.4 + 0
        000000004060  000d00000007 R_X86_64_JUMP_SLO 0000000000000000 _Unwind_Resume@GCC_3.0 + 0
    
    binary with no exception
        Relocation section '.rela.plt' at offset 0x7d0 contains 4 entries:
          Offset          Info           Type           Sym. Value    Sym. Name + Addend
        000000004018  000200000007 R_X86_64_JUMP_SLO 0000000000000000 __cxa_atexit@GLIBC_2.2.5 + 0
        000000004020  000300000007 R_X86_64_JUMP_SLO 0000000000000000 _ZStlsISt11char_t[...]@GLIBCXX_3.4 + 0
        000000004028  000400000007 R_X86_64_JUMP_SLO 0000000000000000 _ZStlsISt11char_t[...]@GLIBCXX_3.4 + 0
        000000004030  000500000007 R_X86_64_JUMP_SLO 0000000000000000 _ZNSt8ios_base4In[...]@GLIBCXX_3.4 + 0




