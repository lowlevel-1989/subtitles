### install in linux
~~~
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
~~~

### Eliminar subtitulos en blanco
~~~
$ python working.srt.py \
    resource/the.magic.school.bus.1994.song.en.srt > the.magic.school.bus.1994.song.en.srt
~~~

### Agregar delay
~~~
$ python working.srt.py --delay 4.15 \
    example/the.magic.school.bus.1994.s1e7.en.srt > the.magic.school.bus.1994.s0e7.en.srt
~~~

### Unir varios subtitulos
~~~
$ python working.srt.py \
    resource/the.magic.school.bus.1994.song.en.srt \
    example/the.magic.school.bus.1994.s01e7.en.srt > the.magic.school.bus.1994.s01e7.en.srt
~~~

### Reemplazar lineas de subtitulos
~~~
$ python working.srt.py -r resource/blues.clues.intro.en.srt \
    ../blue\ is\ clues/s1/Blue\'s.Clues.S01E01.en.srt > blues.clues.s01e01.en.srt
~~~

### Utilizar ia para sync
~~~
$ autosubsync The.Magic.School.Bus.s01e07.mp4 \
    the.magic.school.bus.1994.s01e7.en.fix.srt the.magic.school.bus.1994.s01e7.en.srt
~~~
