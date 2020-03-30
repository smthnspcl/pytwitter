## pytwitter
### deprecated, use [twint](https://github.com/twintproject/twint)
using twitter without their api<br>
### how to...
#### ... install
```shell script
pip3 install git+https://github.com/smthnspcl/pytwitter
```
#### ...use from cli
```shell script
$ ./twitter.py --help
usage:
	unix: ./twitter.py {arguments}
	win:  .\twitter.exe {arguments}
{arguments}			{description}		{default}
	-u	--username	add a username		None
	-o	--output	set output dir		out
	-c	--count		count of tweets		1000
{example}
.\twitter.exe -u s8n -u theydeadinside -o dankmemes
    \-> executable|       \-> 2nd username    \-> output folder
                  \-> 1st username
```
#### ... use from code
```python
from pytwitter import Twitter

username = "s8n"
twitter = Twitter()  # initialize twitter object
user = twitter.get_user(username)  # get user via twitter object
print(user.__dict__)
twitter.close()  # close webdriver in twitter object
```
or see the examples folder.