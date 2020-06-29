from os import listdir
from os.path import join
from PIL import Image

i = 1
for filename in listdir('./amanita_muscaria'):
  path = join('./amanita_muscaria', filename)
  try:
    im = Image.open(path)
  except:
    continue
  ar = round(im.width / im.height, 2)
  if ar < 1.3 or ar > 1.5:
    continue
  output = im.resize((840, 600))
  output.save(join('./amanita_muscaria_resized', filename))
  print(f'Saved {i}')
  i += 1
