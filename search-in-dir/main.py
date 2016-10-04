import os

offset = 1024
patternLength = 16
res = []

def walk(dir):
  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    if os.access(path, os.R_OK):
      if os.path.isfile(path):
        file = open(path, 'r')
        file.seek(offset)
        chunk = file.read(patternLength)
        if chunk == needToFindPattern:
          res.append(path)
      else:
        walk(path)
pathToFile = raw_input('Enter an absolute path to file: ')

if os.path.isfile(pathToFile):
  fileP = open(pathToFile, 'r')
  fileP.seek(offset)
  needToFindPattern = fileP.read(patternLength)
else:
  print('Invalid path to file, the program has stopped. Please, try again.')
  exit()

pathDir = raw_input('Enter an absolute path to directory: ')

if os.path.isdir(pathDir):
  walk(pathDir)
  print('Found this pattern in following files:')
  print('\n'.join(res))
else:
  print('Invalid path to directory, program has stopeed. Please, try again.')
  exit()
