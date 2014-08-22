from xml.dom.minidom import parse

dom1 = parse("AndroidManifest.xml")
oldVersion = dom1.documentElement.getAttribute("android:versionCode")

oldVersion = str(int(oldVersion) + 1)
dom1.documentElement.setAttribute("android:versionCode", oldVersion)

with open("AndroidManifest.xml", 'wt') as f:
    f.write(dom1.toxml())
f.close()
print("set build version = " + oldVersion)
