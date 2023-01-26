from ast import Bytes
from JSONfile import*
import threading
import socket

SERVER_IP = "127.0.0.1"  # loopback dia chi cua may chay
SERVER_PORT = 59300
BUFFER = 1024
FORMART = "utf8"
NUMBER_CONNECTOR = 3
connector = 1

#hàm nhận message (message ngắn dưới 1024 byte)
def recieveLittleThing(connect):
    result = connect.recv(BUFFER).decode(FORMART)
    connect.sendall('success'.encode(FORMART))
    return result
#hàm gửi message (message ngắn dưới 1024 byte)
def sendLittleThing(string, connect):
    connect.sendall(string.encode(FORMART))
    trunggian = connect.recv(BUFFER).decode(FORMART)

#hàm đăng ký đăng nhập
def checkUser(connect): #đăng ký đăng nhập
    type = recieveLittleThing(connect)
    if type=='0': #log_in
        user = recieveLittleThing(connect)
        passw = recieveLittleThing(connect)
        return login_check(user, passw), user

    if type=='1': #sing_up
        user = recieveLittleThing(connect)
        passw = recieveLittleThing(connect)
        if (username_check(user)):
            return False, user
        else:
            save_new_account(user, passw)
            return True, user

#hàm check id của note
def check_Id(connect, user):
    id = recieveLittleThing(connect)
    check = id_check(user, id)
    sendLittleThing(str(check),connect)
    return

#hàm trả về đuôi file
def returnFileTail(path):
    i = len(path)-1
    while (i > 0):
        if path[i] =='.':
            index = i
            break
        i -= 1
    tail = path[index:len(path)]
    return str(tail)

# hàm nhận note từ client và lưu vào database
def saveNewNote(connect, user):    
    id = recieveLittleThing(connect)
    type = recieveLittleThing(connect)

    if (type == 'text'):
        lenght = int(recieveLittleThing(connect))
        if (lenght == 0):
            return
        content = connect.recv(BUFFER)
        lenght -= len(content)

        while (lenght > 0):
            trunggian = connect.recv(BUFFER)
            content += trunggian
            lenght -= len(trunggian)
        
        path = f'userDatabase/' +user +'/' + id + '.txt'
        f = open(path, 'wb')
        f.write(content)
        f.close()
        save_new_note(user, id, type, path)

    elif (type == 'image') or (type == 'files'):
        fileTail = recieveLittleThing(connect)
        filesize = int(recieveLittleThing(connect))
        path = f'userDatabase/' +user +'/' + id + fileTail
        f = open(path, 'wb')
        while (filesize > 0):
            trunggian =connect.recv(BUFFER)
            f.write(trunggian)
            filesize -= len(trunggian)
        f.close()
        save_new_note(user, id, type, path)

#hàm gửi danh sách các note theo dạng dict {<id>:<type>,...} cho client
def sendDict(connect, user):
    list = json.dumps(view_note(user)).encode(FORMART)
    sendLittleThing(str(len(list)),connect)
    connect.sendall(list)

#hàm gửi note qua client
def sendNoteForDownload(connect, user):
    id = recieveLittleThing(connect)
    type, path = read_note(user, id)
    sendLittleThing(type, connect)
    sendLittleThing(user, connect)

    if type == 'text':
        f = open(path, 'rb')
        content = f.read(BUFFER)
        while (True):
            trunggian = f.read(BUFFER)
            if (not trunggian):
                break
            content += trunggian
        
        sendLittleThing(str(len(content)), connect)
        connect.sendall(content)
        f.close()

    elif (type == 'image') or (type == 'files'):
        filetail = returnFileTail(path)
        sendLittleThing(filetail, connect)

        filesize = os.path.getsize(path)
        sendLittleThing(str(filesize),connect)
            
        f = open(path, 'rb')
        trunggian = f.read(BUFFER)
        while (trunggian):
            connect.sendall(trunggian)
            trunggian = f.read(BUFFER)
        f.close()
    

def sendNoteForView(connect, user):
    id = recieveLittleThing(connect)
    type, path = read_note(user, id)
    sendLittleThing(type, connect)
    sendLittleThing(user, connect)

    if type == 'text':
        f = open(path, 'rb')
        content = f.read(BUFFER)
        while (True):
            trunggian = f.read(BUFFER)
            if (not trunggian):
                break
            content += trunggian
        
        sendLittleThing(str(len(content)), connect)
        connect.sendall(content)
        f.close()

    elif (type == 'image'):
        filetail = returnFileTail(path)
        sendLittleThing(filetail, connect)

        filesize = os.path.getsize(path)
        sendLittleThing(str(filesize),connect)
            
        f = open(path, 'rb')
        trunggian = f.read(BUFFER)
        while (trunggian):
            connect.sendall(trunggian)
            trunggian = f.read(BUFFER)
        f.close()
    
    elif (type == 'files'):
        pass

#hàm vận hành
def handleClient(connect, address):
    try:
        user = ''
        while(True): #login/signup
            check, user = checkUser(connect)
            if check: 
                sendLittleThing(str(check),connect)
                print(user)
                print(check)
                break
            else:
                sendLittleThing(str(check),connect)
                print(user)
                print(check)
        print(address,': ' 'log in success')
        while(True): #actions with note
            process = recieveLittleThing(connect)
            print(address, ':', process)
            if (process == 'checkId'):
                check_Id(connect, user)
            elif (process == 'saveNewNote'):
                saveNewNote(connect, user)
            elif (process == 'viewList'):
                sendDict(connect, user)
            elif (process == 'requireNoteForView'):
                sendNoteForView(connect, user)
            elif (process == 'requireNoteForDownload'):
                sendNoteForDownload(connect, user)
            elif(process == 'quit'):
                break
    except:
        print("Client suddenly closed: " , address)
    finally:
        global connector
        connector -=1
        print("Close connect with client: ", address)
        connect.close()

def mainFunction():
    global connector
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT)) #Host server tai day

    server.listen()
    print('Server is now available')
    while(connector <= NUMBER_CONNECTOR):  
        try: 
            connect, address = server.accept()
            print('There is a new connector: ', address)
            print ('The number of connectors: ', connector)
            print()
            connector += 1
            thread = threading.Thread(target= handleClient, args = (connect,address))
            thread.daemon = False #khi hàm chính end thì thread vẫn duy trì
            thread.start()
        except:
            print("There is an error")

    print('Server is not available')
    server.close()

if (__name__ == '__main__'):
    mainFunction()