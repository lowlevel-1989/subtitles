### install in linux
~~~
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
~~~

### Eliminar subtitulos en blanco
~~~
$ python working.srt.py \
    example/the.magic.school.bus.1994.song.en.srt > the.magic.school.bus.1994.song.en.srt
~~~

### Unir varios subtitulos
~~~
$ python working.srt.py \
    example/the.magic.school.bus.1994.song.en.srt \
    example/the.magic.school.bus.1994.s01e7.en.srt > the.magic.school.bus.1994.s01e7.en.srt
~~~
