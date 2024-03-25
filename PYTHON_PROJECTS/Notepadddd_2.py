#matter  of fact we caN make any application which we have used 

import tkinter as tk
from tkinter import filedialog # Filedialog is inbuilt module funtion as it mean its built in fucntion . 

class Notepad():
    def __init__(self,root):#consturctor is used to call all the code run what ever is saved in it . 
        self.file_path = False # it works as it will 
        self.root= root #selfrefer to the current object. 
        root.title('Notepad' )
        root.geometry('1200x600')

        heading = tk.Label(text='Notepad',font=('Harlow Solid Italic',40))

        heading.grid(row=1,column=1,columnspan=2,pady=25)


        open_btn = tk.Button(text='Open',font=('Harlow Solid Italic',30),relief='solid',
                    bg='#7fffcc',fg='white',width=7,command=self.file_open)
        save_btn = tk.Button(text='Save',font=('Harlow Solid Italic',30),relief='solid',
                    bg='#8b0a50',fg='white',width=7,command=self.save)
        save_as_btn = tk.Button(text='Save As',font=('Harlow Solid Italic',30),relief='solid',
                    bg='#79aa45',fg='white',width=7,command=self.save_as)
        clear_btn = tk.Button(text='Clear',font=('Harlow Solid Italic',30),relief='solid',
                    bg='#7645aa',fg='white',width=7,command=self.clear)
        help_btn = tk.Button(text='Help',font=('Harlow Solid Italic',30),relief='solid',
                    bg='#3333ff',fg='white',width=7,command=self.help) 
                    
        self.textarea = tk.Text(font=('Ariel',18),height=20,relief="solid")

        self.textarea.grid(row=2,column=2,rowspan=5)
        # we wrote this here as we are about to use the text area in 

        # to merge the rows  we use this part call rowspan 


        open_btn.grid(row=2,column=1,pady=5,padx=15)
        save_btn.grid(row=3,column=1,pady=5,padx=15)
        save_as_btn.grid(row=4,column=1,pady=5,padx=15)
        clear_btn.grid(row=5,column=1,pady=5,padx=15)
        help_btn.grid(row=6,column=1,pady=5,padx=15)

    def save(self):
        if self.file_path:
            text = self.textarea.get(0.0,tk.END) 
            with open(self.file_path,'w') as my_file:
                my_file.write(text)
        
        else:
            self.save_as()

    # to saveas file function 
    def save_as(self):
        file_option = [('Text File','*.txt'),('Bat File','*.bat'),
                       ('Python File','*.py'),('All File','*.*')]
        path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=file_option)
        text = self.textarea.get(0.0,tk.END)  
        with open(path,'w') as my_file:
            my_file.write(text)

    



    def file_open(self): #( with the use of file hndling method. )
        self.file_path= filedialog.askopenfilename() # if any file is open it will show its path 
        #with open(file_path,'r') as my_file:
        my_file = open(self.file_path,'r')
        text = my_file.read()
        my_file.close()
        self.clear()
        self.textarea.insert(0.0,text)
        self.root.title(f'Notepad : {self.file_path}')


    def clear(self): # 
        self.textarea.delete(0.0,tk.END) # it wont work as we neeed to call the thing in the button as command as this method aling under the classs. 

    def help(self): # its a object as t should be called using self as its is wokring undeer class (). 
        help_text= ''' 
        
        Notepad is a basic text editor that is included with Windows.
        It is a simple program that can be used to create and 
        edit text files. Notepad is not a word processor, so it does not have
        many of the features that are found in word processors, such as the 
        ability to create and edit tables, images, or charts. 
        However, Notepad is a great tool for creating simple text files, 
        such as program code, scripts, or notes.

        To use Notepad, simply open the program and start typing.
        You can use the keyboard to type in text, and you can use 
        the mouse to select text and perform other actions.
        Notepad does not have a lot of menus or buttons, so it is very 
        easy to learn how to use.

        When you are finished editing a text file, you can save it by clicking
        on the "File" menu and selecting "Save." You will be prompted to enter a
        filename and location for the file. Notepad will save the file as a 
        plain text file with a .txt extension.

        Here are some of the things you can do with Notepad:

        Create and edit text files
        Save text files in a variety of formats
        Search for text within a text file
        Replace text within a text file
        Use keyboard shortcuts to perform common tasks
        Print text files
        Notepad is a very versatile tool that can be used for a variety of tasks.
        It is a great tool for beginners and experienced 
        users alike.

        Here are some additional tips for using Notepad:

            # o select a block of text, hold down the left mouse button and
            drag the mouse over the text you want to select.
            # To copy selected text, press the "Ctrl" key and
            the "C" key at the same time.
            # To paste copied text, press the "Ctrl" key and
            the "V" key at the same time.
            # To search for text within a text file, click on the "Edit" menu
            and select "Find." Enter the text you want to search for and 
            # click on the "Find Next" button.
            # To replace text within a text file, click on the "Edit" menu and
            select "Replace." Enter the text you want to replace and the 
            # text you want to replace it with. Click on the "Replace" button
            to replace the first occurrence of the text, or click on the 
            # "Replace All" button to replace all occurrences of the text.
            # To use keyboard shortcuts to perform common tasks, click on the 
            "Help" menu and select "Keyboard shortcuts."
         '''

        self.clear()
        self.textarea.grid(0.0,help_text)


#help will appear as the guide and will guide you through. 
        

window =tk.Tk()

note = Notepad(window)

# consturctor ususally get called when object is called 


window.mainloop()
