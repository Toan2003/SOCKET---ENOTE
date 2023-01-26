from importlib.resources import path
from tkinter import *
import tkinter.font
from turtle import back, color
from PIL import ImageTk, Image
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import filedialog
from Client import *
WIDTH = 1800
HEIGHT = 800


mainFunction()


#Root widget 
root= Tk()
root.title('E-NOTE')

#adjust size
root.geometry("564x766")
canvas1= Canvas(root, width = 564, height = 766)
canvas1.pack(fill = "both", expand = True)
bg = ImageTk.PhotoImage(Image.open("bgfinal.png"))
font_title=tkinter.font.Font(family = "System", size = 80, weight = "bold")
font_title2=tkinter.font.Font(family = "System", size = 20, weight = "bold")
font_title3=tkinter.font.Font(family = "Pristina", size = 15, weight = "bold")
font_title4=tkinter.font.Font(family = "Lucida Console", size = 20, weight = "bold")
font_button=tkinter.font.Font (family="Times New Roman", size=15, weight="bold")

def welcomepage():
    canvas1.delete("all")
    canvas1.create_image( 0, 0, image = bg, 
                        anchor = "nw")
    loginButton= Button (root, text="Log in", command=clicLogIn, width=10, height=1)
    loginButton['font']=font_button
    signupButton= Button (root,text="Sign up", command=clicSignUp, width=10, height=1)
    signupButton['font']=font_button
    loginButton_canvas= canvas1.create_window(270,200,window = loginButton)
    
    singupButton_canvas= canvas1.create_window(270,280,window = signupButton)
    quit=Button(root, text="Quit", command= quitProgram,width=10, height=1)
    quit['font']=font_button
    quit_canvas=canvas1.create_window(270,360,window=quit)
    canvas1.create_text(282,100, text="E-NOTE", font=font_title, justify="center")
    #Create font title
    text=canvas1.create_text(282,100, text="E-NOTE", font=font_title, justify="center")

# Page login  
def clicLogIn():
    #Delete button and text -> blan page
    canvas1.delete("all")
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text(282,100, text="E-NOTE", font=font_title, justify="center")
    backWelcomePage()

    #create Login page
    un=Entry(root)
    pw=Entry(root, show='*')
    #Lay chu 
    
    def checkLogin():
        user=un.get()
        password=pw.get()
        if (not checkUser(user, password, '0')):
            tkinter.messagebox.showinfo(title="Error", message="Password or username is wrong or invalid")
            un.delete(0,END)
            pw.delete(0,END)
        else:
            menuPage()

    un_canvas=canvas1.create_window(280,180, window= un)
    pw_canvas=canvas1.create_window(280,210, window= pw)
    enterUn=canvas1.create_text(180,180, text="Username")
    enterPw=canvas1.create_text(180,210, text="Password")
    enterButton1= Button (root, text="Log in", bg="Blue", fg="white", command= checkLogin)
    enterButton1_canvas=canvas1.create_window(280,240, window=enterButton1)

#Page SignUp
def clicSignUp():
    canvas1.delete("all")
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text(282,100, text="E-NOTE", font=font_title, justify="center")
    backWelcomePage()

    un=Entry(root)
    pw=Entry(root, show='*')

    def checkSignUp():
        user=un.get()
        password=pw.get()
        if (not checkUser(user, password, '1')):
            tkinter.messagebox.showinfo(title="Error", message="Password or username is wrong or invalid")
            un.delete(0,END)
            pw.delete(0,END)
        else:
            menuPage()
        
    un_canvas=canvas1.create_window(280,180, window= un)
    pw_canvas=canvas1.create_window(280,210, window= pw)
    enterUn=canvas1.create_text(180,180, text="Username")
    enterPw=canvas1.create_text(180,210, text="Password")
    enterButton2= Button (root, text="Sign Up", bg="Blue", fg="white", command=checkSignUp)
    enterButton2_canvas=canvas1.create_window(280,240, window=enterButton2)

def backWelcomePage():
    backButton= Button (root, text="<-", command=welcomepage)
    backButton_canvas=canvas1.create_window(15,15, window=backButton)

def downloadFile():
    global Id
    path, type = requireNoteForDownload(Id)
    tkinter.messagebox.showinfo(title="Notice", message="File was successfully downloaded in below Path: " + path)
    return


