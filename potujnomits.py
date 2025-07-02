import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, Image

class PotuzhnomirApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Потужномір")
        self.geometry("600x450")
        self.resizable(False, False)

        self.original_bg_image = Image.open("/home/excalibur/Загрузки/ukr.png").resize((600, 450))
        self.original_bg_photo = ImageTk.PhotoImage(self.original_bg_image)

        self.background_label = tk.Label(self, image=self.original_bg_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure("blue.Horizontal.TProgressbar", troughcolor='#222222', bordercolor='#222222',
                        background='#00aaff', lightcolor='#66ccff', darkcolor='#0088cc', thickness=25)
        self.progress_style = "blue.Horizontal.TProgressbar"
        self.red_progress_style = "red.Horizontal.TProgressbar"
        style.configure(self.red_progress_style, troughcolor='#660000', background='#ff0000', thickness=25)

        self.progress = ttk.Progressbar(self, orient="horizontal", length=400,
                                        mode="determinate", style=self.progress_style)
        self.progress.place(x=100, y=350)

        self.power_label = tk.Label(self, text="Потужність: 0%", font=("Segoe UI", 20, "bold"),
                                    fg="white", bg="#000000")
        self.power_label.place(relx=0.5, y=390, anchor="center")

        self.measure_button = tk.Label(self,
                                       text="Міряти",
                                       font=("Segoe UI", 20, "bold"),
                                       fg="white",
                                       bg="#00aaff",
                                       width=12,
                                       height=1,
                                       cursor="hand2",
                                       relief="raised",
                                       bd=4)
        self.measure_button.place(relx=0.5, y=430, anchor="center")
        self.measure_button.bind("<Button-1>", lambda e: self.start_measure())
        self.measure_button.bind("<Enter>", lambda e: self.measure_button.config(bg="#0088cc"))
        self.measure_button.bind("<Leave>", lambda e: self.measure_button.config(bg="#00aaff"))

        self.count = 0
        self.is_measuring = False
        self.red_screen_active = False
        self.lock_screen_open = False
        self.correct_password_entered = False

        self.protocol("WM_DELETE_WINDOW", self.on_main_window_close)

    def on_main_window_close(self):
        if self.red_screen_active and not self.correct_password_entered:
            return
        self.destroy()

    def start_measure(self):
        if not self.is_measuring:
            self.is_measuring = True
            self.measure_button.config(state="disabled", cursor="watch")
            self.increment_progress()

    def increment_progress(self):
        if self.count < 100:
            self.count += 1
            self.progress["value"] = self.count
            self.power_label.config(text=f"Потужність: {self.count}%")
            self.after(50, self.increment_progress)
        else:
            self.power_label.config(text="SOS — ВСЁ ПІЗДЕЦ!")
            self.make_everything_red()
            self.after(5000, self.show_lock_screen)

    def make_everything_red(self):
        red_bg = Image.new('RGB', (600, 450), color='#cc0000')
        self.red_bg_photo = ImageTk.PhotoImage(red_bg)
        self.background_label.config(image=self.red_bg_photo)

        self.power_label.config(fg="white", bg="#cc0000", font=("Segoe UI", 28, "bold"))
        self.measure_button.config(text="❗❗❗", bg="#cc0000", fg="white", relief="flat", cursor="X_cursor", state="disabled")
        self.progress.config(style=self.red_progress_style)
        self.is_measuring = False
        self.red_screen_active = True

    def show_lock_screen(self):
        if self.lock_screen_open:
            return
        self.lock_screen_open = True

        self.lock_screen = tk.Toplevel(self)
        self.lock_screen.attributes("-fullscreen", True)
        self.lock_screen.attributes("-topmost", True)
        self.lock_screen.protocol("WM_DELETE_WINDOW", lambda: None)
        self.lock_screen.bind("<Escape>", lambda e: "break")
        self.lock_screen.config(bg="#004400")

        canvas = tk.Canvas(self.lock_screen, bg='#004400', highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.create_rectangle(0, 0, self.lock_screen.winfo_screenwidth(), self.lock_screen.winfo_screenheight(),
                                fill="#004400", stipple="gray50")

        lock_text = ("Ваш комьютер заблокирован!\n"
                     "Введіть пароль від програми щоб розблокувати")
        label = tk.Label(self.lock_screen, text=lock_text,
                         font=("Segoe UI", 36, "bold"),
                         fg="white", bg="#004400", justify="center")
        label.place(relx=0.5, rely=0.3, anchor="center")

        self.password_entry = tk.Entry(self.lock_screen, font=("Segoe UI", 24), show="*",
                                       justify="center", width=20)
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center")
        self.password_entry.focus_set()

        self.unlock_button = tk.Button(self.lock_screen, text="Розблокувати",
                                       font=("Segoe UI", 20, "bold"),
                                       bg="#00aa00", fg="white",
                                       activebackground="#007700",
                                       command=self.check_password)
        self.unlock_button.place(relx=0.5, rely=0.6, anchor="center")

        self.password_entry.config(state="normal")
        self.unlock_button.config(state="normal")

        self.lock_screen.grab_set()

    def check_password(self):
        password = self.password_entry.get()
        if password == "Ukraina":
            self.correct_password_entered = True
            self.lock_screen.grab_release()
            self.lock_screen.destroy()
            self.lock_screen_open = False
            self.reset_after_unlock()
        else:
            messagebox.showerror("Помилка", "Невірний пароль!")
            self.password_entry.delete(0, tk.END)
            self.password_entry.config(state="disabled")
            self.unlock_button.config(state="disabled")
            self.after(5000, self.enable_password_fields)

    def enable_password_fields(self):
        if self.lock_screen_open:
            self.password_entry.config(state="normal")
            self.unlock_button.config(state="normal")
            self.password_entry.focus_set()

    def reset_after_unlock(self):
        self.count = 0
        self.progress["value"] = 0
        self.power_label.config(text="Потужність: 0%", fg="white", bg="#000000", font=("Segoe UI", 20, "bold"))
        self.background_label.config(image=self.original_bg_photo)
        self.measure_button.config(text="Міряти", bg="#00aaff", fg="white", relief="raised", cursor="hand2", state="normal", bd=4)
        style = ttk.Style(self)
        style.configure("blue.Horizontal.TProgressbar", troughcolor='#222222', bordercolor='#222222',
                        background='#00aaff', lightcolor='#66ccff', darkcolor='#0088cc', thickness=25)
        self.progress.config(style=self.progress_style)
        self.red_screen_active = False
        self.is_measuring = False

if __name__ == "__main__":
    app = PotuzhnomirApp()
    app.configure(bg="#000000")
    app.mainloop()