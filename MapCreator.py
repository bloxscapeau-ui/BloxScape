from PIL import Image
import json
import numpy as np

# 1. Load the map image
img = Image.open('map_layout.png').convert('RGB')
pixels = np.array(img)

# 2. Define your tile mapping (RGB: TileID)
TILE_MAPPING = {
    (0,0,0): 1, # Black -> Actual Tile
    (255,0,0): 2 # RED -> Enemy Test File
    #(0, 255, 0): 1,   # Green -> Grass
    #(0, 0, 255): 2,   # Blue  -> Water
    #(128, 128, 128): 3 # Grey  -> Stone
}

# 3. Generate the tile array
height, width, _ = pixels.shape
tile_map = []

#Each pixel will have its own array showing the Tile Type, the X Co-ordinate and than the Z Co-ordinate
#End result should show each row something like this [[0,0,0][0,0,5][0,0,10][0,0,3][0,0,4][0,0,5][0,0,6][0,0,7][0,0,8][0,0,9]]
#                                                    [[0,-5,0][0,-1,1][0,-1,2][0,-1,3][0,-1,4][0,-1,5][0,-1,6][0,-1,7][0,-1,8][0,-1,9]]
xAxis = 0
for y in range(height):
    row = []
    zAxis = 0
    for x in range(width):
        color = tuple(pixels[y, x])
        # Get the ID from mapping, default to 0 (empty/unknown)
        tile_id = TILE_MAPPING.get(color, 0)
        if tile_id == 0: print("No ID was given, may want to check map_layout incase this wasn't on purpose.")
        row.append([tile_id, xAxis, zAxis])
        zAxis += 5
    tile_map.append(row)
    xAxis -= 5
# Now 'tile_map' is a 2D array of IDs ready for your script
print(tile_map)

with open("data.json", "w") as file:
    json.dump(tile_map, file)