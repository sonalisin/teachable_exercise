# Set up

## Python installation

Check you have Python installed. This should be Python3,

you can do this by running

`python3 --version`

and you'll probably see something like:

`Python 3.10.8`

## Set up directory

You then want to open a command line program to this directory, which you can see by typing `cd` for Windows, and `pwd` for Mac.

This will look something like this, and you can make sure you're in the correct directory.

`/Users/your_user/Desktop/ai_project/teachable_project`

### Teachable model files into working directory

Take your downloaded Teachable machine project, and take the `keras_model.h5` file, and the `labels.txt` file and place it into the folder.

## Create a virtual environment

Now, you want to create a virtual environment. This is a good thing - it means our dependencies stay within the universe of this project and doesn't mess with our global computer dependencies.

`python3.10 -m venv ./teachable`

In your folder, you should now see a new folder created called "teachable". This is expected.

Now we need to enter into the virtual environment.

### Windows

Powershell: `teachable\Scripts\Activate.ps1`
or
cmd.exe: `teachable\Scripts\activate.bat`

### Mac / Linux

`source ./teachable/bin/activate`

Your command line should look something like:

`(teachable) [(base)] user@machine teachable_project `

Now, you want to run

`pip3 install -r requirements.txt` to install the dependencies.

## Deactivating the virtual environment

This will usually be `deactivate`. Make sure you deactivate it once you want to leave the project!
