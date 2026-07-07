from tkinter import *
window = Tk()

cookie_image = PhotoImage(file='assets/Cookie.png')
cookieLVL2_image = PhotoImage(file='assets/CookieLVL2.png')
cookieLVL3_image = PhotoImage(file='assets/CookieLVL3.png')
cookieLVL4_image = PhotoImage(file='assets/CookieLVL4.png')
cookieLVL5_image = PhotoImage(file='assets/CookieLVL5.png')

width = 800
height = 700
window.geometry(f"{width}x{height}")
window.title("Cookie Clicker")
window.iconphoto(True, cookie_image)
window.config(background="#D2691E")

f = open("variables/cookies.var")
cookies = int(f.read())
f.close()

#CookieClicks
f = open("variables/CookieClick.var")
CookieClick = int(f.read())
f.close()

f = open("variables/CookieClick_Price.var")
CookieClick_Price = int(f.read())
f.close()


f = open("variables/CookieClickLVL2_Price.var")
CookieClickLVL2_Price = int(f.read())
f.close()

f = open("variables/CookieClickLVL3_Price.var")
CookieClickLVL3_Price = int(f.read())
f.close()

f = open("variables/CookieClickLVL4_Price.var")
CookieClickLVL4_Price = int(f.read())
f.close()

f = open("variables/CookieClickLVL5_Price.var")
CookieClickLVL5_Price = int(f.read())
f.close()

def UpdateCookies():
    global cookies, f
    Cookies_text.config(text=f"Cookies: {cookies}")
    f = open("variables/cookies.var", "w")
    f.write(str(cookies))
    f.close()

    CookieClick_text.config(text=f"CookieClicks: {CookieClick}")
    f = open("variables/cookieclick.var", "w")
    f.write(str(CookieClick))
    f.close()

    CookieClick_Price_text.config(text=f"Price: {CookieClick_Price}")
    f = open("variables/CookieClick_Price.var", "w")
    f.write(str(CookieClick_Price))
    f.close()

    CookieClickLVL2_Price_text.config(text=f"Price: {CookieClickLVL2_Price}")
    f = open("variables/CookieClickLVL2_Price.var", "w")
    f.write(str(CookieClickLVL2_Price))
    f.close()

    CookieClickLVL3_Price_text.config(text=f"Price: {CookieClickLVL3_Price}")
    f = open("variables/CookieClickLVL3_Price.var", "w")
    f.write(str(CookieClickLVL3_Price))
    f.close()

    CookieClickLVL4_Price_text.config(text=f"Price: {CookieClickLVL4_Price}")
    f = open("variables/CookieClickLVL4_Price.var", "w")
    f.write(str(CookieClickLVL4_Price))
    f.close()

    CookieClickLVL5_Price_text.config(text=f"Price: {CookieClickLVL5_Price}")
    f = open("variables/CookieClickLVL5_Price.var", "w")
    f.write(str(CookieClickLVL5_Price))
    f.close()

def Click():
    global cookies, f, width

    f = open("variables/cookies.var")
    cookies = int(f.read())
    f.close()

    cookies += CookieClick
    UpdateCookies()

def Buy_Cookie_Upgrade():
    global cookies, CookieClick_Price
    if cookies > CookieClick_Price:
        global CookieClick, f
        cookies -= CookieClick_Price
        CookieClick_Price += 5
        CookieClick += 1
        UpdateCookies()

def Buy_CookieLVL2_Upgrade():
    global cookies, CookieClickLVL2_Price
    if cookies > CookieClickLVL2_Price:
        global CookieClick, f
        cookies -= CookieClickLVL2_Price
        CookieClickLVL2_Price += 25
        CookieClick += 5
        UpdateCookies()
        

def Buy_CookieLVL3_Upgrade():
    global cookies, CookieClickLVL3_Price
    if cookies > CookieClickLVL3_Price:
        global CookieClick, f
        cookies -= CookieClickLVL3_Price
        CookieClickLVL3_Price += 125
        CookieClick += 25
        UpdateCookies()

