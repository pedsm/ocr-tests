try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re


full_text = pytesseract.image_to_string(Image.open('./mag_scan.png'))

lines = full_text.split('\n')

def fetch_chunk(line, chunk_size):
    # print("starting on line " + str(line))
    chunk = ""
    for i in range(chunk_size):
        if len(lines) > line+i:
            chunk += lines[line+i] + "\n"
        else:
            break
    return chunk

def process_chunk(chunk):
    dict = {}
    chunk_lines = chunk.split('\n')
    dict['title'] = chunk_lines[0]

    for line in chunk_lines:
        if re.search(r'[a-zA-Z]*:\ ', line):
            key, value = line.split(':')
            dict[key] = value
    return dict

for (i, line) in enumerate(lines):
    if not re.search('[a-zA-Z]', line):
        continue
    if line.upper() == line and not re.search('[0-9]', line):
        print(process_chunk(fetch_chunk(i, 20)))

