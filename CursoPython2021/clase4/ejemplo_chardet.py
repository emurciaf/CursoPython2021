import cchardet as chardet


with open(r'clase4/ejemplo_fnmatch.py', 'rb') as f:
    msg = f.read()
    result = chardet.detect(msg)
    print(result)
