msg=input("Enter your message: ")

with open("msg.txt","a",encoding="utf-8") as f:
    msg=msg[::-1]
    for s in msg:
        f.write(s+"\n")
    print("Meddelandet har skrivits till filen.")