from PIL import Image
import sys

im_in = sys.argv[1]
message = sys.argv[2]
outfile = sys.argv[3]

if len(sys.argv) != 4:
    print "Usage: image.png message.png outfile.png"
    sys.exit()

c_image = Image.open(im_in)
hide = Image.open(message)
hide = hide.resize(c_image.size)
hide = hide.convert('1')
out = Image.new('RGB', c_image.size)

width, height = c_image.size
new_array = []
print 'Encrypted started... Be patient, it depends on the image size.'

for h in range(height):
    for w in range(width):
        ip = c_image.getpixel((w, h))
        hp = hide.getpixel((w, h))
        if hp == 0:
            newred = ip[0] & 254
        else:
            newred = ip[0] | 1

        new_array.append((newred, ip[1], ip[2]))

out.putdata(new_array)
out.save(outfile)
print "Stealth image is saved to %s" % outfile
