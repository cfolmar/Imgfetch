##-----------------IMG-Fetch-----------------
##                   0.02
##
## A simple script that downloads all the
## images posted on some 4chan board, page
## by page. One can choose the # of pages to
## be parsed, or enter 'a' for all the pages
## -----------------------------------------
##                 2/5/2013
##                 3/3/2014
##             Christopher Folmar
##-------------------------------------------
## You, as the user, are free to modify and
## redistribute this code as long as credit
## to the original author is maintained.
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import urllib
import os
import sys
import datetime
import getopt

PATH_U = os.getenv("HOME") + "/Pictures/"
SITE = ""
COUNT = 0
VERB = 0

def main():
    global VERB
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hs:b:n:tv",[])
    except:
        getopt.GetoptError
        print "unregconized command/incorrect format, refer to the help below"
        f =  open('help',"r")
        print f.read()
        f.close()
        sys.exit(2)
    for opt, arg in opts:
        sort = ''
        if opt == '-h':
            f = open('help',"r")
            print f.read()
            f.close()
            sys.exit()
        elif opt == '-s':
            site = arg
        elif opt == '-b':
            board = arg
        elif opt == '-n':
            npage = int(arg)
        elif opt == '-t':
            sort = 't'
        elif opt == '-v':
            VERB = 1

    imget(site,board,npage,sort)


def imget(site,board,npage,sort):
    global SITE
    if site == '7':
        SITE = "https://7chan.org/"
    elif site == '4':
        SITE = "https://boards.4chan.org/"
    if VERB: print SITE
    if npage == "a":
        recur(board,11,sort,site)
    else:
        recur(board,npage+1,sort,site)




def recur(board,n,sort,site):
    threads = []
    npg = []
    now = datetime.datetime.now()
    for i in range(n):
        print "loading pages...."
        npg.append(pgld(SITE + board + "/" + str(i)))
        threads.append(parsethrd(npg[i],site))
        if VERB: print threads
    print "Fetching images...."

    for j in range(len(threads)):
        for x in range(len(threads[j])):
            imgg(SITE + board + "/res/" + threads[j][x], board,sort,threads[j][x])
    print "Fetched {0} images, put in {1}{2}/{3}".format(COUNT,PATH_U,board,now.strftime("%Y-%m-%d"))

 #print "Fetched "+str(COUNT)+" images, put in "+PATH_U+board+"\\"+now.strftime("%Y-%m-%d")

def imgg(url, folder, sort, thread):
    page = pgld(url)
    im = parseim(page)
    folder = folderchk(folder,sort,thread)
    getimage(im,folder)

def pgld(url):
    #print url
    pg = urllib.urlopen(url)    ##Here we fetch the HTML code and store is as a char array
    for lines in pg.readlines():
        page =  lines
    return page

def folderchk(folder, sort, thread):
    now = datetime.datetime.now()
    #if folder == "":
       # folder = now.strftime("%Y-%m-%d")
    if sort == '':
        folder = folder + "/" + now.strftime("%Y-%m-%d")
    elif sort == 't':
        folder = folder + "/" + now.strftime("%Y-%m-%d") + "/" + thread

    if os.path.exists(PATH_U + folder):  ##Check if such a folder exists
        return folder
    else :
        os.makedirs(PATH_U + folder)     ##If not, then we make one

    return folder

def parsethrd(page,site):
    threads = []
    for i in range(len(page)):
        if page[i] == 't' and page[i+1].isdigit(): #or page[i+1] == '2' or page[i+1]== '3' or page[i+1] == '4' or page[i+1] == '5' or page[i+1] == '6' or page[i+1] == '7' or page[i+1] == '8' or page[i+1] == '9'
            c = i
            while page[c] != '"':
                c = c+1
            if page[c-1].isdigit():
                threads.append(page[i+1:c])
            i = c
        elif site == '7' and page[i] == 'r' and page[i+9] == '_': #for 7chan, this finds the quickreply code in order to generate the threads
            c = i + 1
            while page[c] != '"':
                c = c+1
            threads.append(page[i+1:c])
            i = c

    return threads

def parseim(page):
    images = []
    for i in range(len(page)):
        if page[i] == '/' and page[i+1] == '/' and page[i+2] =='i' and page[i+3] == '.' and page[i+4] == '4':
            c = i
            while page[c] != '"':
                c = c+1
            images.append(page[i:c])
            i = c

    return images

def getimage(images,folder):
    x = 0
    for i in range(len(images)):
        if i<len(images)-2 and images[i] == images[i+1]:
            i = i+1
        else:
            images[i] = "https:" + images[i]
            t = images[i]
            ext = PATH_U + folder +"/" + t[t.rfind('/')+1:]
            count()
            if VERB: print "getting image " + images[i]
            urllib.urlretrieve(images[i], ext)


        #f = open(nme,'w')
        #f.write(dat)
        #f.close

def count():
    global COUNT
    COUNT = COUNT + 1


if __name__ == "__main__":
    main()





