import socket
def ping():
    w = input("say me site:")
    print ()
    p = socket.gethostbyname(w)
    print("Ip site " , p )
    sa = input ("if you want save file succefuly plz type (save)")
    if sa == 'save':
        a = open("amir.txt" , "w")
        a.write(p)
        print ("if you want see your file go this addres (amir,txt)")
ping()
