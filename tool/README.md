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

### Parchear lineas de subtitulos
~~~
$ python working.srt.py --patch resource/blues.clues.intro.en.srt \
    ../blue\ is\ clues/s1/Blue\'s.Clues.S01E01.en.srt > blues.clues.s01e01.en.srt
~~~

### Utilizar ia para sync
~~~
$ autosubsync The.Magic.School.Bus.s01e07.mp4 \
    the.magic.school.bus.1994.s01e7.en.fix.srt the.magic.school.bus.1994.s01e7.en.srt
~~~

### Eliminar CC
~~~
$ find . -type f -name "*.srt" -exec sed -i ':a;N;$!ba;s/([^)]*)//g' {} \;
$ find . -type f -name "*.srt" -exec sed -i ':a;N;$!ba;s/\[[^]]*\]//g' {} \;
~~~

### export srt
~~~
$ ffmpeg -i Heartstopper.S01E01.1080p.WEB.H264-PECULATE.mkv -map 0:s:5 'heartstopper.2022.s01e02.en.srt'
~~~
