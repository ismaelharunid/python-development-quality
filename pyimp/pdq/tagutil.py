
import re
from functools import reduce


regex0 = re.compile(r'[^\w -]+', re.M)
regex1 = re.compile(r'[\s_-]+', re.M)

unique = lambda tags, src=(): \
    type(src)(reduce((lambda a,c: a if c in a else a+(c,)) \
    , tags, tuple(src)))

tag_clean = lambda tag: \
    regex1.sub('-', regex0.sub('', tag.strip('- \n').lower()))

tags_split = lambda tags, more=(): unique(tuple(tag_clean(tag) for tag in \
    (tag.strip() for tag in tags.split(' ')) if tag) + more)

tags_join = lambda tags: ' '.join(unique(tags))
