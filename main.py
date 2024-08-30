import os
import stat
import re
import tkinter as tk
from tkinter import filedialog
import send2trash
def delete_file(folder_path):
    pattern = re.compile(r'.*\(\d\).*')
    filelist=os.listdir(folder_path)
    matchfilelist=[]
    #找出匹配的文件名
    for file in filelist:
        if re.match(pattern,file):
            matchfilelist.append(folder_path+"/"+file)
    #权限检查，移除只读属性
    for file in matchfilelist:
        try:
            os.chmod(file, stat.S_IWRITE)
            send2trash.send2trash(os.path.normpath(file))#将匹配的文件放入回收站
            print(f"成功删除了文件: {file}")
        except Exception as e:
            print(f"删除文件时出现错误: {file}，错误信息: {e}")

def recursive_delete_file(directory):
    for root, dirs, files in os.walk(directory):
        delete_file(root)

def main():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    print("是否采取递归删除？(y/n),递归操作相当危险，请谨慎选择")
    flag=input()
    file_path = filedialog.askdirectory() # 打开文件选择对话框
    if flag=="y" or flag=='Y':
        recursive_delete_file(file_path)
    else:
        delete_file(file_path)
    root.destroy()
    input("按回车键退出")
if __name__=='__main__':
    main()
