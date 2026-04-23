from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root

        # Get screen dimensions and set window size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set window size to 95% of screen or max 1500x800
        window_width = min(int(screen_width * 0.95), 1500)
        window_height = min(int(screen_height * 0.95), 800)

        # Center the window
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.root.title("STUDENT REGISTRATION SYSTEM")
        self.root.resizable(True, True)

        # variables
        self.var_enrollment = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_department = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_section = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()

        # Create main frame with scrollbar
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=True)

        # Create a canvas for scrolling
        self.canvas = Canvas(self.main_frame)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add scrollbar to the canvas
        scrollbar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold all widgets
        self.inner_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Bind the canvas to the scroll region
        self.inner_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Bind mousewheel to scroll
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # Load all images first to prevent flickering
        self.load_images(window_width, window_height)

        # Create the UI elements
        self.create_ui()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def load_images(self, window_width, window_height):
        """Pre-load all images to prevent flickering during scrolling"""
        # 1st image
        img = Image.open(r'./college_images/mits.png')
        img = img.resize((window_width, 170), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Background image
        img_4 = Image.open(r'./college_images/university.png')
        img_4 = img_4.resize((window_width, window_height - 170), Image.Resampling.LANCZOS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        # Left frame image
        img_5 = Image.open(r'./college_images/university.png')
        img_5 = img_5.resize((int(window_width * 1), 400), Image.Resampling.LANCZOS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        # Right frame image
        img_7 = Image.open(r'./college_images/5th.jpeg')
        img_7 = img_7.resize((int(window_width * 1), 400), Image.Resampling.LANCZOS)
        self.photoimg_7 = ImageTk.PhotoImage(img_7)

    def create_ui(self):
        """Create all UI elements in the inner frame"""
        # 1st image (top banner)
        self.button1 = Button(self.inner_frame, image=self.photoimg, cursor="hand2", borderwidth=0)
        self.button1.pack(fill=X)

        # Background frame (contains everything else)
        bg_frame = Frame(self.inner_frame)
        bg_frame.pack(fill=BOTH, expand=True)

        # Background image label (behind everything)
        bg_label = Label(bg_frame, image=self.photoimg_4, borderwidth=0)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title label
        label_title = Label(bg_frame, text="STUDENT REGISTRATION SYSTEM",
                           font=("Arial", 30, "bold"),
                           fg="blue", bg="yellow")
        label_title.pack(fill=X, pady=(0, 10))

        # Main content frame (manages left and right frames)
        manage_frame = Frame(bg_frame, bd=2, relief=RIDGE, bg="green")
        manage_frame.pack(fill=BOTH, expand=True, padx=15, pady=5)

        # Left frame (student information)
        left_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2,
                              text="Student Information",
                              font=("Arial", 12, "bold"),
                              fg="red", bg="blue")
        left_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Left frame image
        my_label = Label(left_frame, image=self.photoimg_5, bd=2, relief=RIDGE)
        my_label.pack(fill=X, padx=5, pady=5)

        # Current course information frame
        student_info_frame = LabelFrame(left_frame, bd=4, relief=RIDGE, padx=2,
                                       text="Current Course Information",
                                       font=("Arial", 12, "bold"),
                                       fg="red", bg="green")
        student_info_frame.pack(fill=X, padx=5, pady=5)

        # Course row
        course_label = Label(student_info_frame, text="Course",
                            font=("Arial", 12, "bold"), bg="yellow")
        course_label.grid(row=0, column=0, padx=2, pady=10, sticky=W)

        course_combo = ttk.Combobox(student_info_frame, textvariable=self.var_course,
                                   font=("Arial", 12, "bold"),
                                   width=17, state="readonly")
        course_combo["value"] = ("Select Courses","BS","B.SC", "B.E/B.Tech", "BBA", "MBA", "MDCAT", "DPT", "PHARMACY")
        course_combo.current(0)
        course_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Department drop box
        department_label = Label(student_info_frame, text="Department",
                                font=("Arial", 12, "bold"), bg="yellow")
        department_label.grid(row=0, column=2, padx=2, sticky=W)

        department_combo = ttk.Combobox(student_info_frame, textvariable=self.var_department,
                                      font=("Arial", 12, "bold"), width=17, state="readonly")
        department_combo["value"] = (
            "Select Department", "Computer Science And Engineering", "Computer Science And Design",
            "Information Technology", "Artificial Intelligence And Machine Learning",
            "Artificial Intelligence And Data Science", "Artificial Intelligence And Robotics",
            "Electrical Engineering",
            "Internet Of Things Offered By Electrical Engineering Department",
            "Internet Of Things Offered By Information Technology", "Mathematics And Computing",
            "Autombile Engineering",
            "Electronics And TeleCommunication", "Chemical Engineering", "Architecture", "Electronics Engineering",
            "Civil Engineering Department", "Mechanical Engineering")
        department_combo.current(0)
        department_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        current_year = Label(student_info_frame, text="Year:",
                           font=("Arial", 12, "bold"), bg="yellow")
        current_year.grid(row=1, column=0, padx=2, sticky=W)

        current_year_combo = ttk.Combobox(student_info_frame, textvariable=self.var_year,
                                        font=("Arial", 12, "bold"),
                                        width=17, state="readonly")
        current_year_combo["value"] = ("Select Your Current Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        current_year_combo.current(0)
        current_year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Current semester
        current_semester = Label(student_info_frame, text="Semester:",
                               font=("Arial", 12, "bold"), bg="yellow")
        current_semester.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        current_semester_combo = ttk.Combobox(student_info_frame, textvariable=self.var_semester,
                                            font=("Arial", 12, "bold"), width=17, state="readonly")
        current_semester_combo["value"] = (
            "Select Your Current Semester", "1st Semester", "2nd Semester", "3rd Semester", "4th Semester",
            "5th Semester", "6th Semester", "7th Semester", "8th Semester")
        current_semester_combo.current(0)
        current_semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Student class information frame
        student_class = LabelFrame(left_frame, bd=4, relief=RIDGE, padx=2,
                                 text="Student Class Information",
                                 font=("Arial", 12, "bold"),
                                 fg="red", bg="skyblue")
        student_class.pack(fill=X, padx=5, pady=5)

        # Student name
        student_name = Label(student_class, text="Student Name: ",
                           font=("Arial", 12, "bold"), bg="orange")
        student_name.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        name_entry = ttk.Entry(student_class, textvariable=self.var_name,
                             font=("Arial", 12, "bold"), width=15)
        name_entry.grid(row=0, column=1, sticky=W, padx=2, pady=7)

        # Student id
        student_id = Label(student_class, text="Enrollment",
                          font=("Arial", 12, "bold"), bg="orange")
        student_id.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        id_entry = ttk.Entry(student_class, textvariable=self.var_enrollment,
                           font=("Arial", 12, "bold"),
                           width=15)
        id_entry.grid(row=0, column=3, sticky=W, padx=2, pady=7)

        # Sections
        class_section = Label(student_class, text="Section: ",
                            font=("Arial", 12, "bold"), bg="orange")
        class_section.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        section_entry = ttk.Combobox(student_class, textvariable=self.var_section, state="readonly",
                                   font=("Arial", 10, "bold"), width=18)
        section_entry["values"] = ("Select Your Branch Section", "RED", "Blue", "Green")
        section_entry.current(0)
        section_entry.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        # Gender
        student_gender = Label(student_class, text="Gender:",
                             font=("Arial", 10, "bold"), bg="orange")
        student_gender.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        gender_combo = ttk.Combobox(student_class, textvariable=self.var_gender, state="readonly",
                                   font=("Arial", 10, "bold"), width=19)
        gender_combo["values"] = ("Select Your Gender", "Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, sticky=W, padx=2, pady=7)

        # DOB
        student_dob = Label(student_class, text="DOB:",
                          font=("Arial", 12, "bold"), bg="orange")
        student_dob.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        dob_entry = ttk.Entry(student_class, textvariable=self.var_dob,
                            font=("Arial", 12, "bold"), width=15)
        dob_entry.grid(row=2, column=1, sticky=W, padx=2, pady=7)

        # Mobile number
        student_mobile = Label(student_class, text="Phone",
                             font=("Arial", 12, "bold"), bg="orange")
        student_mobile.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        num_entry = ttk.Entry(student_class, textvariable=self.var_phone,
                            font=("Arial", 12, "bold"), width=16)
        num_entry.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # Email
        student_email = Label(student_class, text="Email I'D:",
                           font=("Arial", 12, "bold"), bg="orange")
        student_email.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        email_entry = ttk.Entry(student_class, textvariable=self.var_email,
                             font=("calbri", 12, "bold"), width=15)
        email_entry.grid(row=3, column=1, sticky=W, padx=2, pady=7)

        # Address
        student_address = Label(student_class, text="Address:",
                             font=("Arial", 12, "bold"), bg="orange")
        student_address.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        address_entry = ttk.Entry(student_class, textvariable=self.var_address,
                               font=("Arial", 12, "bold"),
                               width=15)
        address_entry.grid(row=3, column=3, sticky=W, padx=2, pady=7)

        # Button frame
        button_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.pack(fill=X, padx=5, pady=5)

        button_add = Button(button_frame, text="Save", command=self.add_data,
                          font=("arial", 14, "bold"), width=13,
                          bg="blue", fg="white")
        button_add.grid(row=0, column=0, padx=1)

        button_update = Button(button_frame, text="Update", command=self.update_data,
                             font=("arial", 14, "bold"),
                             width=13, bg="blue", fg="white")
        button_update.grid(row=0, column=1, padx=1)

        button_del = Button(button_frame, text="Delete", command=self.delete_data,
                          font=("arial", 14, "bold"), width=13,
                          bg="blue", fg="white")
        button_del.grid(row=0, column=2, padx=1)

        button_reset = Button(button_frame, text="Reset", command=self.reset_data,
                            font=("arial", 14, "bold"), width=12,
                            bg="blue", fg="white")
        button_reset.grid(row=0, column=3, padx=1)

        # Right frame (student details) - now placed below left frame
        right_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2,
                               text="Student Details",
                               font=("Arial", 12, "bold"),
                               fg="red", bg="blue")
        right_frame.pack(fill=BOTH, expand=True, padx=10, pady=(0, 10))  # Added pady to create space

        # Right frame image
        right_img = Label(right_frame, image=self.photoimg_7, bd=2, relief=RIDGE)
        right_img.pack(fill=X, padx=5, pady=5)

        # Search frame
        search_frame = LabelFrame(right_frame, bd=4, relief=RIDGE, padx=2,
                                text="Search Student Information",
                                font=("Arial", 12, "bold"),
                                fg="red", bg="green")
        search_frame.pack(fill=X, padx=5, pady=5)

        search_label = Label(search_frame, font=("arial", 14, "bold"),
                           text="Search By: ", width=12, bg="yellow",
                           fg="blue")
        search_label.grid(row=0, column=0, padx=5, sticky=W)

        # Search
        self.var_combo_search = StringVar()

        search_combo = ttk.Combobox(search_frame, textvariable=self.var_combo_search, state="readonly",
                                   font=("Arial", 10, "bold"), width=19)
        search_combo["values"] = ("Select Option", "Enrollment", "Phone", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()

        search_entry = ttk.Entry(search_frame, textvariable=self.var_search,
                               font=("Arial", 12, "bold"),
                               width=15)
        search_entry.grid(row=0, column=2, sticky=W, padx=5)

        button_search = Button(search_frame, text="Search", command=self.search_data,
                             font=("arial", 14, "bold"),
                             width=11, bg="blue", fg="white")
        button_search.grid(row=0, column=3, padx=5)

        button_ShowAll = Button(search_frame, command=self.fetch_data, text="Show All",
                              font=("arial", 14, "bold"),
                              width=10, bg="blue", fg="white")
        button_ShowAll.grid(row=0, column=4, padx=5)

        # Student table and scroll bar
        table_frame = Frame(right_frame, bd=4, relief=RIDGE)
        table_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            "Enrollment", "Name", "Course", "Department", "Year", "Semester", "Section", "Gender", "Dob", "Phone",
            "Email", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Enrollment", text="Enrollment")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Section", text="Section")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Dob", text="DOB")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Address", text="Address")

        self.student_table["show"] = "headings"

        self.student_table.column("Enrollment", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Department", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Section", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Dob", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Address", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    def add_data(self):
        if (self.var_enrollment.get() == "" or self.var_name.get() == "" or self.var_course.get() == ""):
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="426920aa",
                                               database="student_management_system")
                my_cursur = conn.cursor()
                my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.var_enrollment.get(),
                                   self.var_name.get(),
                                   self.var_course.get(),
                                   self.var_department.get(),
                                   self.var_year.get(),
                                   self.var_semester.get(),
                                   self.var_section.get(),
                                   self.var_gender.get(),
                                   self.var_dob.get(),
                                   self.var_phone.get(),
                                   self.var_email.get(),
                                   self.var_address.get()
                                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Registration Successfull", "Student Has Been Successfully Registered...",
                                    parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="426920aa",
                                       database="student_management_system",
                                       port="3306")
        my_cursur = conn.cursor()
        my_cursur.execute("select * from student order by Enrollment")
        data = my_cursur.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]

        self.var_enrollment.set(data[0])
        self.var_name.set(data[1])
        self.var_course.set(data[2])
        self.var_department.set(data[3])
        self.var_year.set(data[4])
        self.var_semester.set(data[5])
        self.var_section.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_phone.set(data[9])
        self.var_email.set(data[10])
        self.var_address.set(data[11])

    def update_data(self):
        if (self.var_enrollment.get() == "" or self.var_name.get() == "" or self.var_course.get() == ""):
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                update = messagebox.askyesno("Update", "Are You Sure To Update This Student Information ?",
                                             parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="426920aa",
                                                   database="student_management_system")
                    my_cursur = conn.cursor()
                    my_cursur.execute(
                        "update student set Name=%s,Course=%s,Department=%s,Year=%s,Semester=%s,Section=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Address=%s where Enrollment=%s",
                        (self.var_name.get(),
                         self.var_course.get(),
                         self.var_department.get(),
                         self.var_year.get(),
                         self.var_semester.get(),
                         self.var_section.get(),
                         self.var_gender.get(),
                         self.var_dob.get(),
                         self.var_phone.get(),
                         self.var_email.get(),
                         self.var_address.get(),
                         self.var_enrollment.get()
                         ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Succesfull", "Student Information Updated Successfull.....", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_enrollment.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                Delete = messagebox.askyesno("Delete", "Are You Sure Want To Delete This Student ?")
                if Delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="426920aa",
                                                   database="student_management_system")
                    my_cursur = conn.cursor()
                    sql = "delete from student where Enrollment=%s"
                    value = (self.var_enrollment.get(),)
                    my_cursur.execute(sql, value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Your Student Information Has Been Deleted...", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_enrollment.set("")
        self.var_name.set("")
        self.var_course.set("Select Course")
        self.var_department.set("Select Department")
        self.var_year.set("Select Your Current Year")
        self.var_semester.set("Select Your Current Semester")
        self.var_section.set("Select Your Branch Section")
        self.var_gender.set("Select Your Gender")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_address.set("")

    def search_data(self):
        if self.var_combo_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please Select Option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="426920aa",
                                               database="student_management_system")
                my_cursur = conn.cursor()
                my_cursur.execute("Select * From Student where " + str(self.var_combo_search.get()) + " LIKE '%" + str(
                    self.var_search.get()) + "%'")
                data = my_cursur.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()