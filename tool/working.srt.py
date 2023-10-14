import srt
import os
import sys
import argparse

from datetime import timedelta


srt_path = []
srt_subs = []

parser = argparse.ArgumentParser(description='Working SRT')
parser.add_argument('srt_path', nargs='+')
parser.add_argument('-d', '--delay', type=float)
parser.add_argument('-r', '--replace', action='store_true')
args = parser.parse_args()

delay      = args.delay
is_replace = args.replace

for i in range(len(args.srt_path)):
    srt_path.append(args.srt_path[i])
    # Solo asignamos espacio en el array
    srt_subs.append(None)

print('', file=sys.stderr)
for i in range(len(srt_path)):
    fn = srt_path[i]
    print(f'srt parh {i}: {fn}', file=sys.stderr)
print('', file=sys.stderr)

for i in range(len(srt_path)):
    with open(srt_path[i], 'r', encoding='utf-8') as f:
       srt_subs[i] = list(srt.parse(f))

text = []

if is_replace and len(srt_path) == 2:
    for i, sub in enumerate(srt_subs[1]):
        if len(srt_subs[0]) > i:
            sub = srt_subs[0][i]
        text.append(sub)
else:
    for subs in srt_subs:
        for _, sub in enumerate(subs):
            text.append(sub)

for i, sub in enumerate(text):
    sub.index = i+1
    if delay:
        sub.start += timedelta(seconds=delay)
        sub.end   += timedelta(seconds=delay)

content = srt.compose(text)
print(content)
