
import re
from functools import reduce


regex0 = re.compile(r'[^\w -]+', re.M)
regex1 = re.compile(r'[\s_-]+', re.M)

clean = lambda tag: \
    regex1.sub('-', regex0.sub('', tag.strip('- \n').lower()))

unique = lambda tags, src=(): \
    type(src)(reduce((lambda a,c: a if c in a else a+(c,)) \
    , tags, tuple(src)))

split = lambda tags, more=(): unique(tuple(clean(tag) for tag in \
    (tag.strip() for tag in tags.split(' ')) if tag) + more)

join = lambda tags: ' '.join(unique(tags))
