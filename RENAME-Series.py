import os
import re
import shutil
import click
# from imdb import IMDb
from imdb import Cinemagoer as IMDb
from similarity.damerau import Damerau

# Title
def title():
    # os.system('mode con: cols=90 lines=30')
    # os.system("clear")
    # print("    _       _                  _          _  ")
    # print("   /_\ _  _| |_ ___ _ __  __ _| |_ ___ __| | ")
    # print("  / _ \ || |  _/ _ \ '  \/ _` |  _/ -_) _` | ")
    # print(" /_/ \_\_,_|\__\___/_|_|_\__,_|\__\___\__,_| ")
    # print("                                             ")
    # print("  _    _ _                       ")
    # print(" | |  (_) |__ _ _ __ _ _ _ _  _  ")
    # print(" | |__| | '_ \ '_/ _` | '_| || | ")
    # print(" |____|_|_.__/_| \__,_|_|  \_, | ")
    # print("                           |__/  ")
    # print("   ___                     _             ")
    # print("  / _ \ _ _ __ _ __ _ _ _ (_)___ ___ _ _ ")
    # print(" | (_) | '_/ _` / _` | ' \| (_-</ -_) '_|")
    # print("  \___/|_| \__, \__,_|_||_|_/__/\___|_|  ")
    # print("           |___/                         ")
    pass

# Find most apt name in Series List
def find_most_apt(name, series):
    damerau = Damerau()
    deg = []
    for ss in series:
        if(name.upper() == ss.upper()):
            return(ss)
        else:
            deg.append(damerau.distance(name.upper(), ss.upper()))
    indd = int(deg.index(min(deg)))
    mostapt = series[indd]
    return(mostapt)

# Retrieves name from imDB
def main_imdb(str21):
    ia = IMDb()
    s_result = ia.search_movie(str21)
    series = []
    for ss in s_result:
        if(ss['kind'] == "tv series"):
            str2 = ss['title']
            series.append(str2)
    return(series)

# Remove illegal characters from file name
def remove_illegal(str):
    illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in illegal_chars:
        str = str.replace(char, "")
    return str.strip()

# has Condition #1
def has_x(inputString):
    return bool(re.search(r'\dx\d', inputString) or re.search(r'\d x \d', inputString))

# has Condition #2
def has_se(inputString):
    return bool(re.search(r'S\d\dE\d\d', inputString) or re.search(r'S\dE\d\d', inputString) or re.search(r's\d\de\d\d', inputString) or re.search(r's\de\d\d', inputString))

# has Condition #3
def has_sep(inputString):
    return bool(re.search(r'S\d\dEP\d\d', inputString) or re.search(r'S\dEP\d\d', inputString) or re.search(r's\d\dep\d\d', inputString) or re.search(r's\dep\d\d', inputString))

def find_name(inputString):
    inputString = inputString.replace(' x ', 'x', 1)
    filtered_list = filter(None, re.split(r'(\dx\d)', inputString))
    for element in filtered_list:
        name = element.replace('-', ' ').replace('.', ' ').strip()
        return str(name)

def find_det(inputString):
    inputString = inputString.replace(' x ', 'x', 1)
    filtered_list = filter(None, re.split(r'(\dx\d\d)', inputString))
    i = 0
    for element in filtered_list:
        det = element.replace('.', ' ').replace('-', ' ').strip()
        if i == 1:
            return str(det)
        i += 1

def find_season(inputString):
    det = find_det(inputString)
    season = det.split('x')[0]
    return str(season)

def find_episode(inputString):
    det = find_det(inputString)
    episode = det.split('x')[1]
    return str(episode)

def add_zero(inputString):
    return f'0{int(inputString)}' if int(inputString) < 10 else inputString

def split_line(text):
    return text.split()

def init(path, dry_run, verbose):
    title()
    try:
        if dry_run:
            click.echo(f"[dryrun] Creating folder {os.path.join(os.getcwd(), 'Input', 'Series')}")
        else:
            if verbose:
                click.echo(f"Creating folder {os.path.join(os.getcwd(), 'Input', 'Series')}...")
            os.makedirs(os.path.join(os.getcwd(), 'Input', 'Series'), exist_ok=True)
    except Exception as e:
        click.echo(f"Error creating directories: {e}")
    main(path, dry_run, verbose)


