Travers Media Tools
===================

Outline
-------

Travers Media Encoder is a cloud-based video and audio encoder that allows a user to convert media from one format to another over the web, with the actual transcoding being done on a server and then letting them download the result. Thanks to filepicker.io, the user can upload files from their own cloud storage service such as Dropbox without having the file locally. It is written in Python and uses the Django framework, libav encoding tools, SQLite and runs on linux.

* [Video Demonstration](http://www.youtube.com/watch?v=UMhja2z2y34)
* [Source Code](https://github.com/thethomaseffect/travers-media-tools)

Installation
------------

This assumes you are running on ubuntu linux machine with python already installed. First we install our dependencies using the command-line.

```shell
sudo apt-get install git python-pip libav-tools
```

git will allow us to download the code from github. pip is a python package manager that'll let us easily install our third-party libraries and libav is the encoding tools used for the actual conversion.

Next we prepare a directory to download the code to and clone the git repository.

```shell
mkdir git-repos
cd git-repos/
git clone https://github.com/thethomaseffect/travers-media-tools.git
```

Now we install the required python libraries (the web framework is one of them!)

```shell
pip install pexpect django
```

Lastly, your own filepicker.io API key must be added to /encoder/settings.py


Running
-------

Now we're ready to go! We'll build the database and run the test server! If you're prompted to create a superuser/admin type 'no' and hit return.

```shell
cd git-repos/travers-media-tools/encoder/
python manage.py syncdb
python manage.py runserver
```

if you're already running something on port 8000, just add a space and a new port number after runserver.

If everything was done right, the server should now be running and available on localhost:8000. Open your web browser, go to the address and upload a media file. I can only guarantee that the included input_small.mkv will work correctly, though many more should work. After hitting upload and waiting a while the page will refresh and you should be able download your new file. Congrats!

Contact Me
----------

If you've any questions or need any help running this software I'm available at github-username at gmail.com. I don't have much time to work on this so all pull requests appreciated :)
