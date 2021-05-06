#!/usr/bin/env python

import re
rna = 'GGUCCGGGAUGCCUGAAUGGUACACUGGUAAGUACACUGUAAGUAAAAAAAA'
orf = re.search('AUG[AUGC]+(UAA|UAG|UGA)', rna). group()

print(orf)
