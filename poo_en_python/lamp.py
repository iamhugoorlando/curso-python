# -*- coding: utf-8 -*-

class Lamp:

    # variable de la clase Lamp
    _LAMPS = [ '''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on): # init es el constructor de nuestra clase
        self._is_turned_on = is_turned_on

    # metodos publicos que cambian el estado y despliegan la imagen
    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    # metodo privado que prende o apaga la imagen
    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


