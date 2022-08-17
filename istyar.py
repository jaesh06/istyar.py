from datetime import date
import tkinter as tk
import htmlclipboard

#Example of OOP of this: https://www.pythontutorial.net/tkinter/tkinter-stringvar/

text0 = "Author's name (F. Lastname):"
text1 = "Article Title:"
text2 = "Website Title:"
text3 = "Publish Date (Mmm. dd, yyyy):"
text4 = "URL:"

text_list = [text0, text1, text2, text3, text4]

var_names = {}

window = tk.Tk()
window.title("Istyar the Cited")
window.columnconfigure(0, weight=1, minsize=100)
for f in range(6):
    window.rowconfigure(f, weight=1, minsize=75)

for f in text_list:
    frame_key = "frame_" + str(text_list.index(f))
    frame_value = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5, bg="#809599")
    var_names[frame_key] = frame_value
    var_names[frame_key].grid(column=0, row=text_list.index(f))
    label_key = "label_" + str(text_list.index(f))
    label_value = tk.Label(master=var_names[frame_key], text=f, bg="#809599", font=('Calibri', 14, 'bold'))
    var_names[label_key] = label_value
    var_names[label_key].pack()
    entry_key = "entry_" + str(text_list.index(f))
    entry_value = tk.Entry(master=var_names[frame_key], width=75)
    var_names[entry_key] = entry_value
    var_names[entry_key].pack(fill=tk.X)

# a = var_names["entry_0"].insert(0, "T. Test")
# t = var_names["entry_1"].insert(0, "Article Title")
# wt = var_names["entry_2"].insert(0, "Website Title")
# pd = var_names["entry_3"].insert(0, "Mar. 16, 2022")
# l = var_names["entry_4"].insert(0, "https://example.com")

frame_6 = tk.Frame(master=window, pady=10)
frame_6.grid(column=0, row=5)

button1 = tk.Button(master=frame_6, text="Cite!")
button1.pack()
error_label = tk.Label(master=frame_6, text="", pady=5)
error_label.pack()

def cite(event):
    a = var_names["entry_0"].get()
    t = var_names["entry_1"].get()
    wt = var_names["entry_2"].get()
    pd = var_names["entry_3"].get()
    l = var_names["entry_4"].get()
    
    td = date.today()
    tdfmt = td.strftime("%b. %d, %Y")

#     #tag_to_html = {
#     ('tagon', 'italics'): '<i>',
#     ('tagoff', 'italics'): '</i>',
# }

    for v in [a, t, wt, pd, l]:
        if v == "":
            error_label.config(text="Please fill out all fields!", fg="red")
            return
    
    citation_1half = a + ", "
    citation_ital = "<i>" + t + "</i>"
    citation_2half = ", " + wt + ", " + pd + ". Accessed on: " + tdfmt + ". [Online]. Available: " + l
    citation_full = citation_1half + citation_ital + citation_2half
    
    # r_window = tk.Tk()
    # r_window.columnconfigure(0, weight=1, minsize=10)
    # r_frame = tk.Frame(master=r_window, padx=10, pady=10)
    # r_frame.grid(column=0, row=0)

    # r_text = tk.Text(master=r_frame, font="Calibri 11")
    # r_text.tag_config("italics", font="Calibri 11 italic")
    # r_text.insert(tk.END, citation_1half)
    # r_text.insert(tk.END, citation_ital, "italics")
    # r_text.insert(tk.END, citation_2half)
    # r_text.config(state=tk.DISABLED, height=5, width=75)
    # r_text.grid(column=0, row=0)
    # content = r_text.dump("1.0", tk.END, tag=True, text=True)
    # html_text = []
    # for key, value, index in content:
    #     if key == "text":
    #         html_text.append(value)
    #     else:
    #         html_text.append(tag_to_html.get((key, value), ''))
    # print(''.join(html_text))
    htmlclipboard.PutHtml(citation_full)
    error_label.config(text="Copied to clipboard!", fg="green")
    #https://code.activestate.com/recipes/474121-getting-html-from-the-windows-clipboard/ - GODSEND
    #https://gist.github.com/Erreinion/6691093/revisions - Actual revision used

    #r_window.mainloop()
button1.bind("<Button-1>", cite)

window.mainloop()