from tkinter import font
f_size = 15
f_weight = "normal"
f_familly = "Arial"
colors = [["black","white"],["blue","white"],["white","black"],["#FADCD9","black"],["#d4cebd","black"]]
def theme(index,root,text):
    # root.config(bg=colors[index][0])
    text.config(background=colors[index][0],foreground=colors[index][1])
    
    
def font_family(family, text):
    f_familly = family
    text.config(font=(family, f_size, f_weight))

def font_size(size, text):
    f_size = size
    text.config(font=(f_familly, size, f_weight))

def font_weight(weight,text):
    f_weight = weight
    # text.config(font=(f_familly, f_size, weight))
    text.tag_configure(weight,font=(f_familly, f_size, weight))
    current_tags = text.tag_names("sel.first")

    if weight in current_tags:
        text.tag_remove(weight,"sel.first","sel.last")
    else:
        text.tag_add(weight,"sel.first","sel.last")
