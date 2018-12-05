##Under Constructions
import os
import re
import msvcrt
from imdb import IMDb
from similarity.damerau import Damerau

def find_most_apt(name, movies):
    damerau = Damerau()
    deg = []
    for movie in movies:
        if(name.upper() == movie.upper()):
            return(movie)
        else:
            deg.append(damerau.distance(name.upper(), movie.upper()))
    indd = int(deg.index(min(deg)))
    mostapt = movies[indd]
    return(mostapt)

def Find(string):
    url = re.findall('www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url

def lastIndexOf(str1,toFind):
    index = len(str1)-1
    i = 0
    for ch in str1:
        if(ch == toFind):
            index = i
        i+=1
    return(index)

def main_imdb(str21):
    ia = IMDb()
    s_result = ia.search_movie(str21)
    movies = []
    for movie in s_result:
        if(movie['kind'] == 'movie'):
            str2 = movie['title']
            try:
                year_str= movie['year']
            except:
                year_str= "----"
            movies.append(str2+" ("+str(year_str)+")")
    return(movies)

def removeIllegal(str):
    str=str.replace('<',"")
    str=str.replace('>',"")
    str=str.replace(':',"")
    str=str.replace('"',"")
    str=str.replace('/',"")
    str=str.replace('\\',"")
    str=str.replace('|',"")
    str=str.replace('?',"")
    str=str.replace('*',"")
    return(str)

def Title():
    os.system("cls")
    os.system('mode con: cols=75 lines=30')
    print("    _       _                  _          _  ")
    print("   /_\ _  _| |_ ___ _ __  __ _| |_ ___ __| | ")
    print("  / _ \ || |  _/ _ \ '  \/ _` |  _/ -_) _` | ")
    print(" /_/ \_\_,_|\__\___/_|_|_\__,_|\__\___\__,_| ")
    print("                                             ")
    print("  _    _ _                       ")
    print(" | |  (_) |__ _ _ __ _ _ _ _  _  ")
    print(" | |__| | '_ \ '_/ _` | '_| || | ")
    print(" |____|_|_.__/_| \__,_|_|  \_, | ")
    print("                           |__/  ")
    print("   ___                     _             ")
    print("  / _ \ _ _ __ _ __ _ _ _ (_)___ ___ _ _ ")
    print(" | (_) | '_/ _` / _` | ' \| (_-</ -_) '_|")
    print("  \___/|_| \__, \__,_|_||_|_/__/\___|_|  ")
    print("           |___/                         ")
    print("")


def FormatStr(temp):
    rest = temp
    if ".1080p" in temp:
        sep = ".1080p"
    elif ".720p" in temp:
        sep = ".720p"
    elif "[" in temp:
        sep = "["
    elif "1080p" in temp:
        sep = "1080p"
    elif "720p" in temp:
        sep = "720p"
    if "TamilRockers" in temp:
        temp = temp.split(' - ',1)[1]
    try:
        rest = temp.split(sep,1)[0]
    except:
        pass
    rest = rest.replace("."," ")
    rest = rest.replace("(","")
    rest = rest.replace(")","")
    return(rest)

#Driver Code
Title()
try:
    os.mkdir("Input")
except FileExistsError:
    pass
try:
    os.mkdir("Input\\Movies")
except FileExistsError:
    pass
try:
    os.mkdir("Output")
except FileExistsError:
    pass
path = "Input\\Movies"
i=0
ErrorFlag=0
FileFlag=0
files = os.listdir(path)
for file in files:
    temp = file
    extn = file[(len(file)-4) : len(file)]

    if(file.endswith(".mp4") or file.endswith(".mkv") or file.endswith(".srt")) :
        Title()
        print(str(i)+" File(s) Processed....")
        rest = FormatStr(temp)
        year_str =  '('+ rest[len(rest)-4 : len(rest)] +')'
        rest = rest[0:len(rest)-4]
        Final = rest + year_str
        print("Derived: ",Final)
        movies = main_imdb(rest + year_str)
        rest = find_most_apt(Final, movies)
        rest = removeIllegal(Final)
        Final = rest + extn
        print("Most Apt: ",Final)
        print()

###############################################################################
##RENAME HAPPENS HERE
        path_new = os.getcwd() + "\\Output\\Movies\\" + rest
        try:
            os.mkdir("Output")
        except FileExistsError:
            pass
        try:
            os.mkdir("Output\\Movies")
        except FileExistsError:
            pass
        try:
            os.mkdir(path_new)
        except FileExistsError:
            pass
        try:
            os.rename(os.path.join(path, file), os.path.join(path_new, Final ))
        except:
            print("Error - File Already Exist: "+rest )
            FileFlag=1
            ErrorFlag=1
            i=i-1;
        i=i+1

###############################################################################
##RESULT GENERATION
Title()
print ("All Files Processed...")
if(FileFlag==1):
    print("Solution: Try again after removing the above file(s) from Output folder")
if(i>0 or ErrorFlag==1):
    print(str(i)+" File(s) Renamed and Organised Successfully")
    if(i>0): os.system("explorer.exe " + str(os.getcwd() + "\Output\\"))
else:
    print("No Media File Found in Input Folder")
print("Enter any key to exit...")
print()
msvcrt.getch()