# Driver Code
def main(path, dry_run, verbose):

    # For Testing
    def debug(location=""):
        click.echo(f"{location}\n")
        click.echo(f"\tName: {name}")
        click.echo(f"\tSeason: {season}")
        click.echo(f"\tEpisode: {episode}")
        click.echo(f"\textension: {extn}")
        click.echo(f"\trest: {rest}")
        click.echo(f"\tFinal: {final}")
        click.echo(f"\tPath_New: {path_new}")
              
    name = season = episode = extn = rest = final = None

    if path == "NULL":
        cwd = os.getcwd()
        path = os.path.join(cwd, "Input", "Series")
        # case = 1 is CWD
        case = 1
    else:
        cwd = path
        print(path)
        # case = 2 is an optional path
        case = 2

    path_new = path_new_1 = rest = final = "NULL"
    name = ""
    copy = ""
    i = 0
    error_flag = 0
    file_flag = 0
    if verbose:
        click.echo("Reading Files....")

    media_extensions = [".mp4", ".mkv", ".srt", ".avi", ".wmv"]

    # main loop
    for dirpath, dirnames, filenames in os.walk(path):
        files = os.listdir(dirpath)
        for file in files:
            check_flag = 0
            temp = file
            extn = file[-4:]

            if any(file.endswith(ex1) for ex1 in media_extensions):
                title()
                print(f"{i} File(s) Processed....")
                rest = temp.split(extn, 1)[0]
                unwanted_stuff = [
                    ".1080p", ".720p", "HDTV", "x264", "AAC", "E-Subs", "ESubs", "WEBRip", "WEB", "BluRay",
                ]
                for stuff in unwanted_stuff:
                    rest = rest.replace(stuff, "")
                rest = rest.replace(".", " ")
                # Specifically written for'x' type Files
                if has_x(file):
                    check_flag = 1
                    name = find_name(rest)
                    season = find_season(rest)
                    episode = add_zero(find_episode(rest))
                    final = f"S{add_zero(find_season(rest))}E{episode}{extn}"
                    if verbose > 1:
                        debug("has_x")
                # Specifically written for 'S__E__' type Files
                elif has_se(file):
                    name = ""
                    words = split_line(rest)
                    if verbose > 1:
                        click.echo(f"[verbose] words:[{words}]", err=True)
                    for word in words:
                        if has_se(word) or has_sep(word):
                            final = word
                            break
                        else:
                            name += word + " "
                    brackets_ = re.findall(r'\((.*?)\)', name)
                    if verbose > 1:
                        click.echo(f"[verbose] brackets_:[{brackets_}] in name:[{name}]", err=True)
                        debug("has_se")
                    for yy in brackets_:
                        try:
                            name = name.replace(yy, "")
                        except:
                            pass
                    if name != copy:
                        copy = name
                        series = main_imdb(name)
                        name = find_most_apt(name, series)
                        name = remove_illegal(name)
                        name = name.strip()
                        restore = name
                    else:
                        name = restore
                    temp_final = final.strip().replace('S', "")
                    season = temp_final.split('E', 1)[0]
                    episode = temp_final.split('E', 1)[1]
                    final = final + extn
                    check_flag = 1
                    if verbose > 1:
                        debug("final")

            if check_flag == 1:
                if case == 1:
                    path_new = os.path.join(cwd, "Output", "Series", name)
                    path_new_1 = os.path.join(path_new, f"Season {int(season)}")
                elif case == 2:
                    path_new = os.path.join(cwd, name)
                    path_new_1 = os.path.join(path_new, f"Season {int(season)}")

                if verbose:
                    print(f"Name: {name}, Season: {season}, Episode: {episode}, Path: {path_new_1}")

                if dry_run:
                    click.echo(f"[dryrun] Creating folder Output: {path_new_1}")
                else:
                    os.makedirs(path_new_1, exist_ok=True)
                
                try:
                    if dry_run:
                        click.echo(f"[dryrun] rename({os.path.join(dirpath, file)} -> {os.path.join(path_new_1, final)}")
                    else:
                        os.rename(os.path.join(dirpath, file), os.path.join(path_new_1, final))
                except FileExistsError:
                    print(f"Error - File Already Exist: {name}/Season {int(season)}/{final}")
                    file_flag = 1
                    error_flag = 1
                    i -= 1

                i += 1

    """Result Generation"""
    title()
    print("All Files Processed...")
    if file_flag == 1:
        print("Solution: Try again after removing the above file(s) from Output folder")
    if i > 0 or error_flag == 1:
        print(f"{i} File(s) Renamed and Organised Successfully")
    else:
        print("No Media File Found in Input Folder")

@click.command()
@click.option('--path', '-p', default="NULL", help='Path to organize TV Shows')
@click.option('--dry-run', is_flag=True, help='Perform a trial run with no changes made')
@click.option('--verbose', "-v", count=True, help='Show verbose output')
def cli(path, dry_run, verbose):
    """Automate the boring process of renaming files for your TV Shows library."""
    init(path, dry_run, verbose)

if __name__ == '__main__':
    cli()
