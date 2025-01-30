import tkinter as tk
from tkinter import filedialog, messagebox



file_name = "Untitled"

win = tk.Tk()
win.title(f'Text Editor - {file_name}')
win.minsize(width=400, height=400)
win.geometry('600x400')



def new_file():
    file_path = filedialog.asksaveasfilename(
        title='Create New File',
        defaultextension='.txt',
        filetypes=[('Text File', '*.txt'),('All Files','*.*')]
    )
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(txt.get("1.0", tk.END))
                messagebox.showinfo("Secess", "File saved")
                win.title(f'Text Editor - {file_path}')

        except Exception  as e:
            messagebox.showwarning("error", f"Not Found{e}")


def open_file():
    file_path = filedialog.askopenfilename(
        title='Open File',
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")] 
    )

    if file_path:
        try:
            with open(file_path, "r") as f:
                content = f.read()
               
                txt.delete("1.0", tk.END)
                txt.insert(tk.END, content)
                win.title(f"Text Editor - {file_path}")
                messagebox.showinfo('Secess', 'Opened')
        except Exception as e:
            messagebox.showwarning("Error", f"Field{e}")




mnu = tk.Frame(win, bg="#556644", height=40)
mnu.pack(side=tk.TOP, fill=tk.X)

text_area = tk.Frame(win, bg="#f5f5f5")
text_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


var = tk.StringVar()

txt = tk.Text(text_area, borderwidth=0 ,  wrap=tk.WORD, font=("Arial", 14), fg='darkorange')
txt.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,pady=10,padx=5)




img_nw = tk.PhotoImage(file='new-file.png')
nw_s = img_nw.subsample(8,8)

img_op = tk.PhotoImage(file='open-file.png')
op_s = img_op.subsample(16,16)

img_sve = tk.PhotoImage(file='save-file.png')
sve_s = img_sve.subsample(18,18)

img_sveas = tk.PhotoImage(file='save-as.png')
sveas_s = img_sveas.subsample(11,11)


img_cp = tk.PhotoImage(file='copy.png')
cp_s = img_cp.subsample(8,8)

img_ct = tk.PhotoImage(file='cut.png')
ct_s = img_ct.subsample(16,16)

img_pt = tk.PhotoImage(file='past.png')
pt_s = img_pt.subsample(16,16)

img_un = tk.PhotoImage(file='undo.png')
un_s = img_un.subsample(4,4)

img_rd = tk.PhotoImage(file='redo.png')
rd_s = img_rd.subsample(8,8)



nw = tk.Button(mnu, image=nw_s, bg='#556644',borderwidth=0,activebackground='#556644', command=new_file).pack(side=tk.LEFT, padx=10)

op = tk.Button(mnu, image=op_s, bg='#556644',borderwidth=0,activebackground='#556644', command=open_file).pack(side=tk.LEFT, padx=0)

sve = tk.Button(mnu, image=sve_s, bg='#556644',borderwidth=0,activebackground='#556644').pack(side=tk.LEFT, padx=4)

sveas = tk.Button(mnu, image=sveas_s, bg='#556644',borderwidth=0,activebackground='#556644').pack(side=tk.LEFT, padx=0)



cp = tk.Button(mnu, image=cp_s, bg='#556644',borderwidth=0,activebackground='#556644').pack(side=tk.LEFT, padx=0)

ct = tk.Button(mnu, image=ct_s, bg='#556644',borderwidth=0,activebackground='#556644').pack(side=tk.LEFT, padx=5)

pt = tk.Button(mnu, image=pt_s, bg='#556644', borderwidth=0,activebackground='#556644').pack(side=tk.LEFT, padx=0)

un = tk.Button(mnu, image=un_s, bg='#556644',  borderwidth=0,activebackground='#556644').pack(side=tk.LEFT, padx=0)

rd = tk.Button(mnu, image=rd_s, bg='#556644',  borderwidth=0,activebackground='#556644').pack(side=tk.LEFT, padx=0)





win.mainloop()