from src import cmdControl
from src.maestro import Maestro
from src.playlist import Playlist

playlist = Playlist()
maestro = Maestro(playlist)

maestro.start()

cmdControl(playlist, maestro)

maestro.join()
