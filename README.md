# Media Library Organiser
###### `v1.1-rc3` `No-GUI`  

A program that'll automatically rename and organise all your offline media files.

## Getting Started


### Prerequisites
What things you need to run the program:
- Python Compiler (3.7 Recommmended)- Install the following Packages:
- strsim
 - From pypi:
 ```bash
 pip install strsim
 ```
 - or clone this repository:
 ```bash
 git clone https://github.com/luozhouyang/python-string-similarity
 cd python-string-similarity
 pip install -r requirements.txt
 ```
- imdbpy
 -From pypi:
 ```bash
 pip install imdbpy
 ```

### Update Logs
#### v1.1-rc3
* `[UPDATE]` Uses **imDB** to retrieve the most relevent movie names.
#### v1.0-rc3
* Minor Bug Fixes
* Major Improvements

### Features
*  Offline Movie files are renamed and organised in format:
```
<Movie_name> (<year>)
```
* Offline TV_Series files are renamed and organised in format:
```
<TV_Series_name>
```
* All episodes of series are renamed in the format:
```
 S<Season_number>E<Episode_Number>
```
* All episodes of a series are moved inside a folder with their corresponding Season number in it:
```
//<TV_Series_name>'//S<Season_number>//
```
End with an example of getting some data out of the system or using it for a little demo


## Authors

* **Krishna Alagiri** - *Initial work* - [KrishnaAlagiri](https://github.com/KrishnaAlagiri/)

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