def Buy_CookieLVL4_Upgrade():
    global cookies, CookieClickLVL4_Price
    if cookies > CookieClickLVL4_Price:
        global CookieClick, f
        cookies -= CookieClickLVL4_Price
        CookieClickLVL4_Price += 125
        CookieClick += 125
        UpdateCookies()

def Buy_CookieLVL5_Upgrade():
    global cookies, CookieClickLVL5_Price
    if cookies > CookieClickLVL5_Price:
        global CookieClick, f
        cookies -= CookieClickLVL5_Price
        CookieClickLVL5_Price += 525
        CookieClick += 525
        UpdateCookies()


Cookies_text = Label(window, text=f"Cookies: {cookies}", font="Andalus, 20", border=0, bg="#D2691E", activebackground="#D2691E")
Cookies_text.pack(side=TOP)
cookie = Button(window, image=cookie_image, border=0, command=Click, bg="#D2691E", activebackground="#D2691E")
cookie.pack(side=BOTTOM)

CookieClick_text = Label(window, text=f"CookieClicks: {CookieClick}", font="Andalus, 10", border=0, bg="#D2691E")
CookieClick_text.pack(side=TOP)

Upgrade_Menu_Frame = Frame(window, bg="#D2691E", bd=5, relief=RAISED)
# Upgrade_Menu_Frame.place(x=500,y=0)
Upgrade_Menu_Frame.pack(side=RIGHT)
# Cookie Click
CookieClick_Frame = Frame(Upgrade_Menu_Frame, bg="#D2691E", bd=0)
CookieClick_Frame.pack()
# Title
CookieClick_Upgrade_title = Label(CookieClick_Frame, text="Upgrade Cookies", font=("Andalus, 10"), border=0, bg="#D2691E")
CookieClick_Upgrade_title.pack(side=TOP)
# Description
CookieClick_Upgrade_description = Label(CookieClick_Frame, text="Make Clicking Cookies Give +1 Cookie", font=("Andalus, 8"), border=0, bg="#D2691E")
CookieClick_Upgrade_description.pack(side=LEFT)
# Price
CookieClick_Price_text = Label(CookieClick_Frame, text=f"Price: {CookieClick_Price}", font="Andalus, 10", border=0, bg="#D2691E")
CookieClick_Price_text.pack(side=TOP)
# Button
CookieClick_Button = Button(CookieClick_Frame, image=cookie_image, border=0, command=Buy_Cookie_Upgrade, activebackground="#D2691E", bg="#D2691E")
CookieClick_Button.pack(side=LEFT)

# Cookie Click LVL2

CookieClickLVL2_Frame = Frame(Upgrade_Menu_Frame, bg="#D2691E", bd=0)
CookieClickLVL2_Frame.pack()
# Title
CookieClickLVL2_Upgrade_title = Label(CookieClickLVL2_Frame, text="Pea Cookies", font=("Andalus, 10"), border=0, bg="#D2691E")
CookieClickLVL2_Upgrade_title.pack(side=TOP)
# Description
CookieClickLVL2_Upgrade_description = Label(CookieClickLVL2_Frame, text="Make Clicking Cookies Give +5 Cookie", font=("Andalus, 8"), border=0, bg="#D2691E")
CookieClickLVL2_Upgrade_description.pack(side=LEFT)
# Price
CookieClickLVL2_Price_text = Label(CookieClickLVL2_Frame, text=f"Price: {CookieClickLVL2_Price}", font="Andalus, 10", border=0, bg="#D2691E")
CookieClickLVL2_Price_text.pack(side=TOP)
# Button
CookieClickLVL2_Button = Button(CookieClickLVL2_Frame, image=cookieLVL2_image, border=0, command=Buy_CookieLVL2_Upgrade, activebackground="#D2691E", bg="#D2691E")
CookieClickLVL2_Button.pack(side=LEFT)

