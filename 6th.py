import os
# # print(os.getcwd())
# # # print(os.listdir(r"C:\Users\PHED\Desktop\pythonprojects"))
# os.chdir(r"C:\Users\PHED\Desktop\pythonprojects\hehe.py")
# # print(os.getcwd())

# # open('test.txt','x')

# file= open('test.txt','a')
# # data="hello baccho"
# # file.write(data)
# # file.write("\n pagal baccho")

# # read=file.read()
# # file.close()
# # print(read)
# data="You zanuj"
#file.write(data)





def new(path,name):

    os.chdir(path)
    open(name,'x')

def writes(path,file,text):
    os.chdir(path)
    file=open(file,'w')
    
    file.write(text)

# new(r"C:\Users\PHED\Desktop\pythonprojects\hehe.py",'try.txt')

# writetext=print(input("write="))
file=print(input("write file to create="))
writes(r"C:\Users\PHED\Desktop\pythonprojects\hehe.py","try.txt","chahcahchaha")

# r"C:\Users\PHED\Desktop\pythonprojects\hehe.py"

#jecrc --> image, pdf, text file,audio --->image_folder , pdf_folder, text_folder,audio_folder