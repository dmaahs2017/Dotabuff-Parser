from cx_Freeze import setup, Executable

setup(name = 'Quick Stats Dota',
      version = '0.7',
      description = 'Scrape the dotabuff overview page for some quick stats about a dota 2 player. Must know the url of the overview page though.',
      executables = [Executable('Quick Stats Dota.py')]
      )