# Cookie Click LVL3

CookieClickLVL3_Frame = Frame(Upgrade_Menu_Frame, bg="#D2691E", bd=0)
CookieClickLVL3_Frame.pack()
# Title
CookieClickLVL3_Upgrade_title = Label(CookieClickLVL3_Frame, text="Plant Cookies", font=("Andalus, 10"), border=0, bg="#D2691E")
CookieClickLVL3_Upgrade_title.pack(side=TOP)
# Description
CookieClickLVL3_Upgrade_description = Label(CookieClickLVL3_Frame, text="Make Clicking Cookies Give +25 Cookie", font=("Andalus, 8"), border=0, bg="#D2691E")
CookieClickLVL3_Upgrade_description.pack(side=LEFT)
# Price
CookieClickLVL3_Price_text = Label(CookieClickLVL3_Frame, text=f"Price: {CookieClickLVL3_Price}", font="Andalus, 10", border=0, bg="#D2691E")
CookieClickLVL3_Price_text.pack(side=TOP)
# Button
CookieClickLVL3_Button = Button(CookieClickLVL3_Frame, image=cookieLVL3_image, border=0, command=Buy_CookieLVL3_Upgrade, activebackground="#D2691E", bg="#D2691E")
CookieClickLVL3_Button.pack(side=LEFT)

# Cookie Click LVL4

CookieClickLVL4_Frame = Frame(Upgrade_Menu_Frame, bg="#D2691E", bd=0)
CookieClickLVL4_Frame.pack()
# Title
CookieClickLVL4_Upgrade_title = Label(CookieClickLVL4_Frame, text="Firey Cookies", font=("Andalus, 10"), border=0, bg="#D2691E")
CookieClickLVL4_Upgrade_title.pack(side=TOP)
# Description
CookieClickLVL4_Upgrade_description = Label(CookieClickLVL4_Frame, text="Make Clicking Cookies Give +125 Cookie", font=("Andalus, 8"), border=0, bg="#D2691E")
CookieClickLVL4_Upgrade_description.pack(side=LEFT)
# Price
CookieClickLVL4_Price_text = Label(CookieClickLVL4_Frame, text=f"Price: {CookieClickLVL4_Price}", font="Andalus, 10", border=0, bg="#D2691E")
CookieClickLVL4_Price_text.pack(side=TOP)
# Button
CookieClickLVL4_Button = Button(CookieClickLVL4_Frame, image=cookieLVL4_image, border=0, command=Buy_CookieLVL4_Upgrade, activebackground="#D2691E", bg="#D2691E")
CookieClickLVL4_Button.pack(side=LEFT)

# Cookie Click LVL5

CookieClickLVL5_Frame = Frame(Upgrade_Menu_Frame, bg="#D2691E", bd=0)
CookieClickLVL5_Frame.pack()
# Title
CookieClickLVL5_Upgrade_title = Label(CookieClickLVL5_Frame, text="Icey Cookies", font=("Andalus, 10"), border=0, bg="#D2691E")
CookieClickLVL5_Upgrade_title.pack(side=TOP)
# Description
CookieClickLVL5_Upgrade_description = Label(CookieClickLVL5_Frame, text="Make Clicking Cookies Give +525 Cookie", font=("Andalus, 8"), border=0, bg="#D2691E")
CookieClickLVL5_Upgrade_description.pack(side=LEFT)
# Price
CookieClickLVL5_Price_text = Label(CookieClickLVL5_Frame, text=f"Price: {CookieClickLVL5_Price}", font="Andalus, 10", border=0, bg="#D2691E")
CookieClickLVL5_Price_text.pack(side=TOP)
# Button
CookieClickLVL5_Button = Button(CookieClickLVL5_Frame, image=cookieLVL5_image, border=0, command=Buy_CookieLVL5_Upgrade, activebackground="#D2691E", bg="#D2691E")
CookieClickLVL5_Button.pack(side=LEFT)

window.mainloop()
