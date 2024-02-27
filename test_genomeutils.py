import genomeutils

print(genomeutils.reverse_complement("AAAACGT"))
print(genomeutils.transcribe('ACGT'))
print(genomeutils.translate('ATGTAA'))

s = 'ACGTGGGGGGCATATG'
print(genomeutils.gc_comp(s))

gc = genomeutils.gc_comp(s)
gc_rev = genomeutils.gc_comp(genomeutils.reverse_complement(s))
print(gc, gc_rev)