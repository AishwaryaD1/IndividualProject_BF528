#!/usr/bin/env python
import re
rna = 'GGUCCGGGAUGCCUGAAUGGUACACUGGUAAGUACACUGUAAGUAAAAAAAA'
orf = re.search('AUG([AUGC]{3})+(UAA|UGA|UAG)', rna) .group()
print(orf)
