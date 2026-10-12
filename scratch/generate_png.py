import zlib
import struct

def create_png_logo(filename):
    # Width: 280, Height: 90
    width = 280
    height = 90
    
    # We will draw a PNG with dark navy/transparent background and white AS9100D logo
    # Dark navy background color: #02245B (RGB: 2, 36, 91)
    # White logo color: #FFFFFF (RGB: 255, 255, 255)
    
    # Simple raster canvas RGBA
    img = bytearray([0] * (width * height * 4))
    
    def set_pixel(x, y, r, g, b, a=255):
        if 0 <= x < width and 0 <= y < height:
            idx = (y * width + x) * 4
            img[idx] = r
            img[idx+1] = g
            img[idx+2] = b
            img[idx+3] = a

    # Fill transparent background
    for y in range(height):
        for x in range(width):
            set_pixel(x, y, 0, 0, 0, 0)
            
    # Draw Jet & A (left side)
    # Airplane nose, wings, tail & fuselage
    for y in range(height):
        for x in range(width):
            # Contrail line y from 43 to 46, x from 35 to 270
            if 43 <= y <= 46 and 35 <= x <= 270:
                set_pixel(x, y, 255, 255, 255, 255)
                
            # Jet Nose & fuselage (slope)
            # Line 1: y = -1.5*x + 85
            # Left leg of A: x from 10 to 65
            if 10 <= x <= 65:
                # Main slanting stroke of A
                dx = x - 10
                expected_y = int(55 - dx * 0.8)
                if expected_y - 6 <= y <= expected_y + 6:
                    set_pixel(x, y, 255, 255, 255, 255)

            # Right leg of A
            if 45 <= x <= 75:
                dx = x - 45
                expected_y = int(10 + dx * 1.3)
                if expected_y - 4 <= y <= expected_y + 4 and y <= 46:
                    set_pixel(x, y, 255, 255, 255, 255)

            # Left wing of jet
            if 15 <= x <= 45 and 45 <= y <= 75:
                if (x - 15) * 1.0 + 45 <= y <= (x - 15) * 0.4 + 55:
                    set_pixel(x, y, 255, 255, 255, 255)

            # Right wing of jet
            if 35 <= x <= 75 and 15 <= y <= 42:
                if (x - 35) * -0.6 + 40 <= y <= (x - 35) * -0.2 + 42:
                    set_pixel(x, y, 255, 255, 255, 255)

    # Encode to PNG format
    raw_data = bytearray()
    for y in range(height):
        raw_data.append(0) # Filter type 0
        raw_data.extend(img[y * width * 4 : (y + 1) * width * 4])

    compressed_data = zlib.compress(raw_data)
    
    def chunk(chunk_type, data):
        return struct.pack('>I', len(data)) + chunk_type + data + struct.pack('>I', zlib.crc32(chunk_type + data))

    png_header = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0))
    idat = chunk(b'IDAT', compressed_data)
    iend = chunk(b'IEND', b'')
    
    with open(filename, 'wb') as f:
        f.write(png_header + ihdr + idat + iend)

create_png_logo(r'c:\Users\ADMIN\Desktop\part-time\img\as9100d-logo.png')
print('PNG created successfully.')
