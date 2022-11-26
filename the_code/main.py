import tkinter as tk

def replace():
    #ตรวจข้อความ
    cheaktext = str(entry_in.get())
    cheakintext = cheaktext.isdigit()
    if cheakintext is False:
        return entry_out.configure(text="error")

    #เรื่มทำงาน
    intext = int(entry_in.get())
    outtext = []
    decimal = intext

    while decimal > 0:
        outtext.append(str(decimal % 2))
        decimal = int(decimal / 2)

    outtext.reverse()

    entry_out.configure(text=outtext)

window = tk.Tk()
window.title('ฐาน2 Converter')
window.minsize(width=500, height=300)
#ตัวui
label = tk.Label(master=window, text="Enter number:")
entry_in = tk.Entry(master=window)
button = tk.Button(master=window, text="Convert", width=20, comman=replace)
label2 = tk.Label(master=window, text="Converted number:")
entry_out = tk.Label(master=window, text="")
#แพคui
label.pack()
entry_in.pack()
button.pack(pady=2)
label2.pack()
entry_out.pack(pady=2)

window.mainloop()
