## ELF x86 - Stack buffer overflow basic 1

*Vulnerability* : Possibility of overflow where the size of the input exceeds the size of the given arrray & setuid binary
*Objective* : Overwriting the integer variable 'check' to match the condition to open a shell

1. ssh connection to server
2. Set payload as 'A'*40 + p32[0xdeadbeef] : Original array + Value to be overwritten
