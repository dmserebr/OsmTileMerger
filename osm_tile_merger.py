import matplotlib.pyplot as plt
import numpy as np
import requests

url_template = "https://a.tile.openstreetmap.org/{0}/{1}/{2}.png"
tmp_file = "tmp.png"
result_file = "result.png"
tile_size = 256

# change these values as needed
zoom = 13
x_start = 4944
x_end = 4960
y_start = 2551
y_end = 2572


def get_image_bytes(x, y):
    url = url_template.format(zoom, x, y)
    print('Downloading tile from url {0}'.format(url))

    req = requests.get(url)

    with open(tmp_file, 'wb') as f:
        f.write(req.content)

    image_bytes = plt.imread(tmp_file)
    return np.transpose(image_bytes, (1, 0, 2))


x_size = (x_end - x_start + 1) * tile_size
y_size = (y_end - y_start + 1) * tile_size

result = np.zeros((x_size, y_size, 3))

for i in range(x_end - x_start + 1):
    for j in range(y_end - y_start + 1):
        tile_x = i + x_start
        tile_y = j + y_start

        bytes = get_image_bytes(tile_x, tile_y)

        result[tile_size*i:tile_size*(i+1), tile_size*j:tile_size*(j+1)] = bytes


result = np.transpose(result, (1, 0, 2))
print('Success! Saving the result: {0}'.format(result_file))

plt.imsave(result_file, result)
