import math
from tkinter import *

#ranged and melee definitions
#final statments need to be reformatted and combined into 1 message box!!!!
#ask yes no boxes and the rest of the boxes and widgets need a title!!!!!
#the if input statments need to have their own widgets :/(basically impossible w/o redoing the entire program)!!!!
#^^^^^ check the widgets section belw for mroe notes!!!
#after everything gets a title and the sizes are changed and the message boxes are combined there is no code left to write!!!
#then after that!! EVERY "" must be revewed by trevor and made to be very readable for the user and easy on the eyes!!!
#   maybe add some instructions to the statments!!!
#   finaly add a credits statment at the end of the program for trevor arthur steven and anthony OR some where in the program!!!
def melee(elm1,elm2,elm3):
    #input statments case sensative!!!!
    bab=            int(elm1)#(input("what is your bab: " ))
    baseStrength=   int(elm2)#input("what is your strength: "))
    weaponType =    int(elm3)#input("is this a one handed weapon or two? (1,2): "))
    askAttack=      messagebox.askyesno(message="do you want power attack?")
    mWK=            messagebox.askyesno(message="is weapon mwk? yes or no?")
    weaponFocus=    messagebox.askyesno(message="do you have weapon focus?")
    enhancment=     messagebox.askyesno(message="is your weapon enhanced?")
    if enhancment == 1:#needs to be so user can access it needs its own widget
        enhancmentNUM = int(input("what is the enhancment bonus on your weapon? 0-5: "))
    #some rando calcs
    strengthModifier=(baseStrength-10)/2#round here
    dmg=strengthModifier
    babM = bab+strengthModifier
    #dmg yes power attack

    if askAttack == 1:#if power attack is yes then based on 1 handed or 2 handed
        if weaponType == 2:#2hpa
            fdmg=math.floor(strengthModifier+(math.floor(((bab//4)+1))*2)*1.5)#round here bab/4+1 needs to be rounded
            babM=math.floor(babM-(math.floor(((bab/4)+1.1), 0)))
        elif weaponType == 1:#1hpa
            fdmg= math.floor(strengthModifier+(math.floor(((bab//4)+1))*2))
            babM=math.floor(babM-(math.floor(((bab/4)+1.1))))
    #dmg no power attack           
    elif askAttack == 0: #if power attack = no
        if weaponType == 2:#2hnpa
            fdmg=math.floor(1.5*dmg) #round down
            babM=math.floor(babM+.1)
        elif weaponType == 1:#1hnpa
            fdmg=math.floor(dmg)#round down
            babM=math.floor(babM+.1)
    #mWK?
    if mWK == 1 and enhancment == 0:
        babM=babM+1
    if enhancment == 1:
        fdmg=fdmg+enhancmentNUM
        babM=babM+enhancmentNUM
    if weaponFocus == 1:
        babM=babM+1
    #bonus attacks for special variables
    bonusAttack=0
    babMMa1=0
    babMMa2=0
    babMMa3=0
    #bonus attacks calculated
    if bab >=6:
        babMMa1=babM-5
        bonusAttack=bonusAttack+1
    if bab >=11:
        babMMa1=babM-5
        babMMa2=babMMa1-5
        bonusAttack=bonusAttack+1
    if bab >=16:
        babMMa1=babM-5
        babMMa2=babMMa1-5
        babMMa3=babMMa2-5
        bonusAttack=bonusAttack+1
    #print statments
    #message box statmentsl. need to be redone so 4 seprate instances of message boxes isntead of 4 boxes
    statment1="%f is your dmg %f is your chance to hit"%(fdmg,babM)
    messagebox.showinfo(title="final dmg and chance",message = statment1)
    if bab>=6:
        statment2="the first bonus attack has a chance to hit of %f "%babMMa1
        messagebox.showinfo(title="first bonus attack",message = statment2)
        if bab>=11:
            statment3="the second bonus attack has a chance to hit of %f "%babMMa2
            messagebox.showinfo(title="second bonus attack",message = statment3)
            if bab >=16:
                statment4="the third bonus attack has a chance to hit of %f "%babMMa3
                messagebox.showinfo(title="third bonus attack",message = statment4)

def ranged(elm1,elm2,elm3):
    #input statments
    bab=            int(elm1)#int(input("what is your bab?: " ))
    baseDex=        int(elm2)#int(input("what is your Dexterity?: "))
    baseStrength=   int(elm3)#int(input("what is your strength: "))
    askBow=         messagebox.askyesno(message="do you have a strength bow?")
    rapidS=         messagebox.askyesno(message="do you want rapid shot?")
    askManyShot=    messagebox.askyesno(message="do your want many shot?")
    askPower=       messagebox.askyesno(message="do you want deadly aim?")
    mWK=            messagebox.askyesno(message="is weapon mwk? yes or no?")
    weaponFocus=    messagebox.askyesno(message="do you have weapon focus? yes or no?")
    enhancment=     messagebox.askyesno(message="is your weapon enhanced?")
    #if statments based on input statments
    penalty=0
    bowStrength= 0
    strengthModifier=math.floor((baseStrength-10)/2)\
    #need to find away to make these into message boxes or widgets
    if askBow == 1:
        bowStrength =   int(input("what is your bow strength: "))
    if bowStrength>strengthModifier:
        penalty=bowStrength-strengthModifier
    if enhancment == 1:
        enhancmentNUM = int(input("what is the enhancment bonus on your weapon? 0-5: "))
    #some rando calcs
    dmg=strengthModifier
    babM = bab+strengthModifier

    #dmg yes power attack

    if askPower == 1:#if power attack is yes then based on 1 handed or 2 handed
        fdmg= (math.floor(((bab//4)+1))*2)
        babM=math.floor(babM-(math.floor(((bab/4)+1.1))))
    #dmg no power attack           
    elif askPower == 0: #if power attack = no
        fdmg=0#round down
        babM=math.floor(babM+.1)

    #composite bow
    if askBow == 1:
        fdmg=fdmg+bowStrength
        
    #mWK?
    if mWK == 1 and enhancment == 0:
        babM=babM+1
    if enhancment == 1:
        fdmg=fdmg+enhancmentNUM
        babM=babM+enhancmentNUM
    if weaponFocus == 1:
        babM=babM+1
    #bonus attacks
    #special variables
    bonusAttack=0
    babMMa1=0
    babMMa2=0
    babMMa3=0
    #for rapid shots and penalty 
    if penalty>0:
        babM=babM-2
    if rapidS == 1:
        bonusAttack=bonusAttack+1
        babMMr=babM-2
    #bonus attacks
    if bab >=6:
        babMMa1=babM-5
        bonusAttack=bonusAttack+1
    if bab >=11:
        babMMa1=babM-5
        babMMa2=babMMa1-5
        bonusAttack=bonusAttack+1
    if bab >=16:
        babMMa1=babM-5
        babMMa2=babMMa1-5
        babMMa3=babMMa2-5
        bonusAttack=bonusAttack+1
    #many shot
    fdmg1=fdmg
    if askManyShot == 1:
        fdmg1=fdmg*2
    #print statments
    #messagebox statments need to be 1 big message box not 4 statments!!!
    statment1="%f is your dmg %f is your chance to hit."%(fdmg1,babM)
    messagebox.showinfo(title="final dmg and chance",message = statment1)
    if rapidS == 1:
        statmentR="%f is your dmg for your rapid shot attack and %f is your chance to hit"%(fdmg,babMMr)
        messagebox.showinfo(title="The Rapid Shot",message = statmentR)
    if bab>=6:
        statment2="%f is the dmg for the first bonus attack and has a chance to hit of %f"%(fdmg1,babMMa1)
        messagebox.showinfo(title="first bonus attack",message = statment2)
        if bab>=11:
            statment3="%f is the dmg for the second bonus attack and has a chance to hit of %f"%(fdmg1,babMMa2)
            messagebox.showinfo(title="second bonus attack",message = statment3)
            if bab >=16:
                statment4="%f is the dmg for the third bonus attack and has a chance to hit of %f"%(fdmg1,babMMa3)
                messagebox.showinfo(title="third bonus attack",message = statment4)


#the widgets
# all widgets need titles(where it says "tk") and to be resized so they aren't small... next work on color/graphics
def widgetRanged():
    def show_entry_fields():#passes the variables into ranged
       elm1=e1.get()
       elm2=e2.get()
       elm3=e3.get()
       ranged(elm1,elm2,elm3)#workfrom here
       e1.delete(0,END)
       e2.delete(0,END)
   
    master = Tk()
    Label(master, text="bab").grid(row=0)
    Label(master, text="base dex").grid(row=1)
    Label(master, text="base strength").grid(row=2)


    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

    #the buttons
    Button(master, text='Quit', command=master.destroy).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='calculate', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

    mainloop( )
    
def widgetMelee():
    def show_entry_fields():#passes the variables into melee
       elm1=e1.get()
       elm2=e2.get()
       elm3=e3.get()
       melee(elm1,elm2,elm3)#workfrom here
       e1.delete(0,END)
       e2.delete(0,END)
       e3.delete(0,END)
   
    master = Tk()
    Label(master, text="bab").grid(row=0)
    Label(master, text="base strength").grid(row=1)
    Label(master, text="1 handed or 2 handed?").grid(row=2)


    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

    #the buttons
    Button(master, text='Quit', command=master.destroy).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='calculate', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

    mainloop( )

#the main function
def widgetMain():# make this bigger and not whimpy
    def forMelee():
       widgetMelee()
    def forRanged():
       widgetRanged()
   
    master = Tk()

    #the buttons
    Button(master, text='Quit', command=master.destroy).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Melee attacks', command=forMelee).grid(row=3, column=1, sticky=W, pady=4)
    Button(master, text='Ranged attacks', command=forRanged).grid(row=3, column=2, sticky=W, pady=4)

    mainloop( )
widgetMain()
    
