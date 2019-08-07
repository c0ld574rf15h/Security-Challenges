##sudo - weak configuration


*Vulnerability* : sudo permission for /bin/cat & wildcard in file path --> read permission for every file in the system with the privilege of the dedicated user
*Objective* : Concatenating the file path for .passwd after a normal one since the wildcard expropriates space characters

1. Check permission using `sudo -l`
2. Read the password file by typing the command `sudo -u app-script-ch1-cracked /challenge/app-script/ch1/ch1/shared_notes ./ch1cracked/.passwd`