def receiveDictionary():
    global idList
    idList = requireDict() 
    return

#viewnote: Id,Content,Type
def clickViewNote():
    def partOfMenu():
        global canvas1
        canvas1= Canvas(root, width = 564, height = 766)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image(0,0, image = bg, 
                        anchor = "nw")
        addNew= Button(root, padx=10, text="+ Add new", command=clickAddNew, width=10, height=1)
        addNew['font']=font_button
        addNew_canvas=canvas1.create_window(280,200, window=addNew)
        viewNote= Button(root, text="View note", command= clickViewNote,width=11, height=1)
        viewNote['font']=font_button 
        viewNote_canvas=canvas1.create_window(280,250,window=viewNote)
        quit=Button(root, text="Quit", command= quitProgram,width=11, height=1)
        quit['font']=font_button
        quit_canvas=canvas1.create_window(280,300,window=quit)
        canvas1.create_text(282,100, text="E-NOTE", font=font_title, justify="center")
        canvas1.create_text(282,100, text="E-NOTE", font=font_title, justify="center")

    def menuPageWithCanvas():
        sample_text.destroy()
        viewButton.destroy()
        inputId.destroy()
        id.destroy()
        frame1.destroy()
        returnMenu.destroy()
        partOfMenu()

    def menuPageWithCanvas2():
        id.destroy()
        downloadButton.destroy()
        returnMenu2.destroy()
        partOfMenu()

    def menuPageWithCanvas3():
        sb_ver.destroy()
        id.destroy()
        downloadButton.destroy()
        returnMenu3.destroy()
        text_box1.destroy()
        partOfMenu()

    def menuPageWithCanvas4():
        id.destroy()
        downloadButton.destroy()
        returnMenu4.destroy()
        partOfMenu()

    canvas1.destroy()
    root.config(bg='#0093b5')

    def checValidNote():
        global Id
        Id = id.get()
        #Kiểm tra có trùng ko
        if (not check_Id(Id,0)):
            tkinter.messagebox.showerror(title="ERROR", message="ID hong ton tai")
        else:
            Content, TypeFile = requireNoteForView(Id)
            #typeFile="Picture" #chừa chỗ cho m viết
            returnMenu.destroy()
            viewButton.destroy()
            inputId.destroy()
            id['state']=DISABLED
            sample_text.destroy()
            global downloadButton
            downloadButton=Button(root, text="Download", command=downloadFile, padx=15, bd=5)
            downloadButton.pack()
            if (TypeFile=="image"):
                global returnMenu2
                returnMenu2= Button(root, text="Return", command=menuPageWithCanvas2, padx=15, bd=5)
                returnMenu2.pack()
                #Đoạn này bỏ ảnh vô cái đi mày, thay chỗ writing .jpg là đường dẫn hoặc tên ảnh nè
                newWindow = Toplevel(root)
                picture= Content
                img = Image.open(picture)
                width, height = img.size
                while (width - WIDTH > 100 or height - HEIGHT >100):
                    width = width//2
                    height = height //2
                img = img.resize((width, height))
                img = ImageTk.PhotoImage(img)
                global panel
                panel = Label(newWindow, image = img)
                panel.image = img
                panel.pack()
                os.remove(Content)
                
            elif (TypeFile=="text"): 
                returnMenu.destroy()  
                global text_box1
                text_box1  = Text(
                    root,
                    height=30,
                    width=40, 
                    font=(12)  
                )
                global returnMenu3
                returnMenu3= Button(root, text="Return", command=menuPageWithCanvas3, padx=15, bd=5)
                returnMenu3.pack()
                text_box1.pack(side=LEFT,expand=True)
                global sb_ver
                sb_ver = Scrollbar(
                    root,
                    orient=VERTICAL
                    )
                sb_ver.pack(side=RIGHT, fill=Y)
                text_box1.config(yscrollcommand=sb_ver.set)
                sb_ver.config(command=text_box1.yview)
                text_box1.configure(state='normal')
                text_box1.insert(END, Content) #chỗ content này mày cũng gửi content đọc file cho t ha~
                text_box1.configure(state='disabled')
            else:
                tkinter.messagebox.showinfo(title="Notice", message="File is not supported, please download")
                global returnMenu4
                returnMenu4= Button(root, text="Return", command=menuPageWithCanvas4, padx=15, bd=5)
                returnMenu4.pack()
            
    frame1 = Frame(root)
    inputId=Label(root, text="Enter ID",bg='#0093b5', font=font_title4)
    inputId.pack()
    viewButton=Button(root,  text="View", command=checValidNote, padx=24, bd=5 )
    returnMenu=Button(root, text="Return", command=menuPageWithCanvas,  padx=20, bd=5 )
    id=Entry( width=50)
    id.pack()
    viewButton.pack(pady=10)
    returnMenu.pack()
    sample_text=Text(root, width=40, height=20)

    receiveDictionary()
    
    for x in idList:
        sample_text.insert(END, x)
        sample_text.insert(END, ': ')
        sample_text.insert(END, idList[x])
        sample_text.insert(END, '\n')
    sample_text.configure(state='disabled')
    sample_text.pack()

