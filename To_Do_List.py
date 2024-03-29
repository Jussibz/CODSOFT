from tkinter import *


class Todo:
    def __init__(self, root):
            self.root = root
            self.root.title("To-do-list")
            self.root.geometry('650x410+300+150')
    
    
            self.label = Label(self.root, text='To-Do-List-App',
                                font=('arial', 25, 'bold'), width=10, bd=5, bg='orange', fg='black')
            self.label.pack(side='top', fill=BOTH)
    
            self.label2 = Label(self.root, text='Add Task',
                                font=('arial',18, 'bold'), width=10, bd=5, bg='orange', fg='black')
            self.label2.place(x=40, y=54)
    
            self.label3 = Label(self.root, text='Task',
                                font=('arial', 25, 'bold'), width=10, bd=5, bg='orange', fg='black')
            self.label3.place(x=320, y=54)
    
            self.main_text = Listbox(self.root, height=9, bd=5, width=23, font = ("ariel", 20, "italic", "bold"))
            self.main_text.place(x=280, y=100)
    
            self.text=Text(self.root, bd=5, height=2, width=30, font='areil, 10 bold')
            self.text.place(x=20, y=120)
        
        
            self.button = Button (self.root, text="Add", font=('serif', 20, 'bold', 'italic') , width=10, fg='black', command=self.add ) 
            self.button.place(x=30, y=180)
    
            self.button2 = Button (self.root, text="Delete", font=('serif', 20, 'bold', 'italic') , width=10, fg='black', command=self.delete) 
            self.button2.place(x=30, y=280)
    
    
    #==================Add Task===============#
    
    
    def add(self):
        content = self.text.get(1.0, END)
        if content.strip():
            self.main_text.insert(END, content)
            with open ('data.text', 'a') as file:
                file.write(content)
            self.text.delete(1.0, END)
        
        
    def delete(self):
        delete_index = self.main_text.curselection()
        if  delete_index:
            task = self.main_text.delete(delete_index)
            self.main_text.delete(delete_index)
            with open('data.text', 'w') as f:
                 lines =f.readlines
            with open ('data.txt' , 'w') as f:
                for line in lines:
                    if line.strip() != task.strip():
                        f.write(line)
           
            
            
            
def main():
        root = Tk()
        app = Todo(root)
        root.mainloop()
    
if __name__ == "__main__":
        main()
        
        
  
                
                
   
     
                        
    
    
    
    
    
    
    
    
    
    
    
    
    