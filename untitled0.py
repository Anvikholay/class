from tkinter import*
root=Tk()
root.geometry("900x600")
root.title("Classes")

class CreateElements:
    
    def __init__(self):
        print("This is CreateElements class")
        
        def createNewElement(self):
            label = Label(root,text="A new label has been created using class",fg="red") 
            label.pack()
            btn=Button(root,text ="Button",command = self.message)
            btn.pack(padx=20,pady=10)
            
            def message(self):
                messagebox.showinfo("showinfo","you clicked the button using class")
                
                
                obj_of_CreateElements = CreateElements()
                
                btn = Button(root,text="click to create label and button element",command =
                             obj_of_CreateElements.createNewElement)
                btn.pack(padx=20,pady=10)
                
                root.mainloop()