def quitProgram():
    quitClient()
    root.destroy()

def menuPage():
    canvas1.delete("all")

    canvas1.create_image(0,0, image = bg, 
                       anchor = "nw")
    addNew= Button(root, padx=10, text="+ Add new", command=clickAddNew, width=10, height=1)
    addNew['font']=font_button
    addNew_canvas=canvas1.create_window(280,200, window=addNew)
    viewNote= Button(root, text="View note", command= clickViewNote,width=11, height=1)
    viewNote['font']=font_button
    viewNote_canvas=canvas1.create_window(280,250,window=viewNote)
    quit=Button(root, text="Quit", command= quitProgram,width=11, height=1)
    quit['font']=font_button
    quit_canvas=canvas1.create_window(280,300,window=quit)
    canvas1.create_text(282,100, text="E-NOTE", font=font_title, justify="center")
    #canvas1.create_text(152,148, text="write sth...",fill="grey", font=font_title3)

def clicView():
    return

def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    global filename
    filename = filedialog.askopenfilename(title ='"pen')
    tkinter.messagebox.showinfo(title="Picture", message=filename)
    return filename

#id
def clickAddNew():
    def menuPageWithCanvas():
        checIDButton.destroy()
        addPicButton.destroy()
        addFileButton.destroy()
        title.destroy()
        textTitle.destroy()
        backMenuPageButton.destroy()
        addTextButton.destroy()
        global canvas1
        canvas1= Canvas(root, width = 564, height = 766)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image(0,0, image = bg, 
                        anchor = "nw")
        addNew= Button(root, padx=10, text="+ Add new", command=clickAddNew, width=10, height=1)
        addNew['font']=font_button
        addNew_canvas=canvas1.create_window(280,200, window=addNew)
        viewNote= Button(root, text="View note", command= clickViewNote,width=11, height=1)
        viewNote['font']=font_button
        viewNote_canvas=canvas1.create_window(280,250,window=viewNote)
        quit=Button(root, text="Quit", command= quitProgram,width=11, height=1)
        quit['font']=font_button
        quit_canvas=canvas1.create_window(280,300,window=quit)
        canvas1.create_text(282,100, text="E-NOTE", font=font_title, justify="center")
        canvas1.create_text(282,100, text="E-NOTE", font=font_title, justify="center")
        
    canvas1.destroy()
    root.config(bg='#0093b5')
    frame1 = Frame(root)
    textTitle=Label(root, text="ID",bg='#0093b5', font=font_title4)
    
    def addText():
        checIDButton.destroy()
        addPicButton.destroy()
        addFileButton.destroy()
        addTextButton.destroy()
        backMenuPageButton.destroy()

        def clickAddNew2():
            checIDButton.destroy()
            text_box.destroy()
            sb_ver.destroy()
            textTitle.destroy()
            backMenuPageButton2.destroy()
            saveButton.destroy()
            title.destroy()
            clickAddNew()

        def saveNote():
            text =text_box.get(1.0, 'end')
            global id
            sendNewNote('text', id, text)
            checIDButton.destroy()
            text_box.destroy()
            sb_ver.destroy()
            textTitle.destroy()
            backMenuPageButton2.destroy()
            saveButton.destroy()
            title.destroy()
            menuPageWithCanvas()

        id=title.get()
        title.configure(state='disabled')
        backMenuPageButton2=Button(root, text="Return",padx=21,command=clickAddNew2, bd=5)
        backMenuPageButton2.pack()
        saveButton= Button(root, text="Save!", padx=20,command=saveNote, bd=5)
        saveButton.pack()
        text_box = Text(
            root,
            height=30,
            width=40, 
            font=(12)  
        )
        text_box.pack(side=LEFT,expand=True)
        sb_ver = Scrollbar(
            root,
            orient=VERTICAL
            )
        sb_ver.pack(side=RIGHT, fill=Y)
        text_box.config(yscrollcommand=sb_ver.set)
        sb_ver.config(command=text_box.yview)

    def addPic():
        def saveNote():
            global filename
            if filename != '':
                sendNewNote('image', id, filename)
            checIDButton.destroy()
            addPicText.destroy()
            textTitle.destroy()
            backMenuPageButton3.destroy()
            saveButton.destroy()
            title.destroy()
            enterPic.destroy()
            menuPageWithCanvas()

        def clickAddNew3():
            checIDButton.destroy()
            addPicText.destroy()
            textTitle.destroy()
            backMenuPageButton3.destroy()
            saveButton.destroy()
            title.destroy()
            enterPic.destroy()
            clickAddNew()

        checIDButton.destroy()
        id=title.get()
        title.configure(state='disabled')
        addPicButton.destroy()
        addFileButton.destroy()
        addTextButton.destroy()
        backMenuPageButton.destroy()
        addPicText=Label(root, text="Input the picture",bg='#0093b5')
        addPicText.pack()
        enterPic=Button(root, text="Add", command=openfilename, padx=24, bd=5)
        enterPic.pack()
        saveButton= Button(root, text="Save!", padx=20,command=saveNote, bd=5)
        saveButton.pack()
        backMenuPageButton3= Button(root, text="Return", command=clickAddNew3, padx=24, bd=5)
        backMenuPageButton3.pack(pady=5)
        
    def addFile():
        def clickAddNew4():
            checIDButton.destroy()
            addFileText.destroy()
            textTitle.destroy()
            backMenuPageButton3.destroy()
            saveButton.destroy()
            title.destroy()
            enterFile.destroy()
            clickAddNew()

        def saveNote():
            if filename != '':
                sendNewNote('files', id, filename)
            checIDButton.destroy()
            addFileText.destroy()
            textTitle.destroy()
            backMenuPageButton3.destroy()
            saveButton.destroy()
            title.destroy()
            enterFile.destroy()
            menuPageWithCanvas()
            
        checIDButton.destroy()
        id=title.get()
        title.configure(state='disabled')
        addPicButton.destroy()
        addFileButton.destroy()
        addTextButton.destroy()
        backMenuPageButton.destroy()
        addFileText=Label(root, text="Input the file",bg='#0093b5')
        addFileText.pack()
        enterFile=Button(root, text="Add", command=openfilename, padx=24, bd=5)
        enterFile.pack()
        backMenuPageButton3= Button(root, text="Return", command=clickAddNew4, padx=24, bd=5)
        backMenuPageButton3.pack(pady=5)
        saveButton= Button(root, text="Save!", padx=20,command=saveNote, bd=5)
        saveButton.pack()

    addPicButton= Button(root, text="Add Pic", command=addPic, padx=20, bd=5, state=DISABLED)
    addFileButton= Button(root, text="Add File", padx=20,command=addFile, bd=5,state=DISABLED)
    title=Entry(root, width=50 )
    backMenuPageButton= Button(root, text="Return", command=menuPageWithCanvas, padx=24, bd=5)
    addTextButton= Button(root, text="Add Text", padx=20,command=addText, bd=5, state=DISABLED)
    textTitle.pack()

    def saveID():
        global id
        id = title.get()
        if (check_Id(id,1)):
            tkinter.messagebox.showerror(title="ERROR", message="ĐẶT LẠI ID ĐI BẠN ƠI")
        else:
            addPicButton["state"]="normal"
            addFileButton["state"]="normal"
            addTextButton["state"]="normal"

    checIDButton= Button(root, text="Check ID", padx=20,command=saveID, bd=5)
    title.pack( pady=5)
    # saveButton= Button(root, text="Save!", padx=20,command=saveNote, bd=5)
    # saveButton.pack() 
    checIDButton.pack()
    addPicButton.pack(pady=10)
    addFileButton.pack(pady=10)
    addTextButton.pack(pady=10)
    backMenuPageButton.pack(pady=10)

welcomepage()

root.mainloop()