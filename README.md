# mailer
Simple python mailer

Please, use python 3.6 or higher!


The Story

My friens need to send one simple question to their 93 fellas in order to get feedback. They ask me to help him, to automate this. So, here we are. 

How does it work?
1. All files from this git should be stored in one folder
2. Script load list of your recipients from file 2send.xlsx
3. Script load mailing parameters from file 3ini.xlsx
4. Script 1send.py - mail to all 2send.xlsx recipients your queston. You should run this script
5. Script 2get.py det all answers sturting current week monday till now and email you results.
Thats it.

How to use this script?
1. You should create special Email address for this. For example: yourownspecialmail@gmail.com. You should store password safely,
2. You should store all files from this GitHub project into one folder,
3. You edit file 3ini.xlsx,
3.1 Instead of 'yourownspecialmail@gmail.com' - you enter your special email,
3.2 Instead of 'yourownpassword' - you enter your special email password,
3.3 Instead of 'Xmas invitation' - you enter your theme,
3.4 Instead of 'Hi! If U are going to come, please, answer this mail. If NOT - do NOT answer!' - you enter your YES/NOT question,
3.5 Instead of 'myfirstemail@gmail.com;mysecondemail@gmail.com' - you enter your current email,
3.6 Instead of 'Xmas invitation results' - you enter your resuting email theme,
3.7 Instead of 'Will come: ' - you enter your resuting email text,
4. Install python (if you use macOs or Linux, skip this step) - from
5. Run 1send.py
6. Run 2get.py
