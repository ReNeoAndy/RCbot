import os
folder  = '/home/evansziandy/Documentos'
test = os.listdir(folder)

for images in test:
    if images.endswith(".png"):
        os.remove(os.path.join(folder, images))