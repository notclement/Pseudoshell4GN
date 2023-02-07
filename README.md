# Pseudoshell4GN
Psuedoshell for GoatNode, exploiting Server-side JavaScript Code Injection 

# Setup
1. Set up NodeGoat with Docker (https://github.com/OWASP/NodeGoat)
2. `python3 pshell.py`
3. ???

# What is vulnerable?
- Server-side using `eval()` on user supplied inputs (`preTax`, `roth`, `afterTax`) in `/contributions`

# How it works?
1. Script will log in with default creds (given in project page)
2. Go to vulnerable page (`"/contributions"`)
3. Wait for user to input a command to execute on the server
3. Send `POST` request with command given as a payload and command output sent to a file on the server
4. Send `POST` request with command to read the file that contains the command output
5. Server returns the command output back and it's displayed to you
5. Rinse & Repeat until `exit` command is given by you

# Why pseudoshell here?
Tried other payloads to get a shell but the nc dies instantly, might be protected with some outbound firewall rules on the server-side. At least I know it at least tries to reach out?

# In action
![image](https://user-images.githubusercontent.com/19283318/217329946-4a933694-8978-4341-abeb-7955b1fa68b7.png)
