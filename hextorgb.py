def hex_tio_rgb(hex):
    return tuple(int(hex[i:i+2],16)for i in (0,2,4))

g=hex_tio_rgb('FFA501')
print(g)