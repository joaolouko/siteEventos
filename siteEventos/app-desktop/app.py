from pymongo import MongoClient
import customtkinter

class DashboardApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Dashboard")

        # MongoDB setup
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["teste"]
        self.collection = self.db["submissoes"]

        # Layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="ns")
        self.sidebar.grid_propagate(False)

        self.sidebar_label = customtkinter.CTkLabel(self.sidebar, text="Dashboard", font=("Arial", 20))
        self.sidebar_label.pack(pady=20)

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar, text="Ver Submissões", command=self.show_stats)
        self.sidebar_button_1.pack(pady=10, fill="x", padx=10)

        # Header
        self.header = customtkinter.CTkFrame(self, height=50)
        self.header.grid(row=0, column=1, sticky="ew", padx=10, pady=(10, 5))
        self.header.grid_columnconfigure(0, weight=1)

        self.header_label = customtkinter.CTkLabel(self.header, text="Painel de Submissões", font=("Arial", 18))
        self.header_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Main Content
        self.main_content = customtkinter.CTkFrame(self)
        self.main_content.grid(row=1, column=1, sticky="nsew", padx=10, pady=(0, 10))
        self.main_content.grid_rowconfigure(0, weight=1)
        self.main_content.grid_columnconfigure(0, weight=1)

        self.content_box = customtkinter.CTkTextbox(self.main_content, font=("Arial", 14))
        self.content_box.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def show_stats(self):
        self.content_box.delete("1.0", "end")
        self.content_box.insert("end", "Submissões encontradas:\n\n")

        submissions = list(self.collection.find())
        if not submissions:
            self.content_box.insert("end", "Nenhuma submissão encontrada.")
            return

        for sub in submissions:
            texto = (
                f"🧑 Nome: {sub.get('name', '')}\n"
                f"Data do show: {sub.get('date', '')}\n"
                f"Local: {sub.get('local', '')}\n"
                f"E-mail: {sub.get('email', '')}\n"
                f"{'-'*30}\n"
            )
            self.content_box.insert("end", texto)

if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()
