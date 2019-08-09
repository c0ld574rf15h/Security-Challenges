## Bash System-1

**Vulnerability** : Non-absolute path for the ls command within the system function of the given binary.

**Objective** : Making a fake ls command linked to /bin/cat & preempt the original ls command by altering the PATH environment variable

1. Generate a soft link ls -> /bin/cat in the /tmp directory
2. Add the directory path where the link lies to the PATH environment [ export PATH=/tmp/coldfish:$PATH ]
3. Return to the home directory and execute the program -> reads the prohibited password file with elevated privilege
