from tkinter import *
from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox
import os
a = Tk()


           
a.title("editor")
a.geometry("500x500+100+100")


mymenu =Menu()

new_icon_icons=PhotoImage(file="icons2/new.png")
open_icon_icons=PhotoImage(file="icons2/open.png")
save_icon_icons=PhotoImage(file="icons2/save.png")
save_as_icon_icons=PhotoImage(file="icons2/save_as.png")
exit_icon=PhotoImage(file="icons2/exit.png")



listone=Menu(tearoff=False)



copy_icon=PhotoImage(file="icons2/copy.png")
paste_icon=PhotoImage(file="icons2/paste.png")
cut_icon=PhotoImage(file="icons2/cut.png")
clear_all_icon=PhotoImage(file="icons2/clear_all.png")
find_icon=PhotoImage(file="icons2/find.png")

listtwo=Menu(tearoff=False)


tool_bar_icons=PhotoImage(file="icons2/tool_bar.png")
status_bar_icons=PhotoImage(file="icons2/status_bar.png")

listthree=Menu(tearoff=False)

light_default=PhotoImage(file="icons2/light_default.png")
light_plus=PhotoImage(file="icons2/light_plus.png")
dark=PhotoImage(file="icons2/dark.png")
red=PhotoImage(file="icons2/red.png")
monokai=PhotoImage(file="icons2/monokai.png")
night_blue=PhotoImage(file="icons2/night_blue.png")

listfour=Menu(tearoff=False)
listfour.add_command(label="light default",image=light_default,compound=LEFT)
listfour.add_command(label="light plus",image=light_plus,compound=LEFT)
listfour.add_command(label="dark",image=dark,compound=LEFT)
listfour.add_command(label="red",image=red,compound=LEFT)
listfour.add_command(label="monokai",image=monokai,compound=LEFT)
listfour.add_command(label="blue",image=night_blue,compound=LEFT)

color_theme=Menu(tearoff=False)

theme_choice=StringVar()
color_icons=(light_default,light_plus,dark,red,monokai,night_blue)

color_dict={
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}




mymenu.add_cascade(label="File",menu=listone)
mymenu.add_cascade(label="Edit",menu=listtwo)
mymenu.add_cascade(label="view",menu=listthree)
mymenu.add_cascade(label="color theme",menu=listfour)


tool_bar = ttk.Label(a)
tool_bar.pack(side=TOP,fill=X)

#font

font_tuple =font.families()
font_family = StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)

#size box

size_var=IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state="readonly")
font_size["values"]=tuple(range(8,81,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

#bold

bold_icon=PhotoImage(file="icons2/bold.png")
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

#italic

italic_icon=PhotoImage(file="icons2/italic.png")
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

#underline

underline_icon=PhotoImage(file="icons2/underline.png")
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)


#font color

font_color_icon=PhotoImage(file="icons2/font_color.png")
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

#align left


align_left_icon=PhotoImage(file="icons2/align_left.png")
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

#align right


align_right_icon=PhotoImage(file="icons2/align_right.png")
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=7,padx=5)


#align center


align_center_icon=PhotoImage(file="icons2/align_center.png")
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=8,padx=5)

#text editor

text_editor=Text(a)
text_editor.config(wrap="word",relief=FLAT)

#scroll bar

scroll_bar=Scrollbar(a)
text_editor.focus_set()
scroll_bar.pack(side=RIGHT,fill=Y)
text_editor.pack(fill=BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#status bar

status_bar=Label(a)
status_bar.pack(side=BOTTOM)

#font
current_font_family = 'Arial'
current_font_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)


#bold button function

def change_bold():
    text_property=font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
bold_btn.configure(command=change_bold)


# italic functionlaity
def change_italic():
    text_property=font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
italic_btn.configure(command=change_italic)

# underline functionality 
def change_underline():
    text_property=font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
underline_btn.configure(command=change_underline)


## font color functionality 
def change_font_color():
    color_var=colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)

### align functionality 

