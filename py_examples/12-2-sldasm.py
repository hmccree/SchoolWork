import os
from os import path
# from pathlib import Path
# from shutil import copyfile

parts = os.listdir()
print(parts)

# for file in files:
#     if file.endswith('.prt.1'):
#         os.rename(file.with_suffix('.sldprt'))
#     elif file.endswith('.asm.1'):
#         file.rename(file.with_suffix('.sldasm'))


# thisFile = './12-2-sldasmParts/part1.prt.1'
# base = os.path.splitext(thisFile)[0]
# os.rename(thisFile, base + '.sldprt')

# for part in parts:
#     if '.prt.1' in part:
#         newpart = part.replace('.prt.1', '.sldprt')
#         os.rename(part, newpart)

# for part in parts:
#   os.rename(%s.prt.1, %s.sldprt % part)

for part in parts:
    parts = os.listdir()

    if '.prt.1' in part:
        ext = '.sldprt'
        # filename = part
        partnoext = part.rsplit('.', 2)[0]
        print(partnoext)
        os.rename(part, partnoext + ext)#, (os.path.join('12-2-sldasmParts', parts))
        #parts = os.listdir('12-2-sldasmParts')
        print(part)

    elif '.asm.1' in part:
        ext = '.sldasm'
        # filename = part
        partnoext = part.rsplit('.', 2)[0]
        print(partnoext)
        os.rename(part, partnoext + ext)#, (os.path.join('12-2-sldasmParts', parts))
        #parts = os.listdir('12-2-sldasmParts')
        print(part)

print(parts)