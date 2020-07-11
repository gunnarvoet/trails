from pathlib import Path

all_images = sorted(list(Path.cwd().glob('*.jpg')))

for i, file in enumerate(all_images):
    file.rename('img{:03d}.jpg'.format(i))