def align_left():
    text_content=text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=LEFT)
    text_editor.delete(1.0,END)
    text_editor.insert(INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

## center 
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=CENTER)
    text_editor.delete(1.0,END)
    text_editor.insert(INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

## right 
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=RIGHT)
    text_editor.delete(1.0,END)
    text_editor.insert(INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)


text_editor.configure(font=('Arial', 12))


#status bar

status_bar=Label(a)
status_bar.pack(side=BOTTOM)

text_changed=False 
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True 
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f"Characters : {characters} Words : {words}")
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)

## variable 
url = ''

## new functionality
def new_file(event=None):
    global url 
    url = ''
    text_editor.delete(1.0,END)

## file commands
listone.add_command(label="New file",image=new_icon_icons,compound=LEFT,accelerator="Ctrl+N")
 
## open functionality

def open_file(event=None):
    global url 
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0,END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
       return
    except:
       return
a.title(os.path.basename(url)) 

listone.add_command(label='Open', image=open_icon_icons, compound=LEFT, accelerator='Ctrl+O', command=open_file)

## save file 

def save_file(event=None):
    global url 
    try:
        if url:
            content = str(text_editor.get(1.0,END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0,END)
            url.write(content2)
            url.close()
    except:
        return 

listone.add_command(label="Save file",image=save_icon_icons,compound=LEFT,accelerator="Ctrl+s")


## save as functionality 
def save_as(event=None):
    global url 
    try:
        content = text_editor.get(1.0,END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return 
listone.add_command(label='Save As', image=new_icon_icons, compound=LEFT, accelerator='Ctrl+Alt+S', command=save_as)

## exit functionality 

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        a.destroy()
                else:
                    content2 = str(text_editor.get(1.0,END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    a.destroy()
            elif mbox is False:
                a.destroy()
        else:
           a.destroy()
    except:
        return 
listone.add_command(label='Exit', image=exit_icon, compound=LEFT, accelerator='Ctrl+Q', command=exit_func)


############ find functionality

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0',END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0,END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0,END)
        text_editor.insert(1.0,new_content)

    find_dialogue =Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

## edit commands 
listtwo.add_command(label='Copy', image=copy_icon, compound=LEFT, accelerator='Ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
listtwo.add_command(label='Paste', image=paste_icon, compound=LEFT, accelerator='Ctrl+V', command=lambda:text_editor.event_generate("<Control v>"))
listtwo.add_command(label='Cut', image=cut_icon, compound=LEFT, accelerator='Ctrl+X', command=lambda:text_editor.event_generate("<Control x>"))
listtwo.add_command(label='Clear All', image=clear_all_icon, compound=LEFT, accelerator='Ctrl+Alt+X', command= lambda:text_editor.delete(1.0, tk.END))
listtwo.add_command(label='Find', image=find_icon, compound=LEFT, accelerator='Ctrl+F', command = find_func)

## view check button 

show_statusbar =BooleanVar()
show_statusbar.set(True)
show_toolbar =BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False 
    else :
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=TOP, fill=X)
        text_editor.pack(fill=BOTH, expand=True)
        status_bar.pack(side=BOTTOM)
        show_toolbar = True 


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False 
    else :
        status_bar.pack(side=BOTTOM)
        show_statusbar = True 
listthree.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0,variable = show_toolbar, image=tool_bar_icons, compound=LEFT, command=hide_toolbar)
listthree.add_checkbutton(label='Status Bar',onvalue=1, offvalue=False,variable = show_statusbar, image=status_bar_icons, compound=LEFT, command=hide_statusbar)


def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color) 
count = 0 
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=LEFT, command=change_theme)
    count += 1 




a.bind("<Control-n>", new_file)
a.bind("<Control-o>", open_file)
a.bind("<Control-s>", save_file)
a.bind("<Control-Alt-s>", save_as)
a.bind("<Control-q>", exit_func)
a.bind("<Control-f>", find_func)




a.config(menu=mymenu)
a.mainloop()














