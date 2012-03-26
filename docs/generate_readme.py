import os

content = ''
for filename in ['introduction.rst', 'installation.rst', 'usage.rst']:
    instream = open(filename)
    content += instream.read()
    if not content.endswith("\n\n"):
        if content.endswith("\n"):
            content += '\n'
        else:
            content += '\n\n'
    instream.close()
    

outfilename = 'README_test.rst'
outfilenamepath = os.path.join("../", outfilename)
print outfilenamepath

outstream = open(outfilenamepath, "wb")
outstream.write(content)
outstream.close()


    