# reading images using normal read mode: cannot decode byte 0x8f means text is generally unicode and unicode doesnot support byte value and throws a UnicodeDecodeError


with open('File handling\Binary files\Shivom.png', 'r') as f:
    f.read()


#  reading binary files
with open('File handling\Binary files\Shivom.png', 'rb') as f:
    with open('shivom_copy.png','wb') as wb:
        wb.write(f.read())
