#https://www.adamsmith.haus/python/examples/5649/zipfile-write-a-string-to-a-zip-archive
import zipfile
zf = zipfile.ZipFile("sample.zip", mode="w", compression=zipfile.ZIP_DEFLATED)
zf.writestr("sample.txt", "Hello there!")
zf.close()
zf = zipfile.ZipFile("sample.zip")
print(zf.read("sample.txt"))