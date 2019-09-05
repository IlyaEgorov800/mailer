# mailer
Simple python mailer

Please, use python 3.6 or higher!


The Story

My friens need to send one simple question to their 93 fellas in order to get feedback. They ask me to help him, to automate this. So, here we are. You should be 'IT guy' a little.

How does it work?
1. All files from this git should be stored in one folder
2. Script loads list of your recipients from file 2send.xlsx
3. Script loads mailing parameters from file 3ini.xlsx
4. 1send.py script mails to all 2send.xlsx recipients your queston. You should run this script
5. 2get.py script gets all answers starting 'current week monday' till now and email you results.
Thats it.

How to use this script?
1. You should create special gmail address for this. For example: yourownspecialmail@gmail.com. You should store password safely,
2. You should store all files from this GitHub project into one folder,
3. You edit file 3ini.xlsx,
3.1 Instead of 'yourownspecialmail@gmail.com' - you enter your special email,
3.2 Instead of 'yourownpassword' - you enter your special email password,
3.3 Instead of 'Xmas invitation' - you enter your theme,
3.4 Instead of 'Hi! If U are going to come, please, answer this mail. If NOT - do NOT answer!' - you enter your YES/NOT question,
3.5 Instead of 'myfirstemail@gmail.com;mysecondemail@gmail.com' - you enter your current email,
3.6 Instead of 'Xmas invitation results' - you enter your resuting email theme,
3.7 Instead of 'Will come: ' - you enter your resuting email text,
4. Install python
4.1 Windows - run installation from https://www.python.org/downloads/, button looks like 'Download Python 3.7.4'. Mark 'Add Python 3.x to PATH' when you will asked for. 
4.2 macOs - find instruction here https://www.python.org/downloads/mac-osx/ 
4.3 Linux - find instruction here https://www.python.org/downloads/source/
5. Run 1send.py - using command 'python yourfolder\1send.py'
5.1 Wait for answers
6. Run 2get.py - using command 'python yourfolder\2get.py'

Ask me questions!
