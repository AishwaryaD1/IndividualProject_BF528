#!/usr/bin/env python
import re

rna= 'GGUCCGGGAUGCCUGAAUGGUACACUGGUAAGUACACUGUAAGUAAAAAAAA'
result = re.search('AUG.+', str(rna))

orf = result.group()
print(orf)

