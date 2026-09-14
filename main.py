from webbrowser import register

#first set of import for splash,login and sigup
import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox, END

#later wen creating function for clock
from datetime import datetime, time

#second intallation set
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3




#creating the class for the application
class App:
    def __init__(self):#initialize the class using the init function,which would be callled automatically wen the class is created

        self.messagebox = None
        self.clock()


        self.Splashwindow = tk.Tk()
        self.Splashwindow.title('School Management System')
        #self.Splashwindow.geometry('1000x650')

        # Center the window on the screen
        window_width = 700
        window_height = 550
        screen_width = self.Splashwindow.winfo_screenwidth()
        screen_height = self.Splashwindow.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.Splashwindow.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
        self.Splashwindow.config(bg='white')

        #icon photo
        self.image_icon1 = Image.open('images/360_F_238940516_0BihE7YocY9vpgClPDDWuuaLneDwxtWn.png')
        self.image_icon1 = ImageTk.PhotoImage(self.image_icon1)
        self.Splashwindow.iconphoto(False, self.image_icon1)
        #print("loginwindow() executed successfully.")

         #splash window display image and text
        self.image2 = Image.open('images/EMMMA1.png')
        self.image2 = ImageTk.PhotoImage(self.image2)
        self.label2 = tk.Label(self.Splashwindow, image=self.image2, bg='white')
        self.label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.label3 = tk.Label(self.Splashwindow, text='SCHOOL MANAGEMENT SYSTEM',
                               bg='white', fg='#173662', font=('Times', 20))
        self.label3.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        #open a new window after 6sec of displaying the splashscreen
        self.Splashwindow.after(1000,self.loginwindow)


    def loginwindow(self):
        #destroy or remove the splashscreen completely
        self.Splashwindow.destroy()


        #initialize the new window from the class
        self.login_window =tk.Tk()
        self.login_window.title('School MAnagement System')
        self.login_window.geometry('1000x600')
        self.login_window.config(bg='white')

        window_width = 1000
        window_height = 600
        screen_width = self.login_window.winfo_screenwidth()
        screen_height = self.login_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.login_window.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
        self.login_window.resizable(False, False)

        #insert an icon to the new window9login window)
        self.image_icon2  = Image.open('images/360_F_238940516_0BihE7YocY9vpgClPDDWuuaLneDwxtWn.jpg')
        self.image_icon2 = ImageTk.PhotoImage(self.image_icon2)
        self.login_window.iconphoto(False, self.image_icon2)


        #creating frame widget on the window

        self.login_frame = ctk.CTkFrame(self.login_window, fg_color='#173662', width=450,
                                   height=600,corner_radius=10)
        self.login_frame.place(relx=0.67, rely=0.1)
        self.login_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        #add image images to the login frame
        self.image3 = Image.open('images/EMMMA1.png')
        self.image3 = ImageTk.PhotoImage(self.image3)
        self.label4 = tk.Label(self.login_window, image=self.image3, bg='white')
        self.label4.pack(side=tk.LEFT, padx=120, pady=10)
        #print('hi')
        #creating labels on th frame

        labelwlcm=ctk.CTkLabel(self.login_frame, text='Welcome Back!',font=('Italian bold', 30),
                               text_color='white',fg_color='#173662')
        labelwlcm.place(relx=0.05,rely=0.11)
        labelwlcm2 = ctk.CTkLabel(self.login_frame, text='sign into your account', font=('Ariel', 20),
                                 text_color='white', fg_color='#173662')
        #'#173662'
        labelwlcm2.place(relx=0.05, rely=0.18)
        print('how about here')
        #for username
        self.image_username = Image.open('images/user (2).png')
        self.image_username = ctk.CTkImage(self.image_username)
        self.username_label = ctk.CTkLabel(self.login_frame, text='User_ID:', compound=tk.LEFT, image=self.image_username,
                                    fg_color='#173662', font=('Times bold', 25), text_color='white',padx=1,pady=5)
        self.username_label.place(relx=0.05,rely=0.3)

        self.username_entry=ctk.CTkEntry(self.login_frame,placeholder_text='enter username',width=350,height=50,
                                   text_color='black',corner_radius=15,
                                   border_color='black',font=('Helvetica',18))
        self.username_entry.place(relx=0.05,rely=0.4)

        # for password
        self.image_password = Image.open('images/padlock-check (1).png')
        self.image_password = ctk.CTkImage(self.image_password)
        self.password_label = ctk.CTkLabel(self.login_frame, text='PassWord:', compound=tk.LEFT, image=self.image_password,
                                    fg_color='#173662', font=('Times bold', 25), text_color='white', padx=1, pady=5)
        self.password_label.place(relx=0.05, rely=0.55)
        self.passentry = ctk.CTkEntry(self.login_frame, placeholder_text='password', width=350, height=50,
                                     text_color='black', corner_radius=15,
                                     border_color='black', font=('Helvetica', 18),border_width=1)
        self.passentry.place(relx=0.05, rely=0.65)
        print('hope all is well')
        #button
        self.image_but = Image.open('images/sign-in-alt.png')
        button_submit=ctk.CTkButton(self.login_frame,text='sign in',corner_radius=32,
                                    text_color= 'blue',border_color='black',border_spacing=2,
                                    fg_color='#c6e2b5',hover_color='grey',command=self.signup,
                                    border_width=2, image=ctk.CTkImage(self.image_but),width=350,height=50,font=('Times',20))
        button_submit.place(relx=0.05,rely=0.85)


    #function to signup

    def signup(self):
        #userid = self.username_entry.get()
        #password = self.passentry.get()

        #if 'project' not in userid:
            #messagebox.showinfo('error', 'Incorrect information')
            #return
        #elif password != "1234":
            #messagebox.showinfo('Opps', 'incorrect information')
            #return
        #else:
        self.mainwindow()
            ##messagebox.showinfo('error', 'An unknown error')

    #creating the main window
    def mainwindow(self):
        self.login_window.destroy()
        self.main_window = tk.Tk()
        self.main_window.title('School MAnagement System')
        self.main_window.geometry('1200x650')
        self.main_window.config(bg='#ecebe9')
        window_width = 1200
        window_height = 620
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.main_window.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')

        #icon image for the main window...
        self.image_icon3 = Image.open('images/360_F_238940516_0BihE7YocY9vpgClPDDWuuaLneDwxtWn.jpg')
        self.image_icon3 = ImageTk.PhotoImage(self.image_icon3)
        self.main_window.iconphoto(False, self.image_icon3)

        #side-frame for main window
        self.side_frame = ctk.CTkFrame(self.main_window, fg_color='#173662', width=250,
                                   height=680, corner_radius=10)
        self.side_frame.place(relx=0.67, rely=0.1)
        self.side_frame.pack(side=tk.LEFT, pady=10, padx=20)

        self.image_top = Image.open('images/top_image.png')
        self.image_top = ctk.CTkImage(self.image_top)
        self.label3F1 = ctk.CTkLabel(self.side_frame, text='FINAL YEAR PROJECT', compound=tk.LEFT, image=self.image_top,
                                     fg_color='#173662', font=('Italian bold', 15), text_color='white', padx=8, pady=5)
        self.label3F1.place(relx=0.43, rely=0.06, anchor=tk.CENTER)

        top_text = ctk.CTkLabel(self.side_frame, text='Academics excellence and power', font=('Ariel', 10),
                                text_color='white', fg_color='#173662')
        top_text.place(relx=0.13, rely=0.08)

        self.frameline = ctk.CTkFrame(self.side_frame, fg_color='white', width=200,
                                      height=5, corner_radius=10)
        self.frameline.place(relx=0.06, rely=0.17, anchor='sw')
        # self.frameline.pack(side=tk.LEFT, padx=10, pady=10)
        print('check2')

       #creating the buttons on the menu frame
        #chnage the transparent fg color to #276878 by the end of part one video
        self.icon_butHome = Image.open('images/home-page-white-icon.png')
        self.button_Home = ctk.CTkButton(self.side_frame , text='Home',
                                         text_color='white',
                                         fg_color='transparent', hover_color='#276878',
                                         image=ctk.CTkImage(self.icon_butHome), width=120, height=35,
                                         font=('Times', 18),command=self.homepage)
        self.button_Home.place(relx=0.05, rely=0.25)

        self.icon_Butreg = Image.open('images/pencil-2-32.png')
        self.button_register = ctk.CTkButton(self.side_frame , text='Registration',
                                             text_color='white',
                                             fg_color='transparent', hover_color='#276878',
                                             image=ctk.CTkImage(self.icon_Butreg), width=120, height=35,
                                             font=('Times', 18),command=self.register)
        self.button_register.place(relx=0.1, rely=0.35)

        self.icon_Butsearch = Image.open('images/search-9-32.png')
        self.button_search = ctk.CTkButton(self.side_frame , text='Search',
                                           text_color='white',
                                           fg_color='transparent', hover_color='#276878',
                                           image=ctk.CTkImage(self.icon_Butsearch), width=120, height=35,
                                           font=('Times', 18))
        self.button_search.place(relx=0.05, rely=0.45)

        self.icon_Butresult = Image.open('images/book-16-32.png')
        self.button_result = ctk.CTkButton(self.side_frame, text='Result',
                                           text_color='white',
                                           fg_color='transparent', hover_color='#276878',
                                           image=ctk.CTkImage(self.icon_Butresult), width=120, height=35,
                                           font=('Times', 18))
        self.button_result.place(relx=0.05, rely=0.55)

        self.icon_Butrecord = Image.open('images/text-file-32.png')
        self.button_record = ctk.CTkButton(self.side_frame , text='Record',
                                           text_color='white',
                                           fg_color='transparent', hover_color='#276878',
                                           image=ctk.CTkImage(self.icon_Butrecord), width=120, height=35,
                                           font=('Times', 18))
        self.button_record.place(relx=0.05, rely=0.65)

        self.icon_ButDB = Image.open('images/database-32.png')
        self.button_database = ctk.CTkButton(self.side_frame , text='Database',
                                             text_color='white',
                                             fg_color='transparent', hover_color='#276878',

                                             image=ctk.CTkImage(self.icon_ButDB), width=120, height=35,
                                             font=('Times', 18))
        self.button_database.place(relx=0.05, rely=0.75)

        self.button_logout = ctk.CTkButton(self.side_frame, text='LogOut',
                                           text_color='white',
                                           fg_color='transparent', hover_color='#276878',
                                           image=ctk.CTkImage(self.image_but), width=120, height=35,
                                           font=('Times', 18))
        self.button_logout.place(relx=0.05, rely=0.90)


        #create the mainframe by the right on the main window

        self.mainframe = ctk.CTkFrame(self.main_window, fg_color='#ECEBE9', width=1400,
                                       height=680, corner_radius=10, border_color='#173662',
                                       border_width=0)
        self.mainframe.place(relx=0.5, rely=0.5)
        self.mainframe.pack(pady=0, padx=0, fill=ctk.BOTH)

        self.homepage()

    def homepage(self):

        #only put this at the end of the part one video
        self.destroymain()
        #-------------------

        self.button_Home.configure(fg_color='#276878')
        self.largeframe = ctk.CTkFrame(self.mainframe, fg_color='#ECEBE9', width=1400,
                                       height=680, corner_radius=10, border_color='#173662',
                                       border_width=0)
        self.largeframe.place(relx=0.5, rely=0.5)
        self.largeframe.pack(pady=0, padx=0, fill=ctk.BOTH)

        # top frame
        self.top_frame = ctk.CTkFrame(self.largeframe, fg_color='white', width=1020,
                                      height=25, corner_radius=5,
                                      )
        self.top_frame.pack(side=ctk.TOP, pady=15, ipady=10, fill=ctk.X)
        print('chek5')
        # small frames

        self.smallframe1 = ctk.CTkFrame(self.largeframe, fg_color='white', width=200,
                                        height=80, corner_radius=10,
                                        )


        self.smallframe2 = ctk.CTkFrame(self.largeframe, fg_color='white', width=200,
                                        height=80, corner_radius=10,
                                        )
        self.smallframe3 = ctk.CTkFrame(self.largeframe, fg_color='white', width=200,
                                        height=80, corner_radius=10,
                                        )
        self.smallframe4 = ctk.CTkFrame(self.largeframe, fg_color='white', width=200,
                                        height=80, corner_radius=10,
                                        )

        self.smallframe1.pack(side=ctk.LEFT, padx=0, expand=True, ipadx=10)
        self.smallframe2.pack(side=ctk.LEFT, padx=10, expand=True, ipadx=20)
        self.smallframe3.pack(side=ctk.LEFT, padx=10, expand=True, ipadx=20)
        self.smallframe4.pack(side=ctk.LEFT, padx=0, expand=True, ipadx=10)

        self.largeframe2 = ctk.CTkFrame(self.mainframe, fg_color='#ecebe9', width=680,
                                        height=600, corner_radius=10, border_color='#173662',
                                        border_width=0)
        self.largeframe2.place(relx=0.26, rely=0.35)
        self.largeframe2.pack(side=ctk.LEFT, padx=2, pady=5)

        self.smallframe5 = ctk.CTkFrame(self.largeframe2, fg_color='white', width=320,
                                         height=250, corner_radius=10,
                                         )
        self.smallframe5.place(relx=0.15, rely=1, anchor='s')
        self.smallframe6 = ctk.CTkScrollableFrame(self.mainframe, fg_color='white', width=370,
                                                   height=500, corner_radius=10, orientation='vertical',
                                                   scrollbar_button_color='#276878',
                                                   scrollbar_button_hover_color='#173662')
        self.smallframe6.pack(side=ctk.LEFT, padx=8, pady=5)

        self.smallframe7 = ctk.CTkFrame(self.largeframe2, fg_color='white', width=320,
                                         height=250, corner_radius=10,
                                         )
        self.smallframe7.place(relx=0.4, rely=0.5, anchor='s')
        self.smallframe8 = ctk.CTkFrame(self.largeframe2, fg_color='white', width=600,
                                         height=250, corner_radius=10,
                                         )
        self.smallframe8.place(relx=0.01, rely=0.01)



        #pack widget to make it flexible nd scale to screen
        self.smallframe8.pack(fill=ctk.X, pady=10)
        self.smallframe5.pack(side=ctk.RIGHT, pady=2, padx=5)
        self.smallframe7.pack(side=ctk.RIGHT, pady=0, padx=0, ipadx=20)


        # labels and widget on the frames
        labeltopframe = ctk.CTkLabel(self.top_frame, text='DASHBOARD', font=('Helvetica', 20),
                                     text_color='#173662', fg_color='WHITE', corner_radius=4)
        labeltopframe.place(relx=0.01, rely=0.1)

        self.labeltopframeENTRY = ctk.CTkEntry(self.top_frame, placeholder_text='search for student with matric number',
                                               width=500, height=30,
                                               text_color='#090a06', corner_radius=15,
                                               border_color='#ecebe9', font=('Ariel', 10))
        self.labeltopframeENTRY.place(relx=0.2, rely=0.2)

         #search bar
        self.searchicon = Image.open('images/search1.png')
        searchtop = ctk.CTkButton(self.top_frame, text='',
                                  fg_color='#ecebe9',
                                  image=ctk.CTkImage(self.icon_Butsearch), width=20, height=20
                                  )
        searchtop.place(relx=0.62, rely=0.25)

         #notification for the top
        self.noticon = Image.open('images/notification3.png')
        notitop = ctk.CTkButton(self.top_frame, text='',
                                fg_color='white',
                                image=ctk.CTkImage(self.noticon), width=25, height=25,
                                )
        notitop.place(relx=0.78, rely=0.1)

        #database coonection button
        self.topcon = ctk.CTkButton(self.top_frame, text='Connect',
                                    fg_color='green',
                                    width=100, height=40, text_color='white',
                                    command=self.connectDatabase)
        self.topcon.place(relx=0.85, rely=0.12)

        #add content to the frames

        self.smallframe1image = Image.open('images/studying1.png')

        self.smallframe1image = ImageTk.PhotoImage(self.smallframe1image)
        self.smallframe1label1 = tk.Label(self.smallframe1, image=self.smallframe1image, bg='white')
        self.smallframe1label1.place(relx=0.1, rely=0.1)

        smallframe1label2 = ctk.CTkLabel(self.smallframe1, text='Students', font=('Ariel', 10),
                                     text_color='#242818', fg_color='white', corner_radius=4)
        smallframe1label2.place(relx=0.37, rely=0.1)

        smallframe1label3 = ctk.CTkLabel(self.smallframe1, text='12,765', font=('Helvetica', 30),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smallframe1label3.place(relx=0.35, rely=0.45)


        # second small frame
        self.smallframe2image = Image.open('images/teacher1.png')

        self.smallframe2image = ImageTk.PhotoImage(self.smallframe2image)
        self.smallframe2label1 = tk.Label(self.smallframe2, image=self.smallframe2image, bg='white')
        self.smallframe2label1.place(relx=0.1, rely=0.1)
        smallframe2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
                                     text_color='#242818', fg_color='white', corner_radius=4)
        smallframe2label2.place(relx=0.37, rely=0.1)

        smallframe2label3 = ctk.CTkLabel(self.smallframe2, text='108', font=('Helvetica', 30),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smallframe2label3.place(relx=0.35, rely=0.45)


        # third frame
        self.smallframe3image = Image.open('images/379383_student_icon.png')

        self.smallframe3image = ImageTk.PhotoImage(self.smallframe3image)
        self.smallframe3label1 = tk.Label(self.smallframe3, image=self.smallframe3image, bg='white')
        self.smallframe3label1.place(relx=0.1, rely=0.1)
        smallframe3label2 = ctk.CTkLabel(self.smallframe3, text='Graduates', font=('Ariel', 10),
                                     text_color='#242818', fg_color='white', corner_radius=4)
        smallframe3label2.place(relx=0.37, rely=0.1)

        smallframe3label3 = ctk.CTkLabel(self.smallframe3, text='32,762', font=('Helvetica', 30),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smallframe3label3.place(relx=0.35, rely=0.45)


        # fourth frame
        self.smallframe4image = Image.open('images/books (1).png')

        self.smallframe4image = ImageTk.PhotoImage(self.smallframe4image)
        self.smallframe4label1 = tk.Label(self.smallframe4, image=self.smallframe4image, bg='white')
        self.smallframe4label1.place(relx=0.1, rely=0.1)
        smallframe4label2 = ctk.CTkLabel(self.smallframe4, text='Courses', font=('Ariel', 10),
                                     text_color='#242818', fg_color='white', corner_radius=4)
        smallframe4label2.place(relx=0.37, rely=0.1)

        smallframe4label3 = ctk.CTkLabel(self.smallframe4, text='620', font=('Helvetica', 30),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smallframe4label3.place(relx=0.35, rely=0.45)

        #calling function to provide data into those other small large frames
        self.draw_bar_chart()
        self.draw_pie_chart()
        #self.draw_scatter_plot()

        # frame scrollable info

        smallframe6label1 = ctk.CTkLabel(self.smallframe6, text='LIST OF COURSES', font=('Helvetica', 15),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smallframe6label1.pack(pady=5)

        self.frameline2 = ctk.CTkFrame(self.smallframe6, fg_color='#173662', width=300,
                                       height=5, corner_radius=10)
        self.frameline2.pack(pady=15)

        smallframe6label2 = ctk.CTkLabel(self.smallframe6, text='Computer science\nFood technology\nSLT'
                                                             '\nBanking & Finance\nComputer Engineering\nElect Elect'
                                                             '\nAccounting\nHMT\nTaxation\nAgric Technology\nMechatronic\nCivil Engineering\nMass Comm\nMarkerting\ne.t.c',
                                     font=('Ariel', 15),
                                     text_color='black', fg_color='white')
        smallframe6label2.pack(pady=10, padx=0.1)

        smallframe6label3 = ctk.CTkLabel(self.smallframe6, text='LIST OF FACULTY', font=('Helvetica', 15),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smallframe6label3.pack(pady=5)

        self.frameline4 = ctk.CTkFrame(self.smallframe6, fg_color='#173662', width=300,
                                       height=5, corner_radius=10)
        self.frameline4.pack(pady=15)

        smallframe6label4 = ctk.CTkLabel(self.smallframe6, text='Applied Science\nEngineering\nCommunication'
                                                             '\nART\nManagement\nElect Elect'
                                                             '\nCommerce\nAgriculture\ne.t.c',
                                     font=('Ariel', 15),
                                     text_color='black', fg_color='white')
        smallframe6label4.pack(pady=10, padx=0.1)

        smallframe6label5 = ctk.CTkLabel(self.smallframe6, text='NUMBER OF STUENTS', font=('Helvetica', 15),
                                     text_color='#173662', fg_color='white', corner_radius=4)
        smallframe6label5.pack(pady=5)
        self.frameline5 = ctk.CTkFrame(self.smallframe6, fg_color='#173662', width=300,
                                       height=5, corner_radius=10)
        self.frameline5.pack(pady=15)

        smallframe6label6 = ctk.CTkLabel(self.smallframe6, text='Computer science: 512\nFood technology: 613\nSLT: 900'
                                                             '\nBanking & Finance: 1023\nComputer Engineering: 2515\nElect Elect: 896'
                                                             '\nAccounting: 1890\nHMT: 654\nTaxation: 432\nAgric Technology: 789\nMechatronic: 321\nCivil Engineering: 657\nMass Comm: 3567\nMarkerting: 761\ne.t.c',
                                     font=('Ariel', 15),
                                     text_color='black', fg_color='white')
        smallframe6label6.pack(pady=10, padx=0.1)



    def draw_bar_chart(self):

        # Sample data
        categories = ['Com-Sci', 'SLT', 'Mass-Com','Food-Nut',
                      'Com-Eng', 'Elect-Elect','Civil-Eng','Accounting',
                      'Bank&Fin','Architecture','Machanical','Mechatronic']
        values = [85, 90, 80, 50, 75,80,80,70,75,72,80,65]
        #colors = ['red', 'green', 'blue', 'orange', 'purple']
        fig, ax = plt.subplots(figsize=(5, 3), dpi=100)
        ax.bar(categories, values)
        #ax.set_xlabel('Courses',color='#173662')
        ax.set_ylabel('Percentage',color='#173662')
        ax.set_title('Course competitiveness')
        plt.xticks(rotation=10, ha='right',fontsize=5)

        canvas = FigureCanvasTkAgg(fig, master=self.smallframe8)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def draw_pie_chart(self):

        # Sample data (replace with your actual data)
        male_count = 450
        female_count = 550

        # Calculate percentages
        total_count = male_count + female_count
        male_percentage = (male_count / total_count) * 100
        female_percentage = (female_count / total_count) * 100

        # Create labels and sizes for the pie chart
        labels = ['Male', 'Female']
        sizes = [male_percentage, female_percentage]
        colors = ['lightblue', 'lightcoral']

        # Create the pie chart
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.set_title('Percentage of Boys to Girls',fontsize=7)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Embed the plot in a Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.smallframe7)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, rely=1, anchor=tk.CENTER)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        #canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=tk.CENTER)




   #second part of the first video begins here

    #first we have to create a way to remove everythin currently on the mainwindow
    #except the side menubar,hence we create the destroy function;

    def destroymain(self):
        for frame in self.mainframe.winfo_children():
            frame.destroy()
        for button in self.side_frame.winfo_children():
            button.configure(fg_color='transparent')

        self.frameline.configure(fg_color='white')


    def clock(self):
        time = datetime.now()
        self.date=time.strftime('%d/%m/%Y')
        self.currenttime=time.strftime('%H:%M:%S')
        print(self.currenttime,self.date)


    #create database and set it as a command to the connect button at the top of the dashboard

    def connectDatabase(self):
        try:
            # SQLite connection (creates a database file if it doesn't exist)
            self.con = sqlite3.connect('SchoolManagementSystem.db')
            self.mycursor = self.con.cursor()
        except sqlite3.Error as e:
            messagebox.showinfo('Error', f"Couldn't connect to the database: {e}")
            print(e)
            return

        try:
            # Creating the Student table
            self.mycursor.execute('''CREATE TABLE IF NOT EXISTS Student(
                    Matric_no TEXT NOT NULL PRIMARY KEY,
                    Surname TEXT,
                    Name TEXT,
                    DOB TEXT,                -- Changed D.O.B to DOB
                    Department TEXT,
                    Gender TEXT,
                    Level TEXT,
                    Grade TEXT,
                    Status REAL,
                    Faculty TEXT,            -- Changed Falculty to Faculty
                    Email TEXT,
                    Phone_No TEXT,
                    Time TEXT,
                    Date TEXT
                )''')

            # Creating the StudentInformation table
            self.mycursor.execute('''CREATE TABLE IF NOT EXISTS StudentInformation(
                    `key` TEXT,
                    `value` TEXT,
                    description TEXT,
                    PRIMARY KEY(`key`, `value`)
                )''')
        except sqlite3.Error as e:
            messagebox.showinfo('Error', f"An error occurred while creating tables: {e}")
            print(e)
            return

        messagebox.showinfo('Success', 'Database successfully connected')
        self.topcon.configure(fg_color='green', text="Connected")

        #not needed now in current video
        #self.button_Home.configure(state='normal')
        #self.button_register.configure(state='normal')
        #self.button_record.configure(state='normal')
        #self.button_result.configure(state='normal')
        #self.button_search.configure(state='normal')
        #self.button_database.configure(state='normal')
        #self.homepage()

    #create the register function and the widget first before the internal register
    # command to actually safe to database
    def register(self):
         #only create this after designing the widget
         #for the register page and creating the database

        def internal_register():
            if (
                    self.Matric2entry.get() == '' or
                    self.Surname2entry.get() == '' or
                    self.Name2entry.get() == '' or
                    self.DOB2entry.get() == '' or
                    self.Dept2entry.get() == '' or
                    self.Gender2entry.get() == '' or
                    self.Level2entry.get() == '' or
                    self.Grade2entry.get() == '' or
                    self.Status2entry.get() == '' or
                    self.Fac2entry.get() == '' or
                    self.Email2entry.get() == '' or
                    self.phone2entry.get() == ''
            ):
                messagebox.showerror('Error', 'No field should be left empty')

            else:
                try:
                    query = '''INSERT INTO Student (
                        Matric_no, Surname, Name, DOB, Department, Gender,
                        Level, Grade, Status, Faculty, Email, Phone_No, Time, Date
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

                    self.mycursor.execute(query, (
                        self.Matric2entry.get(), self.Surname2entry.get(), self.Name2entry.get(),
                        self.DOB2entry.get(), self.Dept2entry.get(), self.Gender2entry.get(),
                        self.Level2entry.get(), self.Grade2entry.get(), self.Status2entry.get(),
                        self.Fac2entry.get(), self.Email2entry.get(), self.phone2entry.get(),
                        #import datetime package above after putting this and create the clock function to be added to tha App
                        self.currenttime, self.date
                    ))

                    self.con.commit()

                    result = messagebox.askyesno('Data Added Successfully', 'Do you want to clear the form?')
                    if result:
                        self.Matric2entry.delete(0, END)
                        self.Surname2entry.delete(0, END)
                        self.Name2entry.delete(0, END)
                        self.DOB2entry.delete(0, END)
                        self.Dept2entry.delete(0, END)
                        self.Grade2entry.delete(0, END)
                        self.Level2entry.delete(0, END)
                        self.Email2entry.delete(0, END)
                        self.Gender2entry.delete(0, END)
                        self.phone2entry.delete(0, END)
                        self.Fac2entry.delete(0, END)
                        self.Status2entry.delete(0, END)

                except sqlite3.IntegrityError:
                    messagebox.showerror('Error', 'Matric number already exists!')
                    return

                query = 'select *from student'
                self.mycursor.execute(query)
                self.fecthed_data = self.mycursor.fetchall()
                print(self.fecthed_data)

        self.destroymain()

        self.button_register.configure(fg_color='#276878')
        self.largeframe2 = ctk.CTkScrollableFrame(self.mainframe, fg_color='#ECEBE9', width=1000,
                                       height=650, corner_radius=10, border_color='#173662',
                                       border_width=0,orientation='vertical')
        self.largeframe2.place(relx=0.01, rely=0.01)

        self.labelregg = ctk.CTkLabel(self.largeframe2, text='REGISTER NEW STUDENT',image=ctk.CTkImage(self.icon_Butreg),compound=tk.LEFT,
                                         fg_color='blue', font=('Times', 25), text_color='white',
                                      corner_radius=10)
        self.labelregg.grid(row=0,columnspan=3,padx=20,pady=15)

        self.labelMatric2 = ctk.CTkLabel(self.largeframe2, text='Matric_No:',
                                         fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelMatric2.grid(row=1,column=0,padx=10, pady=15,sticky='w')

        self.Matric2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Matric_no(e.g N/CS/22/3087)', width=500, height=35,
                                         text_color='black', corner_radius=10,
                                         border_color='black', font=('Helvetica', 18), border_width=1)
        self.Matric2entry.grid(row=1,column=1,sticky='w',padx=10)

        self.labelSurname2 = ctk.CTkLabel(self.largeframe2, text='Surname:',
                                         fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelSurname2.grid(row=2, column=0, padx=10, pady=15, sticky='w')

        self.Surname2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Surname(preferrably uppercase letter)', width=500, height=35,
                                         text_color='black', corner_radius=10,
                                         border_color='black', font=('Helvetica', 18), border_width=1)
        self.Surname2entry.grid(row=2, column=1, sticky='w', padx=10)

        self.labelName2 = ctk.CTkLabel(self.largeframe2, text='Name:',
                                          fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelName2.grid(row=3, column=0, padx=10, pady=15, sticky='w')

        self.Name2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Name(preferrably uppercase letter)', width=500, height=35,
                                          text_color='black', corner_radius=10,
                                          border_color='black', font=('Helvetica', 18), border_width=1)
        self.Name2entry.grid(row=3, column=1, sticky='w', padx=10)

        self.labelDOB2 = ctk.CTkLabel(self.largeframe2, text='DOB:',
                                       fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelDOB2.grid(row=4, column=0, padx=10, pady=15, sticky='w')

        self.DOB2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your DOB(preferrably uppercase letter)', width=500, height=35,
                                       text_color='black', corner_radius=10,
                                       border_color='black', font=('Helvetica', 18), border_width=1)
        self.DOB2entry.grid(row=4, column=1, sticky='w', padx=10)

        self.labelDept2 = ctk.CTkLabel(self.largeframe2, text='Department:',
                                      fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelDept2.grid(row=5, column=0, padx=10, pady=15, sticky='w')

        self.Dept2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Department(preferrably uppercase letter)', width=500, height=35,
                                      text_color='black', corner_radius=10,
                                      border_color='black', font=('Helvetica', 18), border_width=1)
        self.Dept2entry.grid(row=5, column=1, sticky='w', padx=10)

        self.labelGender2 = ctk.CTkLabel(self.largeframe2, text='Gender:',
                                       fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelGender2.grid(row=6, column=0, padx=10, pady=15, sticky='w')

        self.Gender2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your gender', width=500, height=35,
                                       text_color='black', corner_radius=10,
                                       border_color='black', font=('Helvetica', 18), border_width=1)
        self.Gender2entry.grid(row=6, column=1, sticky='w', padx=10)

        self.labelLevel2 = ctk.CTkLabel(self.largeframe2, text='Level:',
                                         fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelLevel2.grid(row=7, column=0, padx=10, pady=15, sticky='w')

        self.Level2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Level(e.g ND 2)', width=500, height=35,
                                         text_color='black', corner_radius=10,
                                         border_color='black', font=('Helvetica', 18), border_width=1)
        self.Level2entry.grid(row=7, column=1, sticky='w', padx=10)

        self.labelGrade2 = ctk.CTkLabel(self.largeframe2, text='Grade:',
                                        fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelGrade2.grid(row=8, column=0, padx=10, pady=15, sticky='w')

        self.Grade2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your grade(e.g DISTINCTION,UPPER,LOWER)', width=500, height=35,
                                        text_color='black', corner_radius=10,
                                        border_color='black', font=('Helvetica', 18), border_width=1)
        self.Grade2entry.grid(row=8, column=1, sticky='w', padx=10)

        self.labelStatus2 = ctk.CTkLabel(self.largeframe2, text='Cgpa:',
                                      fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelStatus2.grid(row=9, column=0, padx=10, pady=15, sticky='w')

        self.Status2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your cgpa(e.g 3.99)', width=500, height=35,
                                        text_color='black', corner_radius=10,
                                        border_color='black', font=('Helvetica', 18), border_width=1)
        self.Status2entry.grid(row=9, column=1, sticky='w', padx=10)


        self.labelFac2 = ctk.CTkLabel(self.largeframe2, text='Faculty:',
                                       fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelFac2.grid(row=10, column=0, padx=10, pady=15, sticky='w')

        self.Fac2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Faculty(e.g APPLIED SCIENCE,ENGINEERING ETC)', width=500, height=35,
                                        text_color='black', corner_radius=10,
                                        border_color='black', font=('Helvetica', 18), border_width=1)
        self.Fac2entry.grid(row=10, column=1, sticky='w', padx=10)

        self.labelEmail2 = ctk.CTkLabel(self.largeframe2, text='Email:',
                                      fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelEmail2.grid(row=11, column=0, padx=10, pady=15, sticky='w')

        self.Email2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your Email', width=500, height=35,
                                      text_color='black', corner_radius=10,
                                      border_color='black', font=('Helvetica', 18), border_width=1)
        self.Email2entry.grid(row=11, column=1, sticky='w', padx=10)

        self.labelphone2 = ctk.CTkLabel(self.largeframe2, text='Phone_no:',
                                        fg_color='#ECEBE9', font=('Times', 25), text_color='black')
        self.labelphone2.grid(row=12, column=0, padx=10, pady=15, sticky='w')

        self.phone2entry = ctk.CTkEntry(self.largeframe2, placeholder_text='enter your phone_no', width=500, height=35,
                                        text_color='black', corner_radius=10,
                                        border_color='black', font=('Helvetica', 18), border_width=1)
        self.phone2entry.grid(row=12, column=1, sticky='w', padx=10)

        self.registernew = ctk.CTkButton(self.largeframe2, text='Register', corner_radius=32,
                                         text_color='white', border_color='black', border_spacing=2,
                                         fg_color='#173662', hover_color='#276878', command=internal_register,
                                         border_width=2, image=ctk.CTkImage(self.image_but), width=200, height=50,
                                         font=('Times', 20))
        self.registernew.grid(row=13,columnspan=3)


        #use this to display data in database
        query = 'select *from student'
        self.mycursor.execute(query)
        self.fecthed_data = self.mycursor.fetchall()
        print(self.fecthed_data)





    #BEGINNER OF PART TWO VIDEO SEARCH AND RECORD PAGE




    def get_top_students(self, level, department, top_n=3):

        # Define the query to fetch the top 3 students by CGPA in the specified level and department
        query = """
                       SELECT * FROM student
                       WHERE Level = ? AND Department = ?
                       ORDER BY Status DESC
                       LIMIT ?
                       """

        # Execute the query with the given level and department
        self.mycursor.execute(query, (level, department, top_n))

        # Fetch the results
        top_students = self.mycursor.fetchall()

        if len(top_students) < 3:
            messagebox.showinfo('Error','Data not Available')
            self.smallwindow.destroy()
        else:
           return top_students

    def get_top_students2(self,department, top_n=3):

        # Define the query to fetch the top 3 students by CGPA in the specified level and department
        query = """
                       SELECT * FROM student
                       WHERE  Department = ?
                       ORDER BY Status DESC
                       LIMIT ?
                       """

        # Execute the query with the given level and department
        self.mycursor.execute(query, ( department, top_n))

        # Fetch the results
        top_students = self.mycursor.fetchall()
        #print('did you execute up to here')
        if len(top_students) < 3:
            messagebox.showinfo('Error', 'Data not Available')
            self.smallwindow.destroy()
        else:
            return top_students

    def get_top_students3(self, faculty, top_n=3):

        # Define the query to fetch the top 3 students by CGPA in the specified level and department
        query = """
                       SELECT * FROM student
                       WHERE Faculty = ?
                       ORDER BY Status DESC
                       LIMIT ?
                       """

        # Execute the query with the given level and department
        self.mycursor.execute(query, (faculty,top_n))

        # Fetch the results
        top_students = self.mycursor.fetchall()
        print('did you execute up to here')
        if len(top_students) < 3:
            messagebox.showinfo('Error', 'Data not Available')
            self.smallwindow.destroy()
        else:
            return top_students

    def get_top_students4(self, top_n=3):
        # Define the query to fetch the top students by CGPA in descending order
        query = """
            SELECT * FROM Student
            ORDER BY Status DESC
            LIMIT ?
        """

        # Execute the query with the top_n parameter as a tuple
        self.mycursor.execute(query, (top_n,))

        # Fetch the results
        top_students = self.mycursor.fetchall()
        print('did you execute up to here')

        return top_students

    def destroymain1(self):
        for frame in self.mainframe.winfo_children():
            frame.destroy()


    def main_Search(self):

        #create this function first after calling the command on the main search page
        def smallframe1but():

            #-------------OKAY BDOY STARTS HERE---------------
            #create the okay function after callin the command inside of the small frame window
            def okay():
                try:
                    self.selected_dept = comboDept1.get()
                    self.selected_level = combolevel.get()

                except Exception as e:

                    messagebox.showinfo('opps😯', 'data unavailable', parent=self.smallwindow)

                try:
                    #create the top student function outside  before calling it inside here
                    top_students = self.get_top_students(self.selected_level, self.selected_dept)

                    for i, student in enumerate(top_students, start=1):
                        matric_no, surname, name, dob, department, gender, level, grade, status, faculty, email, phone_no, time, date = student
                        if i == 1:
                            surname1 = surname
                            name1 = name
                            grade1 = grade
                            status1 = status
                            matric_no1 = matric_no
                        elif i == 2:
                            surname2 = surname
                            name2 = name
                            grade2 = grade
                            status2 = status
                            matric_no2 = matric_no
                        elif i == 3:
                            surname3 = surname
                            name3 = name
                            grade3 = grade
                            status3 = status
                            matric_no3 = matric_no



                    self.smallwindow.destroy()
                    self.destroymain1()

                    largeframeSmall1 = ctk.CTkFrame(self.mainframe, fg_color='#ECEBE9', width=1100,
                                                    height=680, corner_radius=10, border_color='#173662',
                                                    border_width=0)
                    largeframeSmall1.place(relx=0.008, rely=0.01)

                    Small0 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=500,
                                          height=20, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    # Small1.place(relx=0.23, rely=0.01)
                    Small0.pack(side=ctk.TOP, expand=True, fill=tk.Y)

                    Small1 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small1.place(relx=0.23, rely=0.01)
                    Small1.pack(padx=270, expand=True, ipadx=20, pady=10)

                    Back = ctk.CTkButton(largeframeSmall1, text='BACK', fg_color='#173662',
                                     text_color='white', height=35, width=80,
                                     font=('Ariel', 10, 'bold'), command=self.main_Search)
                    Back.place(relx=0.5, rely=0.5)
                    Back.pack(side=ctk.RIGHT, padx=5, pady=10)

                    Small2 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small2.place(relx=0.1, rely=0.04)
                    Small2.pack(side=ctk.LEFT, padx=10, expand=True, pady=5)

                    Small3 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small3.place(relx=0.03, rely=0.04)
                    Small3.pack(side=ctk.LEFT, padx=45, expand=True, pady=5)

                    label1 = tk.Label(Small1, image=self.smallframeimage3, bg='#ECEBE9')

                    label1.place(relx=0.35, rely=0.1)

                    label1head = tk.Label(Small1,
                                          text='FIRST BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label1head.place(relx=0.1, rely=0.25)

                    label1a = ctk.CTkLabel(Small1,
                                           text=f"Matric_no: {matric_no1}\nSurname: {surname1}\nName: {name1}\nCgpa: {status1}\nGrade: {grade1}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label1a.place(relx=0.1, rely=0.4)

                    # smalll2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
                    # text_color='#242818', fg_color='white', corner_radius=4)
                    # smalll2label2.place(relx=0.37, rely=0.1)

                    label2 = tk.Label(Small2, image=self.smallframeimage3, bg='#ECEBE9')

                    label2.place(relx=0.35, rely=0.1)

                    label2head = tk.Label(Small2,
                                          text='SECOND BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label2head.place(relx=0.1, rely=0.25)

                    label2a = ctk.CTkLabel(Small2,
                                           text=f"Matric_no: {matric_no2}\nSurname: {surname2}\nName: {name2}\nCgpa: {status2}\nGrade: {grade2}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label2a.place(relx=0.1, rely=0.4)

                    label3 = tk.Label(Small3, image=self.smallframeimage3, bg='#ECEBE9')

                    label3.place(relx=0.35, rely=0.1)

                    label3head = tk.Label(Small3,
                                          text='THIRD BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label3head.place(relx=0.1, rely=0.25)

                    label3a = ctk.CTkLabel(Small3,
                                           text=f"Matric_no: {matric_no3}\nSurname: {surname3}\nName: {name3}\nCgpa: {status3}\nGrade: {grade3}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label3a.place(relx=0.1, rely=0.4)

                    # print(f"Selected Department: {self.selected_dept}, Selected Level: {self.selected_level}")
                except Exception as e:
                    print(e)
                # -------------OKAY BDOY ENDS HERE---------------


            #------SMALL FROM FUNCTION BODY STARTS HERE-------

            self.smallwindow = tk.Tk()
            self.smallwindow.grab_set()
            self.smallwindow.title('School MAnagement System')
            self.smallwindow.geometry('400x250+600+200')
            self.smallwindow.config(bg='white')
            self.smallwindow.resizable(False, False)

            checkin = tk.Label(self.smallwindow, text='CHOOSE LEVEL & DEPT?',
                               font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
            checkin.grid(row=0, columnspan=3, padx=50, pady=20)

            deptvalues = ['COMPUTER SCIENCE', 'PUBLIC ADMIN', 'ACCOUNTING', 'SLT', 'BANKING', 'HMT']
            levelValues = ['ND 1', 'ND 2', 'HND 1', 'HND 2']

            deptlabel = tk.Label(self.smallwindow, text='Department:',
                                 font=('Ariel', 10,), bg='white', fg='#173662')
            deptlabel.grid(row=1, column=1, padx=10, pady=10)

            comboDept1 = ctk.CTkComboBox(self.smallwindow, values=deptvalues)
            comboDept1.set = ('select department')
            comboDept1.grid(row=1, column=2)

            levellabel = tk.Label(self.smallwindow, text='level:',
                                  font=('Ariel', 10,), bg='white', fg='#173662')
            levellabel.grid(row=2, column=1, padx=10, pady=10)

            combolevel = ctk.CTkComboBox(self.smallwindow, values=levelValues)
            combolevel.set = ('select level')
            combolevel.grid(row=2, column=2)



            OKbut = ctk.CTkButton(self.smallwindow, text='VIEW', fg_color='#173662',
                              text_color='white', height=35, width=80,
                              font=('Ariel', 15, 'bold'), command=okay)
            OKbut.grid(row=3, columnspan=4)

            # -------------SMALL FRAME BUT FUNCTION BODY ENDS HERE---------------


        def smallframe2but():
            def okay2():
                try:
                    self.selected_dept2 = comboDept.get()
                    #print(f"Selected Department: {self.selected_dept}, Selected Level: {self.selected_level}")
                except Exception as e:
                    print(f"Error: {str(e)}")
                top_students = self.get_top_students2(self.selected_dept2)
                try:
                    for i, student in enumerate(top_students, start=1):
                        matric_no, surname, name, dob, department, gender, level, grade, status, faculty, email, phone_no, time, date = student
                        if i == 1:
                            surname1 = surname
                            name1 = name
                            grade1 = grade
                            status1 = status
                            matric_no1 = matric_no
                        elif i == 2:
                            surname2 = surname
                            name2 = name
                            grade2 = grade
                            status2 = status
                            matric_no2 = matric_no
                        elif i == 3:
                            surname3 = surname
                            name3 = name
                            grade3 = grade
                            status3 = status
                            matric_no3 = matric_no



                    self.smallwindow.destroy()
                    self.destroymain1()

                    largeframeSmall1 = ctk.CTkFrame(self.mainframe, fg_color='#ECEBE9', width=1100,
                                                    height=680, corner_radius=10, border_color='#173662',
                                                    border_width=0)
                    largeframeSmall1.place(relx=0.008, rely=0.01)

                    Small0 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=500,
                                          height=20, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    # Small1.place(relx=0.23, rely=0.01)
                    Small0.pack(side=ctk.TOP, expand=True, fill=tk.Y)

                    Small1 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small1.place(relx=0.23, rely=0.01)
                    Small1.pack(padx=270, expand=True, ipadx=20, pady=10)

                    Back = ctk.CTkButton(largeframeSmall1, text='BACK', fg_color='#173662',
                                     text_color='white', height=35, width=80,
                                     font=('Ariel', 10, 'bold'), command=self.main_Search)
                    Back.place(relx=0.5, rely=0.5)
                    Back.pack(side=ctk.RIGHT, padx=5, pady=10)

                    Small2 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small2.place(relx=0.1, rely=0.04)
                    Small2.pack(side=ctk.LEFT, padx=10, expand=True, pady=5)

                    Small3 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small3.place(relx=0.03, rely=0.04)
                    Small3.pack(side=ctk.LEFT, padx=45, expand=True, pady=5)

                    label1 = tk.Label(Small1, image=self.smallframeimage3, bg='#ECEBE9')

                    label1.place(relx=0.35, rely=0.1)

                    label1head = tk.Label(Small1,
                                          text='FIRST BEST STUDENT5555',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label1head.place(relx=0.1, rely=0.25)

                    label1a = ctk.CTkLabel(Small1,
                                           text=f"Matric_no: {matric_no1}\nSurname: {surname1}\nName: {name1}\nCgpa: {status1}\nGrade: {grade1}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label1a.place(relx=0.1, rely=0.4)

                    # smalll2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
                    # text_color='#242818', fg_color='white', corner_radius=4)
                    # smalll2label2.place(relx=0.37, rely=0.1)

                    label2 = tk.Label(Small2, image=self.smallframeimage3, bg='#ECEBE9')

                    label2.place(relx=0.35, rely=0.1)

                    label2head = tk.Label(Small2,
                                          text='SECOND BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label2head.place(relx=0.1, rely=0.25)

                    label2a = ctk.CTkLabel(Small2,
                                           text=f"Matric_no: {matric_no2}\nSurname: {surname2}\nName: {name2}\nCgpa: {status2}\nGrade: {grade2}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label2a.place(relx=0.1, rely=0.4)

                    label3 = tk.Label(Small3, image=self.smallframeimage3, bg='#ECEBE9')

                    label3.place(relx=0.35, rely=0.1)

                    label3head = tk.Label(Small3,
                                          text='THIRD BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label3head.place(relx=0.1, rely=0.25)

                    label3a = ctk.CTkLabel(Small3,
                                           text=f"Matric_no: {matric_no3}\nSurname: {surname3}\nName: {name3}\nCgpa: {status3}\nGrade: {grade3}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label3a.place(relx=0.1, rely=0.4)
                except Exception as e:
                   print(e)


            self.smallwindow = tk.Tk()
            self.smallwindow.grab_set()
            self.smallwindow.title('School MAnagement System')
            self.smallwindow.geometry('400x250+600+200')
            self.smallwindow.config(bg='white')
            self.smallwindow.resizable(False, False)

            checkin = tk.Label(self.smallwindow, text='CHOOSE DEPARTMENT?',
                               font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
            checkin.grid(row=0, columnspan=3, padx=50, pady=20)

            deptvalues = ['COMPUTER SCIENCE', 'PUBLIC ADMIN', 'ACCOUNTING', 'SLT', 'BANKING', 'HMT']


            deptlabel = tk.Label(self.smallwindow, text='Department:',
                                 font=('Ariel', 10,), bg='white', fg='#173662')
            deptlabel.grid(row=1, column=1, padx=10, pady=10)

            comboDept = ctk.CTkComboBox(self.smallwindow, values=deptvalues)
            comboDept.set = ('select department')
            comboDept.grid(row=1, column=2)

            OKbut = ctk.CTkButton(self.smallwindow, text='VIEW', fg_color='#173662',
                              text_color='white', height=35, width=80,
                              font=('Ariel', 15, 'bold'), command=okay2)
            OKbut.grid(row=3, columnspan=4)

        def smallframe3but():
            def okay3():
                try:
                    self.selected_dept3 = comboDept.get()
                    #print(f"Selected Department: {self.selected_dept}, Selected Level: {self.selected_level}")
                except Exception as e:
                    print(f"Error: {str(e)}")
                top_students = self.get_top_students3(self.selected_dept3)
                try:
                    for i, student in enumerate(top_students, start=1):
                        matric_no, surname, name, dob, department, gender, level, grade, status, faculty, email, phone_no, time, date = student
                        if i == 1:
                            surname1 = surname
                            name1 = name
                            grade1 = grade
                            status1 = status
                            matric_no1 = matric_no
                        elif i == 2:
                            surname2 = surname
                            name2 = name
                            grade2 = grade
                            status2 = status
                            matric_no2 = matric_no
                        elif i == 3:
                            surname3 = surname
                            name3 = name
                            grade3 = grade
                            status3 = status
                            matric_no3 = matric_no



                    self.smallwindow.destroy()
                    self.destroymain1()

                    largeframeSmall1 = ctk.CTkFrame(self.mainframe, fg_color='#ECEBE9', width=1100,
                                                    height=680, corner_radius=10, border_color='#173662',
                                                    border_width=0)
                    largeframeSmall1.place(relx=0.008, rely=0.01)

                    Small0 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=500,
                                          height=20, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    # Small1.place(relx=0.23, rely=0.01)
                    Small0.pack(side=ctk.TOP, expand=True, fill=tk.Y)

                    Small1 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small1.place(relx=0.23, rely=0.01)
                    Small1.pack(padx=270, expand=True, ipadx=20, pady=10)

                    Back = ctk.CTkButton(largeframeSmall1, text='BACK', fg_color='#173662',
                                     text_color='white', height=35, width=80,
                                     font=('Ariel', 10, 'bold'), command=self.main_Search)
                    Back.place(relx=0.5, rely=0.5)
                    Back.pack(side=ctk.RIGHT, padx=5, pady=10)

                    Small2 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small2.place(relx=0.1, rely=0.04)
                    Small2.pack(side=ctk.LEFT, padx=10, expand=True, pady=5)

                    Small3 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                          height=300, corner_radius=10, border_color='#173662',
                                          border_width=0)
                    Small3.place(relx=0.03, rely=0.04)
                    Small3.pack(side=ctk.LEFT, padx=45, expand=True, pady=5)

                    label1 = tk.Label(Small1, image=self.smallframeimage3, bg='#ECEBE9')

                    label1.place(relx=0.35, rely=0.1)

                    label1head = tk.Label(Small1,
                                          text='FIRST BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label1head.place(relx=0.1, rely=0.25)

                    label1a = ctk.CTkLabel(Small1,
                                           text=f"Matric_no: {matric_no1}\nSurname: {surname1}\nName: {name1}\nCgpa: {status1}\nGrade: {grade1}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label1a.place(relx=0.1, rely=0.4)

                    # smalll2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
                    # text_color='#242818', fg_color='white', corner_radius=4)
                    # smalll2label2.place(relx=0.37, rely=0.1)

                    label2 = tk.Label(Small2, image=self.smallframeimage3, bg='#ECEBE9')

                    label2.place(relx=0.35, rely=0.1)

                    label2head = tk.Label(Small2,
                                          text='SECOND BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label2head.place(relx=0.1, rely=0.25)

                    label2a = ctk.CTkLabel(Small2,
                                           text=f"Matric_no: {matric_no2}\nSurname: {surname2}\nName: {name2}\nCgpa: {status2}\nGrade: {grade2}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label2a.place(relx=0.1, rely=0.4)

                    label3 = tk.Label(Small3, image=self.smallframeimage3, bg='#ECEBE9')

                    label3.place(relx=0.35, rely=0.1)

                    label3head = tk.Label(Small3,
                                          text='THIRD BEST STUDENT',
                                          bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

                    label3head.place(relx=0.1, rely=0.25)

                    label3a = ctk.CTkLabel(Small3,
                                           text=f"Matric_no: {matric_no3}\nSurname: {surname3}\nName: {name3}\nCgpa: {status3}\nGrade: {grade3}",
                                           fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

                    label3a.place(relx=0.1, rely=0.4)
                except Exception as e:
                   print(e)


            self.smallwindow = tk.Tk()
            self.smallwindow.grab_set()
            self.smallwindow.title('School MAnagement System')
            self.smallwindow.geometry('400x250+600+200')
            self.smallwindow.config(bg='white')
            self.smallwindow.resizable(False, False)

            checkin = tk.Label(self.smallwindow, text='CHOOSE DEPARTMENT?',
                               font=('Ariel', 15, 'bold'), bg='white', fg='#173662')
            checkin.grid(row=0, columnspan=3, padx=50, pady=20)

            deptvalues = ['COMPUTER SCIENCE', 'PUBLIC ADMIN', 'ACCOUNTING', 'SLT', 'BANKING', 'HMT']


            deptlabel = tk.Label(self.smallwindow, text='Department:',
                                 font=('Ariel', 10,), bg='white', fg='#173662')
            deptlabel.grid(row=1, column=1, padx=10, pady=10)

            comboDept = ctk.CTkComboBox(self.smallwindow, values=deptvalues)
            comboDept.set = ('select department')
            comboDept.grid(row=1, column=2)

            OKbut = ctk.CTkButton(self.smallwindow, text='VIEW', fg_color='#173662',
                              text_color='white', height=35, width=80,
                              font=('Ariel', 15, 'bold'), command=okay3)
            OKbut.grid(row=3, columnspan=4)


        def okay4():

            top_students = self.get_top_students4()

            for i, student in enumerate(top_students, start=1):
                matric_no, surname, name, dob, department, gender, level, grade, status, faculty, email, phone_no, time, date = student
                if i == 1:
                    surname1 = surname
                    name1 = name
                    grade1 = grade
                    status1 = status
                    matric_no1 = matric_no
                elif i == 2:
                    surname2 = surname
                    name2 = name
                    grade2 = grade
                    status2 = status
                    matric_no2 = matric_no
                elif i == 3:
                    surname3 = surname
                    name3 = name
                    grade3 = grade
                    status3 = status
                    matric_no3 = matric_no


            self.destroymain1()

            largeframeSmall1 = ctk.CTkFrame(self.mainframe, fg_color='#ECEBE9', width=1100,
                                            height=680, corner_radius=10, border_color='#173662',
                                            border_width=0)
            largeframeSmall1.place(relx=0.008, rely=0.01)

            Small0 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=500,
                                  height=20, corner_radius=10, border_color='#173662',
                                  border_width=0)
            # Small1.place(relx=0.23, rely=0.01)
            Small0.pack(side=ctk.TOP, expand=True, fill=tk.Y)

            Small1 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small1.place(relx=0.23, rely=0.01)
            Small1.pack(padx=270, expand=True, ipadx=20, pady=10)

            Back = ctk.CTkButton(largeframeSmall1, text='BACK', fg_color='#173662',
                             text_color='white', height=35, width=80,
                             font=('Ariel', 10, 'bold'), command=self.main_Search)
            Back.place(relx=0.5, rely=0.5)
            Back.pack(side=ctk.RIGHT, padx=5, pady=10)

            Small2 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small2.place(relx=0.1, rely=0.04)
            Small2.pack(side=ctk.LEFT, padx=10, expand=True, pady=5)

            Small3 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small3.place(relx=0.03, rely=0.04)
            Small3.pack(side=ctk.LEFT, padx=45, expand=True, pady=5)

            label1 = tk.Label(Small1, image=self.smallframeimage3, bg='#ECEBE9')

            label1.place(relx=0.35, rely=0.1)

            label1head = tk.Label(Small1,
                                  text='FIRST BEST STUDENT',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label1head.place(relx=0.1, rely=0.25)

            label1a = ctk.CTkLabel(Small1,
                                   text=f"Matric_no: {matric_no1}\nSurname: {surname1}\nName: {name1}\nCgpa: {status1}\nGrade: {grade1}",
                                   fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

            label1a.place(relx=0.1, rely=0.4)

            # smalll2label2 = ctk.CTkLabel(self.smallframe2, text='Lecturers', font=('Ariel', 10),
            # text_color='#242818', fg_color='white', corner_radius=4)
            # smalll2label2.place(relx=0.37, rely=0.1)

            label2 = tk.Label(Small2, image=self.smallframeimage3, bg='#ECEBE9')

            label2.place(relx=0.35, rely=0.1)

            label2head = tk.Label(Small2,
                                  text='SECOND BEST STUDENTuuyt',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label2head.place(relx=0.1, rely=0.25)

            label2a = ctk.CTkLabel(Small2,
                                   text=f"Matric_no: {matric_no2}\nSurname: {surname2}\nName: {name2}\nCgpa: {status2}\nGrade: {grade2}",
                                   fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

            label2a.place(relx=0.1, rely=0.4)

            label3 = tk.Label(Small3, image=self.smallframeimage3, bg='#ECEBE9')

            label3.place(relx=0.35, rely=0.1)

            label3head = tk.Label(Small3,
                                  text='THIRD BEST STUDENT',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label3head.place(relx=0.1, rely=0.25)

            label3a = ctk.CTkLabel(Small3,
                                   text=f"Matric_no: {matric_no3}\nSurname: {surname3}\nName: {name3}\nCgpa: {status3}\nGrade: {grade3}",
                                   fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

            label3a.place(relx=0.1, rely=0.4)

        def okay5():
            self.destroymain1()

            self.smallokay5img = Image.open('images/medal-of-honor.png')

            self.smallokay5img = ImageTk.PhotoImage(self.smallokay5img)

            largeframeSmall1 = ctk.CTkFrame(self.mainframe, fg_color='#ECEBE9', width=1100,
                                            height=680, corner_radius=10, border_color='#173662',
                                            border_width=0)
            largeframeSmall1.place(relx=0.008, rely=0.01)

            Small0 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=500,
                                  height=20, corner_radius=10, border_color='#173662',
                                  border_width=0)
            # Small1.place(relx=0.23, rely=0.01)
            Small0.pack(side=ctk.TOP, expand=True, fill=tk.Y)

            Small1 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small1.place(relx=0.23, rely=0.01)
            Small1.pack(padx=270, expand=True, ipadx=20, pady=10)

            Back = ctk.CTkButton(largeframeSmall1, text='BACK', fg_color='#173662',
                             text_color='white', height=35, width=80,
                             font=('Ariel', 10, 'bold'), command=self.main_Search)
            Back.place(relx=0.5, rely=0.5)
            Back.pack(side=ctk.RIGHT, padx=5, pady=10)

            Small2 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small2.place(relx=0.1, rely=0.04)
            Small2.pack(side=ctk.LEFT, padx=10, expand=True, pady=5)

            Small3 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small3.place(relx=0.03, rely=0.04)
            Small3.pack(side=ctk.LEFT, padx=45, expand=True, pady=5)

            label1 = tk.Label(Small1, image=self.smallokay5img, bg='#ECEBE9')

            label1.place(relx=0.32, rely=0.01)

            label1head = tk.Label(Small1,
                                  text='TOP ACHEIVER 1',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label1head.place(relx=0.1, rely=0.25)

            label1a = ctk.CTkLabel(Small1,
                                   text=' Matric_no: N/cs/22/4564\nSurname: Kunle\nName: Bola\nCgpa: 4.96\nGrade: Distinction',
                                   fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

            label1a.place(relx=0.1, rely=0.4)



            label2 = tk.Label(Small2, image=self.smallokay5img, bg='#ECEBE9')

            label2.place(relx=0.32, rely=0.01)

            label2head = tk.Label(Small2,
                                  text='TOP ACHEIVER 2',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label2head.place(relx=0.1, rely=0.25)

            label2a = ctk.CTkLabel(Small2,
                                   text=' Matric_no: N/cs/22/4564\nSurname: Kunle\nName: Bola\nCgpa: 4.96\nGrade: Distinction',
                                   fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

            label2a.place(relx=0.1, rely=0.4)

            label3 = tk.Label(Small3, image=self.smallokay5img, bg='#ECEBE9')

            label3.place(relx=0.32, rely=0.01)

            label3head = tk.Label(Small3,
                                  text='TOP ACHIEVER 3',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label3head.place(relx=0.1, rely=0.25)

            label3a = ctk.CTkLabel(Small3,
                                   text=' Matric_no: N/cs/22/4564\nSurname: Kunle\nName: Bola\nCgpa: 4.96\nGrade: Distinction',
                                   fg_color='white', text_color='black', font=('Ariel', 20), corner_radius=5)

            label3a.place(relx=0.1, rely=0.4)

        def okay6():

            self.destroymain1()

            self.smallokay6img = Image.open('images/trophy.png')

            self.smallokay6img = ImageTk.PhotoImage(self.smallokay6img)

            largeframeSmall1 = ctk.CTkFrame(self.mainframe, fg_color='#ECEBE9', width=1100,
                                            height=680, corner_radius=10, border_color='#173662',
                                            border_width=0)
            largeframeSmall1.place(relx=0.008, rely=0.01)

            Small0 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=500,
                                  height=20, corner_radius=10, border_color='#173662',
                                  border_width=0)
            # Small1.place(relx=0.23, rely=0.01)
            Small0.pack(side=ctk.TOP, expand=True, fill=tk.Y)

            Small1 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small1.place(relx=0.23, rely=0.01)
            Small1.pack(padx=270, expand=True, ipadx=20, pady=10)

            Back = ctk.CTkButton(largeframeSmall1, text='BACK', fg_color='#173662',
                             text_color='white', height=35, width=80,
                             font=('Ariel', 10, 'bold'), command=self.main_Search)
            Back.place(relx=0.5, rely=0.5)
            Back.pack(side=ctk.RIGHT, padx=5, pady=10)

            Small2 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small2.place(relx=0.1, rely=0.04)
            Small2.pack(side=ctk.LEFT, padx=10, expand=True, pady=5)

            Small3 = ctk.CTkFrame(largeframeSmall1, fg_color='#ECEBE9', width=400,
                                  height=300, corner_radius=10, border_color='#173662',
                                  border_width=0)
            Small3.place(relx=0.03, rely=0.04)
            Small3.pack(side=ctk.LEFT, padx=45, expand=True, pady=5)

            label1 = tk.Label(Small1, image=self.smallokay6img, bg='#ECEBE9')

            label1.place(relx=0.32, rely=0.01)

            label1head = tk.Label(Small1,
                                  text='DISTINGUISHED PROFESSORS',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label1head.place(relx=0.08, rely=0.25)

            label1a = ctk.CTkLabel(Small1,
                                   text=' Number of Award: 6\nIssued by: ECOWAS\nCategory: International\nYear: 1996,98,99,2005,14,24\nType: Academics Award',
                                   fg_color='white', text_color='#173662', font=('Ariel', 20), corner_radius=5)

            label1a.place(relx=0.1, rely=0.4)



            label2 = tk.Label(Small2, image=self.smallokay6img, bg='#ECEBE9')

            label2.place(relx=0.32, rely=0.01)

            label2head = tk.Label(Small2,
                                  text='BEST UNIVERSITY AWARD ',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label2head.place(relx=0.1, rely=0.25)

            label2a = ctk.CTkLabel(Small2,
                                   text=' Number of Award: 4\nIssued by: Academic Board Nigeria\nCategory: National\n Year: 2007,9,15,24\n Type: Academics Award',
                                   fg_color='white', text_color='#173662', font=('Ariel', 20), corner_radius=5)

            label2a.place(relx=0.1, rely=0.4)

            label3 = tk.Label(Small3, image=self.smallokay6img, bg='#ECEBE9')

            label3.place(relx=0.32, rely=0.01)

            label3head = tk.Label(Small3,
                                  text='STAR GOLD MEDAL',
                                  bg='#ECEBE9', fg='#173662', font=('helvetica', 18))

            label3head.place(relx=0.1, rely=0.25)

            label3a = ctk.CTkLabel(Small3,
                                   text=' Number of Award: 2\nIssued by: Nigeria Football Federation\nCategory: National\nYear: 2014,15\n Type: Sport Award',
                                   fg_color='white', text_color='#173662', font=('Ariel', 20), corner_radius=5)

            label3a.place(relx=0.1, rely=0.4)



        #-------MAIN SEARCH BODY----------------
        self.destroymain()
        self.button_search.configure(fg_color='#276878')

        self.largeframesearch = ctk.CTkFrame(self.mainframe, fg_color='#ECEBE9', width=1050,
                                             height=680, corner_radius=10, border_color='#173662',
                                             border_width=0)
        self.largeframesearch.place(relx=0.008, rely=0.01)

        self.labelsearching = ctk.CTkLabel(self.largeframesearch, text='MAKE A QUICK SEARCH',
                                           image=ctk.CTkImage(self.icon_Butreg), compound=tk.LEFT,
                                           fg_color='transparent', font=('Helvetica', 25), text_color='#173662',
                                           corner_radius=10)
        self.labelsearching.grid(row=1, column=1, pady=15, sticky='w')

        smallframe1 = ctk.CTkFrame(self.largeframesearch, fg_color='#CCE0FE', width=320,
                                   height=250, corner_radius=10,
                                   )

        smallframe1.grid(row=2, column=1, pady=20, sticky='w')

        smallframe2 = ctk.CTkFrame(self.largeframesearch, fg_color='#FAE8ED', width=320,
                                   height=250, corner_radius=10,
                                   )

        smallframe2.grid(row=2, column=2, pady=20, padx=30, sticky='w')

        smallframe3 = ctk.CTkFrame(self.largeframesearch, fg_color='#FFF5FD', width=320,
                                   height=250, corner_radius=10,
                                   )

        smallframe3.grid(row=2, column=3, pady=20, sticky='w')

        smallframe4 = ctk.CTkFrame(self.largeframesearch, fg_color='#BCA0DC', width=320,
                                   height=250, corner_radius=10,
                                   )

        smallframe4.grid(row=3, column=1, pady=15, sticky='w')

        smallframe5 = ctk.CTkFrame(self.largeframesearch, fg_color='#f0e2d2', width=320,
                                   height=250, corner_radius=10,
                                   )

        smallframe5.grid(row=3, column=2, pady=15, padx=30, sticky='w')

        smallframe6 = ctk.CTkFrame(self.largeframesearch, fg_color='grey', width=320,
                                   height=250, corner_radius=10,
                                   )

        smallframe6.grid(row=3, column=3, pady=15, sticky='w')

        # LABEL ON FRAME
        smallframe1label = ctk.CTkLabel(smallframe1, text='BEST STUDENT LEVEL',
                                        image=ctk.CTkImage(self.icon_Butreg), compound=tk.LEFT,
                                        fg_color='transparent', font=('Helvetica', 18, 'bold'), text_color='#173662',
                                        corner_radius=10, )
        smallframe1label.place(relx=0.1, rely=0.2)

        smallframe1button = ctk.CTkButton(smallframe1, text='VIEW', fg_color='white',
                                      text_color='#173662', height=35, width=80,
                                      font=('Ariel', 10, 'bold'),command=smallframe1but)#create command=smallframe1but later and call
        smallframe1button.place(relx=0.5, rely=0.7)

        smallframe2label = ctk.CTkLabel(smallframe2, text='BEST STUDENT DEPT',
                                        image=ctk.CTkImage(self.image_butreg), compound=tk.LEFT,
                                        fg_color='transparent', font=('Helvetica', 18, 'bold'), text_color='#173662',
                                        corner_radius=10, )
        smallframe2label.place(relx=0.1, rely=0.2)

        smallframe2button = ctk.CTkButton(smallframe2, text='VIEW', fg_color='white',
                                      text_color='#173662', height=35, width=80,
                                      font=('Ariel', 10, 'bold'), )
        smallframe2button.place(relx=0.5, rely=0.7)

        smallframe3label = ctk.CTkLabel(smallframe3, text='BEST STUDENT FACULTY',
                                        image=ctk.CTkImage(self.image_butreg), compound=tk.LEFT,
                                        fg_color='transparent', font=('Helvetica', 18, 'bold'), text_color='#173662',
                                        corner_radius=10, )
        smallframe3label.place(relx=0.1, rely=0.2)

        smallframe3button = ctk.CTkButton(smallframe3, text='VIEW', fg_color='white',
                                      text_color='#173662', height=35, width=80,
                                      font=('Ariel', 10, 'bold'))
        smallframe3button.place(relx=0.5, rely=0.7)

        smallframe4label = ctk.CTkLabel(smallframe4, text='OVERALL BEST IN SCHOOL',
                                        image=ctk.CTkImage(self.image_butreg), compound=tk.LEFT,
                                        fg_color='transparent', font=('Helvetica', 18, 'bold'), text_color='#173662',
                                        corner_radius=10, )
        smallframe4label.place(relx=0.1, rely=0.2)

        smallframe4button = ctk.CTkButton(smallframe4, text='VIEW', fg_color='white',
                                      text_color='#173662', height=35, width=80,
                                      font=('Ariel', 10, 'bold'))
        smallframe4button.place(relx=0.5, rely=0.7)

        smallframe5label = ctk.CTkLabel(smallframe5, text='TOP ACHIEVERS',
                                        image=ctk.CTkImage(self.image_butreg), compound=tk.LEFT,
                                        fg_color='transparent', font=('Helvetica', 18, 'bold'), text_color='#173662',
                                        corner_radius=10, )
        smallframe5label.place(relx=0.3, rely=0.2)

        smallframe5button = ctk.CTkButton(smallframe5, text='VIEW', fg_color='white',
                                      text_color='#173662', height=35, width=80,
                                      font=('Ariel', 10, 'bold'))
        smallframe5button.place(relx=0.5, rely=0.7)

        smallframe6label = ctk.CTkLabel(smallframe6, text='AWARDS & MERITS',
                                        image=ctk.CTkImage(self.icon_Butreg), compound=tk.LEFT,
                                        fg_color='transparent', font=('Helvetica', 18, 'bold'), text_color='#173662',
                                        corner_radius=10, )
        smallframe6label.place(relx=0.3, rely=0.2)

        smallframe6button = ctk.CTkButton(smallframe6, text='VIEW', fg_color='white',
                                      text_color='#173662', height=35, width=80,
                                      font=('Ariel', 10, 'bold'))
        smallframe6button.place(relx=0.5, rely=0.7)



    def record(self):
        self.destroymain()
        self.button_record.configure(fg_color='#276878')

        self.largeframerecord = ctk.CTkFrame(self.mainframe, fg_color='#ECEBE9', width=1400,
                                       height=680, corner_radius=10, border_color='#173662',
                                       border_width=0)
        self.largeframerecord.place(relx=0.5, rely=0.5)
        self.largeframerecord.pack(pady=0, padx=0, fill=ctk.BOTH)

        self.treeframe2 = tk.Frame(self.largeframerecord, bg='black', width=100,
                                  height=680)
        self.treeframe2.pack(pady=5, padx=10, side=ctk.RIGHT)

        scrollbarX = tk.Scrollbar(self.treeframe2, orient=ctk.HORIZONTAL)
        scrollbarY = tk.Scrollbar(self.treeframe2, orient=ctk.VERTICAL)

        style = tk.Style(self.treeframe2)
        style.theme_use('clam')
        style.configure('Treeview', font=('Arial', 10), foreground='#173662', background='white',
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', '#173662')])

        style.configure('Treeview.Heading', font=('Arial', 10,), background='#173662', foreground='white')

        # Create Treeview widget
        self.tree = tk.Treeview(self.treeframe2, height=30, xscrollcommand=scrollbarX.set,
                                 yscrollcommand=scrollbarY.set,
                                 columns=('Matric', 'Surname', 'Name', 'DOB', 'Department', 'Gender', 'Level',
                                          'Grade', 'Cgpa', 'Faculty', 'Email',
                                          'Phone_No', 'Time', 'Date'), show='headings')
        self.tree.column('#0', width=100)

        scrollbarX.configure(command=self.tree.xview)
        scrollbarY.configure(command=self.tree.yview)
        scrollbarX.pack(side=tk.BOTTOM, fill=tk.X)
        scrollbarY.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Define columns and set their properties
        columns = ['Matric', 'Surname', 'Name', 'DOB', 'Department', 'Gender', 'Level',
                   'Grade', 'Cgpa', 'Faculty', 'Email',
                   'Phone_No', 'Time', 'Date']
        for col in columns:
            self.tree.heading(col, text=col, )
            self.tree.column(col, width=150, anchor='center')

        query = 'select *from student'
        self.mycursor.execute(query)
        self.fecthed_data = self.mycursor.fetchall()
        self.tree.delete(*self.tree.get_children())
        for data in self.fecthed_data:
            datalist = list(data)
            self.tree.insert('', END, values=datalist)










    def start(self):
        self.Splashwindow.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
