import socket
import os
import json

SERVER_IP = "192.168.159.172" #chỉnh sửa theo ipv4 của máy server nếu không chạy cùng một máy
SERVER_PORT = 59432
BUFFER = 1024
FORMART = 'utf8' #comprise Unicode and ascii

global client

def mainFunction():
    try:
        global client   
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect( (SERVER_IP,SERVER_PORT) )
    except:
        ms = 'Can\'t connect to server or another errors'
        print(ms)
        input() 

def sendLittleThing(string):
    global client
    client.sendall(string.encode(FORMART))
    trunggian = client.recv(BUFFER).decode(FORMART)

def recieveLittleThing():
    global client
    result = client.recv(BUFFER).decode(FORMART)
    client.sendall('success'.encode(FORMART))
    return result

def returnFileTail(path):
    i = len(path)-1
    while (i > 0):
        if path[i] =='.':
            index = i
            break
        i -= 1
    tail = path[index:len(path)]
    return str(tail)

def check_Id(Id, sign):
    #0 là viewnote 1 là addnote
    if (Id == ''):
        if sign == 0:
            return False
        return True

    if (len(Id) > BUFFER):
        if sign == 0:
            return False
        return True

    sendLittleThing('checkId')
    print(Id)
    sendLittleThing(Id)
    check = recieveLittleThing()
    if (check == 'True'):
        return True
    else:
        return False

#hàm lưu note mới gửi note qua cho server
def sendNewNote(type, Id, content):
    sendLittleThing('saveNewNote')
    sendLittleThing(Id)
    sendLittleThing(type)
    global client
    if type == 'text':
        if len(content) == 0:
            sendLittleThing('0')
            return
        content = content.encode(FORMART)
        sendLittleThing(str(len(content)))
        client.sendall(content)

    elif (type == 'image') or (type == 'files'):
        filetail = returnFileTail(content)
        sendLittleThing(filetail)

        filesize = os.path.getsize(content)
        sendLittleThing(str(filesize))

        f = open(content, 'rb')
        trunggian = f.read(BUFFER)
        while (trunggian):
            client.sendall(trunggian)
            trunggian = f.read(BUFFER)
        f.close()

#hàm yêu cầu danh sách note đang có của người dùng {<id>:<type>,...}
def requireDict():
    global client
    sendLittleThing('viewList')
    lenght = int(recieveLittleThing())
    list = client.recv(BUFFER)
    lenght -= len(list)
    while (lenght > 0):
        trunggian = client.recv(BUFFER)
        list += trunggian
        lenght -= len(trunggian)
    list = json.loads(list.decode(FORMART))
    return list
        
#hàm viewnote
def requireNoteForView(Id):
    sendLittleThing('requireNoteForView')
    sendLittleThing(Id)
    type = recieveLittleThing()
    user = recieveLittleThing()
    global client

    if (type == 'text'):
        lenght = int(recieveLittleThing())
        content = client.recv(BUFFER)
        lenght -= len(content)
        while (lenght > 0):
            trunggian = client.recv(BUFFER)
            content += trunggian
            lenght -= len(trunggian)

        content = content.decode(FORMART)
        return content, type

    elif (type == 'image'):
        fileTail = recieveLittleThing()
        filesize = int(recieveLittleThing())
        folder = './Cache/' +user
        os.makedirs(folder, exist_ok = True)
        path = f'Cache/' +user +'/' + Id + fileTail
        f = open(path, 'wb')
        while (filesize > 0):
            trunggian = client.recv(BUFFER)
            f.write(trunggian)
            filesize -= len(trunggian)
        f.close()
        return path, type

    elif (type =='files'):
        return 'nothing', type

#hàm tải note
def requireNoteForDownload(Id):
    sendLittleThing('requireNoteForDownload')
    sendLittleThing(Id)
    type = recieveLittleThing()
    user = recieveLittleThing()
    global client

    if (type == 'text'):
        lenght = int(recieveLittleThing())
        content = client.recv(BUFFER)
        lenght -= len(content)
        while (lenght > 0):
            trunggian = client.recv(BUFFER)
            content += trunggian
            lenght -= len(trunggian)

        folder = './Database/' +user
        os.makedirs(folder, exist_ok = True)
        path = f'Database/' +user +'/' + Id + '.txt'
        f = open(path, 'wb')
        f.write(content)
        f.close()
        return path, type

    elif (type == 'image') or (type == 'files'):
        fileTail = recieveLittleThing()
        filesize = int(recieveLittleThing())
        folder = './Database/' +user
        os.makedirs(folder, exist_ok = True)
        path = f'Database/' +user +'/' + Id + fileTail
        f = open(path, 'wb')
        while (filesize > 0):
            trunggian = client.recv(BUFFER)
            f.write(trunggian)
            filesize -= len(trunggian)
        f.close()
        return path, type

#hàm checkuser
def checkUser(username, password, sign):
    #username and passsword no longer than 1024byte: 
    #no more than 1024 charaters in ascii code, or 512 charaters in unicode
    if (len(username) < 5 or len(password) <3):
        return False
    for x in username:
        if (x < 'a' or x >'z'):
            if (x < '0' or x > '9'):
                return False
    #tên quá dài
    if(len(username) > BUFFER or len(password) > BUFFER):
        return False
    sendLittleThing(sign)
    sendLittleThing(username)
    sendLittleThing(password)
    check = recieveLittleThing()
    if check == 'False':
        return False
    else:
        return True

#hàm đóng kết nối khi bấm nút quit
def quitClient():
    sendLittleThing('quit')
    client.close()

mainFunction()

