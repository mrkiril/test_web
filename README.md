## Running Locally

Make sure you have Python 3 [installed properly](https://www.python.org/) and 
cheak that you have install [GIT](https://git-scm.com/)

Of course you must have [MySQL](https://www.mysql.com/) or [MariaDB](https://mariadb.com/resources/blog/how-connect-python-programs-mariadb).

I use  MAriaDB couse it`s open souse
```gh
$ sudo apt-get update
$ sudo apt-get install python-pip python-dev mariadb-server libmariadbclient-dev libssl-dev
$ sudo mysql_secure_installation

$ mysql -u root -p
$ CREATE DATABASE test_project CHARACTER SET UTF8;
$ CREATE USER test_projectuser@localhost IDENTIFIED BY 'test_password';
$ GRANT ALL PRIVILEGES ON myproject.* TO myprojectuser@localhost;
$ FLUSH PRIVILEGES;
$ exit
```

Done. Great.
## NEXT STEP

Create our environment
```sh
$ sudo pip install virtualenv
$ mkdir ~/myproject
$ cd ~/myproject
$ virtualenv myprojectenv
$ source myprojectenv/bin/activate

```
After all of it you must see something like this (myprojectenv)user@host:~/myproject$

## Final step
```sh
$ mkdir ~/app
$ cd ~/app
$ git clone git@github.com:mrkiril/test_web.git
$ cd python-getting-started
$ pip install -r requirements.txt
$ python3 manage.py runserver

```
in your browser enter 127.0.0.1:5000/

## HOW TO USE IT

Your start page it is login page.
Of course now you don`t have any account.
Click to the Register link and create your first account.

