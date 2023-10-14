import srt
import os
import sys

srt_path = []
srt_subs = []

for i in range(len(sys.argv)-1):
    srt_path.append(sys.argv[i+1])
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
for subs in srt_subs:
    for _, sub in enumerate(subs):
        text.append(sub)

for i, sub in enumerate(text):
    sub.index = i+1

content = srt.compose(text)
print(content)
