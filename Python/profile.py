from tkinter import *
from tkinter import ttk
import json
import time
from PIL import ImageTk, Image


class bot():
    def __init__(self):
        self.main()


    def main(self):
        self.z = 0
        self.i = 0
        self.red = 0
        self.blue = 0
        self.green = 0
        self.task_count = 0
        self.root = Tk()
        self.root.geometry("300x250")
        self.root.title("Shitty Shoe Bot")
        self.root.configure(bg="lightblue")
        Label(text = "Another Shitty Shoe Bot",bg = "#8ac7e6", width = "300", height = "2", font = ("Montserrat", 13)).pack()
        img = PhotoImage(file="Images/addprofile.png")

        Button(image = img,  activebackground='#8ac7e6', width=200,command=lambda: self.profile_page()).pack()
        viewprofiles = PhotoImage(file="Images/viewprofiles.png")

        Button(image=viewprofiles, activebackground='#8ac7e6', width=200,command=lambda: self.view_profiles()).pack()

        shopify = PhotoImage(file="Images/shopify.png")

        Button(image=shopify,activebackground='#8ac7e6', command=lambda: self.shopify(),width = 200).pack()

        showtask = PhotoImage(file="Images/showtasks.png")

        Button(image=showtask, activebackground='#8ac7e6',command=lambda: self.show_tasks(), width = 200).pack()


        self.root.mainloop()
    def view_profiles(self):
        print("Loading Profiles")
        self.profile = Toplevel(self.root)
        self.profile.geometry("300x400")
        #Make the notebook
        nb = ttk.Notebook(self.profile)
        nb.pack()

        #Make 1st tab
        f1 = Frame(nb)
        #Add the tab
        #nb.add(f1, text="First tab")


        lbl1 = Label(nb, text= 'My Profiles:', padx=5, pady=5).pack()
        with open ("config.json", "r") as f:
            temp = json.load(f)

        for entry in temp:

            if entry["Profile Name"]:
                Label(nb, text=entry["Profile Name"]).pack()
                self.chk_state = IntVar()


                self.chk = Checkbutton(nb, text='Choose', var=self.chk_state, command=lambda: self.view_profiles1()).pack()

                self.i+=1

                self.view_profiles1()
            else:
                print("Not Profiles Avilable")

                Label(nb, text="No Profiles Avilable").pack()
    def view_profiles1(self):
        print(self.chk_state.get())
        self.chk_state.trace_info()



    def profile_page(self):
        self.fName = StringVar()
        self.lName = StringVar()
        self.address1 = StringVar()
        self.address2 = StringVar()
        self.apt = StringVar()
        self.states = StringVar()
        self.zip = StringVar()
        self.pname = StringVar()
        self.email_entry = StringVar()
        self.phone_entry = StringVar()
        self.cc_entry = StringVar()
        self.exp_m = StringVar()
        self.exp_y = StringVar()
        self.ccv_entry = StringVar()
        self.cardholder_entry = StringVar()
        self.city_entry = StringVar()

        print("Starting profile Addition")
        self.frame = Toplevel(self.root)
        self.frame.geometry("700x450")
        self.frame.configure(bg="#e4c7bb")




        #Credit Card
        Label(self.frame, text="Credit Card",width=20, font = ("Calibri", 11),bg="#e0c9bf").place(x=460, y=14)
        self.cc = Entry(self.frame, textvariable=self.cc_entry)
        self.cc.place(x=500, y=33)

        #exp_m
        Label(self.frame, text="Exp Month",width=20, font = ("Calibri", 11),bg="#e0c9bf").place(x=460, y=50)
        self.exp_month = Entry(self.frame, textvariable=self.exp_m)
        self.exp_month.place(x=500, y= 70)

        #exp_y
        Label(self.frame, text="Exp Year",width=20, font = ("Calibri", 11),bg="#e0c9bf").place(x=460, y=90)
        self.exp_year = Entry(self.frame, textvariable=self.exp_y)
        self.exp_year.place(x=500, y= 110)

        #CCV
        Label(self.frame, text="CCV",width=20, font = ("Calibri", 11),bg="#e0c9bf").place(x=460, y=130)
        self.ccv = Entry(self.frame, textvariable=self.ccv_entry)
        self.ccv.place(x=500, y=150)

        #Cardholder
        Label(self.frame, text="Card Holder",width=20, font = ("Calibri", 11),bg="#e0c9bf").place(x=460, y=170)
        self.cardholder = Entry(self.frame, textvariable=self.cardholder_entry)
        self.cardholder.place(x=500, y=190)

        #Profiles Avilable
        Label(self.frame, text="My Profiles").pack()

        #Profile Name
        Label(self.frame, text = "Profile Name", width=20, font = ("Calibri", 11),bg="#e0c9bf").pack()
        self.profile_name = Entry(self.frame, textvariable = self.pname)
        self.profile_name.pack()


        #First Name
        Label(self.frame, text = "First Name",  font = ("Calibri", 11),bg="#e0c9bf").pack()
        self.first_name = Entry(self.frame, textvariable = self.fName)
        self.first_name.pack()

        #Last Name
        Label(self.frame, text = "Last Name",  font = ("Calibri", 11),bg="#e0c9bf").pack()
        self.last_name = Entry(self.frame, textvariable=self.lName)
        self.last_name.pack()

        #address1
        Label(self.frame, text = "Address 1",  font = ("Calibri", 11),bg="#e0c9bf").pack()
        self.address = Entry(self.frame, textvariable=self.address1)
        self.address.pack()

        #address2
        Label(self.frame, text = "Address 2(optional)",  font = ("Calibri", 11),bg="#e0c9bf").pack()
        self.address2 = Entry(self.frame, textvariable=self.address2)
        self.address2.pack()

        #Apt Number
        Label(self.frame, text = "Apt Number (optional)",  font = ("Calibri", 11),bg="#e0c9bf").pack()
        self.apt_num = Entry(self.frame, textvariable=self.apt)
        self.apt_num.pack()

        #city
        Label(self.frame, text = "City",  font = ("Calibri", 11),bg="#e0c9bf").pack()
        self.city = Entry(self.frame, textvariable=self.city_entry)
        self.city.pack()

        #state
        Label(self.frame, text = "State",  font = ("Calibri", 11),bg="#e0c9bf").pack()
        self.state = Entry(self.frame, textvariable=self.states)
        self.state.pack()


        #zipcode
        Label(self.frame, text = "Zipcode",  font = ("Calibri", 11),bg="#e0c9bf").pack()
        self.zip_code = Entry(self.frame, textvariable=self.zip)
        self.zip_code.pack()

        #email
        Label(self.frame, text="Email",font = ("Calibri", 11),bg="#e0c9bf").pack()
        self.email = Entry(self.frame, textvariable=self.email_entry)
        self.email.pack()

        #Phone NUM
        Label(self.frame, text="Phone Number",font = ("Calibri", 11),bg="#e0c9bf").pack()
        self.phone_num = Entry(self.frame, textvariable=self.phone_entry)
        self.phone_num.pack()

        Button(self.frame, text="Submit Info", font = ("Calibri", 11), command=lambda: self.submit_profile()).place(x=500, y=210)

        self.frame.mainloop()

    def submit_profile(self):
        print("Submitting Profile")


        data_list = {"Profile Name":self.pname.get(),"FirstName":self.first_name.get(), "LastName":self.last_name.get(), "add1":self.address.get(), "add2":self.address2.get(), "apt":self.apt_num.get(), "state":self.state.get(), "zip":self.zip_code.get(),"email":self.email_entry.get(), "phoneNum": self.phone_entry.get(), "creditCard": self.cc_entry.get(), "exp_m": self.exp_m.get(), "exp_y":self.exp_y.get(), "ccv":self.ccv_entry.get(), "cardholder": self.cardholder_entry.get(), "city":self.city_entry.get()}
        print(data_list)

        with open ("config.json", "r") as f:
		          temp = json.load(f)
        temp.append(data_list)

        with open ("config.json", 'w') as f:
		          json.dump(temp, f, indent=4)

        Label(self.frame, text="Info Added", fg="green").pack()



    def shopify(self):
        self.websit = StringVar()
        self.dely = StringVar()
        self.keyword = StringVar()
        self.size_entry = StringVar()
        self.color_entry=StringVar()
        i = 0

        self.win = Toplevel(self.root)
        self.win.geometry("300x400")
        #Make the notebook
        nb = ttk.Notebook(self.win)
        nb.pack()

        #Make 1st tab
        f1 = Frame(nb)
        #Add the tab
        #nb.add(f1, text="First tab")


        lbl1 = Label(nb, text= 'My Profiles:', padx=5, pady=5).pack()
        with open ("config.json", "r") as f:
            temp = json.load(f)

        for entry in temp:

            if entry["Profile Name"]:
                Label(nb, text=entry["Profile Name"]).pack()
                self.chk_state = BooleanVar()

                self.chk_state.set(True) #set check state

                chk = Checkbutton(nb, text='Choose', var=self.chk_state).pack()


                i+=1
            else:
                print("Not Profiles Avilable")

                Label(nb, text="No Profiles Avilable").pack()

        Label(self.win, text="Website").pack()
        website = Entry(self.win, textvariable=self.websit)
        website.pack()

        Label(self.win, text='',)
        Label(self.win, text="Keywords").pack()
        kwrd = Entry(self.win, textvariable=self.keyword)
        kwrd.pack()

        Label(self.win, text="Delay (In Seconds)").pack()
        delay = Entry(self.win, textvariable=self.dely)
        delay.pack()

        Label(self.win, text="Size (Leave Blank For Random)").pack()
        size = Entry(self.win, textvariable=self.size_entry)
        size.pack()

        Label(self.win, text="Color (Leave Blank For Random)").pack()
        color = Entry(self.win, textvariable=self.color_entry)
        color.pack()

        Button(self.win, text="Create Task", command=lambda: self.create_task()).pack()



        self.win.mainloop()

    def create_task(self):
        print("Starting Task Creation")
        if self.chk_state.get():
            self.z += 1
            self.task_num = self.z
            task_list = {"Task":self.z,"Website":self.websit.get(),"Keywords":self.keyword.get(),"Delay":self.dely.get(),"size":self.size_entry.get(),"color":self.color_entry.get()}
            print(task_list)

            with open ("tasks.json", "r") as f:
    		          temps = json.load(f)
            temps.append(task_list)

            with open ("tasks.json", 'w') as f:
    		          json.dump(temps, f,indent=4 )

            Label(self.win, text="Task Created"+"("+str(self.z)+")", fg="Green", ).pack()
            Button(self.win, text="Show Tasks", command=lambda: self.show_tasks()).pack()
        else:
            Label(self.win, text="No Profiles Selected", fg="red").pack()

    def show_tasks(self):
        print("Loading task")

        self.task_win = Toplevel(self.root)
        self.task_win.geometry("900x850")
        self.task_win.configure(bg="lightblue")

        Label(self.task_win, text="Shopify",bg = "#8ac7e6", width = "300", height = "2", font = ("Calibri", 13) ).pack()
        runimg = PhotoImage(file="Images/run.png")
        with open ("tasks.json", "r") as f:
		          temp = json.load(f)
        for entry in temp:
                  self.task_count += 1


                  Label(self.task_win, text="Task:"+str(entry["Task"]), bg = "#AC67F9", width = "10", height = "2", font = ("Calibri", 13)).pack()

                  Label(self.task_win, text="Website: "+entry["Website"], bg="#a3dbf7").pack()
                  Label(self.task_win, text="Keywords: "+entry["Keywords"],bg="#a3dbf7").pack()
                  Label(self.task_win, text="Delay: "+entry["Delay"], bg="#a3dbf7").pack()
                  Label(self.task_win, text="Size: "+entry["size"], bg="#a3dbf7").pack()
                  Label(self.task_win, text="Color: "+entry["color"], bg="#a3dbf7").pack()

                  Button(self.task_win, text="Delete", width=10, height=2, command=lambda: self.delete_task()).pack()
                  Button(self.task_win, text="Run",width=10, height=2, command=lambda: self.run_task()).pack()
                  Label(self.task_win, text="**********************************************************************************", fg="blue").pack()
                  #Label(self.task_win, text="", width=10, height=10).pack()
        #Button(self.task_win, text="Back", command=lambda: self.main()).pack()
        self.task_win.mainloop()

    def delete_task(self):
        print("Deleting")



    def run_task(self):
        print("Starting Task")








bot()
