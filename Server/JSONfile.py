'''Vui lòng đọc kĩ hướng dẫn sử dụng trước khi dùng hàm trong đây <(")
Nếu bạn quá vjp pro đến mức đọc code cũng hiểu thì không cần :>
hướng dẫn sử dụng t gửi kế bên á :>
'''
import json
import os 

def login_check(usr,pwd): # hàm kiểm tra đăng nhập
  with open("account_database.json", "r") as fin: 
    data = json.load(fin)
  for x in data:
    if usr == x["username"] and pwd == x["password"]:
      return True
  return False

def save_new_account(usr,pwd): #hàm lưu tk mới 
  new_account = {
  "username" : usr,
  "password" : pwd
  }
  with open("account_database.json", "r") as fin: 
    data = json.load(fin)
  data.append(new_account)
  with open("account_database.json", "w") as fout:
    json.dump(data, fout)
  user_database = f"userDatabase/" + usr + ".json"
  file_format = []
  with open(user_database, "w") as fout: #tạo file lưu ghi chú cho tài khoản 
    json.dump(file_format, fout)
  folder_path = './userDatabase/' + usr 
  os.mkdir(folder_path)

def save_new_note(username,id,type,content): #hàm lưu note mới 
  file_name =  f"userDatabase/" +  username + ".json"
  with open(file_name, "r") as fin:
    data = json.load(fin)
  new_note = {
  "ID" : id,
  "type" : type,
  "content" : content
  }
  data.append(new_note)
  with open(file_name, "w") as fout:
    json.dump(data, fout)

def read_note(username,id): #hàm trả về content của node cụ thể với id nhập vào 
  file_name = f"userDatabase/" + username + ".json"
  with open(file_name, "r") as fin: 
    data = json.load(fin)
  for x in data:
    if id == x["ID"]:
      content = x["content"]
      type = x["type"]
  return type, content
  
def username_check(usr): #hàm check username 
  with open("account_database.json", "r") as fin: 
    data = json.load(fin)
  for x in data:
    if usr == x["username"]:
      return True #có bị trùng thì trả về true
  return False

#cập nhật 03/07/2022: thêm hàm check trùng id, thêm hàm trả về kiểu dict có dạng { "ID" : "type" }

def id_check(username,id): #hàm check_id 
  file_name = f"userDatabase/" + username + ".json"
  with open(file_name, "r") as fin: 
    data = json.load(fin)
  for x in data:
    if id == x["ID"]:
      return True #có bị trùng thì trả về true
  return False

def view_note(username):# hàm trả về kiểu dict 
  file_name = f"userDatabase/" + username + ".json"
  with open(file_name, "r") as fin: 
    data = json.load(fin)
  note_dict = {}
  for x in data:
    note_dict[x["ID"]] = x["type"]
  return note_dict #cái nà



