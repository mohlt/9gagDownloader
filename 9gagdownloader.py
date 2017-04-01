import re
import urllib
import os
def downGif(gifs):
    for x in gifs:
        print("downloading "+x)
        filename=open("./gifs/"+x+".mp4","wb")
        f=urllib.urlopen("https://img-9gag-fun.9cache.com/photo/"+x+"_460sv.mp4")
        filename.write(f.read())
        filename.close()
def downJpg(gifs):
    
    for x in gifs:
        print("downloading "+x)
        filename=open("./pics/"+x+".jpg","wb")
        f=urllib.urlopen("https://img-9gag-fun.9cache.com/photo/"+x+"_700b.jpg")
        filename.write(f.read())
        filename.close()
def seperate(res):
    gifs=[]
    jpegs=[]
    for x in res:
        if(x[-3:]=="gif"):
            gifs.append(x[-17:-10])
        else:
            jpegs.append(x[-16:-9])
    return [gifs,jpegs]
            
if not os.path.exists("./gifs"):
    os.makedirs("./gifs")
if not os.path.exists("./pics"):
    os.makedirs("./pics")
limit=input("Enter minimum number of posts: ")
count=0
gifs=[]
jpgs=[]
gagurl="https://9gag.com";
firstTime=True
while(count<limit):
    filename=open("txtml","wb")
    f=urllib.urlopen(gagurl)
    filename.write(f.read())
    filename.close()
    fil=open("txtml")
    sourceHtml=fil.read()
    content=re.compile("https:\/\/img-9gag-fun\.9cache\.com\/photo\/.{12,13}\.[(jpg|gif)]{3,3}")
    nextContent=re.compile("<a class=\"btn badge-load-more-post\" href=\"\/\?id=.{32,32}")

    nextCont=nextContent.findall(sourceHtml)
    nextContLink=nextCont[0][-32:]

    
    cont=content.findall(sourceHtml)
    [gifName,jpgName]=seperate(cont)
    gifName=list(set(gifName))
    jpgName=list(set(jpgName)-set(gifName))
    
    gifs = gifs + gifName
    jpgs = jpgs + jpgName
    gagurl= gagurl +"/?id="+nextContLink if firstTime else gagurl[0:-32] +nextContLink
    firstTime=False
    count=len(gifs)+len(jpgs)
    print("collected url for "+str(count)+" posts")

print("done collecting urls!!")
print("starting downloads")


downJpg(jpgs)
downGif(gifs)

