# import customtkinter as ctk
from tkinter import filedialog

# ==========================================
# НАСТРОЙКИ И API-КЛЮЧ MINIMAX (ВСТРОЕН)
# ==========================================
MINIMAX_API_KEY = "sk-api-YwyqQins8e-o0otZp3QVFrp_uW411eIon5Fisxsj8f1XxkjvsMbotg9aaPh2V0nKT5p5MZSc3P1W9qBsSsUsJTSqh_agGPa-_K_gRY9kBOzWtctD1C0VYGI"

# Настройка общей темы оформления
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ForgeHubApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("FORGE HUB YOUTUBE")
        self.geometry("1100x700")
        self.configure(fg_color="#0b0f19")  # Темно-синий фон

        # Сетка: Боковая панель + Основная зона
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._create_sidebar()
        self._create_main_content()

    def _create_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color="#0f172a")
        sidebar.grid(row=0, column=0, sticky="nsew")

        # Название приложения
        logo_label = ctk.CTkLabel(
            sidebar, 
            text="FORGE HUB\nYOUTUBE", 
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#ffffff",
            justify="left"
        )
        logo_label.pack(padx=20, pady=(25, 30), anchor="w")

        # Кнопки навигации
        self.btn_step1 = ctk.CTkButton(
            sidebar, 
            text="1  Разметка таймкодов", 
            anchor="w", 
            fg_color="#1e293b", 
            hover_color="#334155",
            command=self.show_step1
        )
        self.btn_step1.pack(fill="x", padx=15, pady=5)

        self.btn_step2 = ctk.CTkButton(
            sidebar, 
            text="2  Финальная сборка", 
            anchor="w", 
            fg_color="transparent", 
            hover_color="#334155",
            command=self.show_step2
        )
        self.btn_step2.pack(fill="x", padx=15, pady=5)

        # Статус
        status_frame = ctk.CTkFrame(sidebar, fg_color="#1e293b", corner_radius=8)
        status_frame.pack(side="bottom", fill="x", padx=15, pady=20)
        
        status_dot = ctk.CTkLabel(status_frame, text="●", text_color="#10b981", font=ctk.CTkFont(size=14))
        status_dot.pack(side="left", padx=(10, 5), pady=8)
        
        status_text = ctk.CTkLabel(status_frame, text="Ключ активен", font=ctk.CTkFont(size=12))
        status_text.pack(side="left", pady=8)

    def _create_main_content(self):
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=30, pady=25)
        self.show_step1()

    def _clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_step1(self):
        """Вкладка 1: Разметка таймкодов"""
        self._clear_main_frame()
        self.btn_step1.configure(fg_color="#2563eb")
        self.btn_step2.configure(fg_color="transparent")

        title = ctk.CTkLabel(self.main_frame, text="Выбор метода разметки таймкодов", font=ctk.CTkFont(size=22, weight="bold"))
        title.pack(anchor="w", pady=(0, 5))
        
        subtitle = ctk.CTkLabel(self.main_frame, text="Настройте файлы и выберите подходящий способ синхронизации", text_color="#94a3b8")
        subtitle.pack(anchor="w", pady=(0, 25))

        self._add_file_input("Папка с картинками", "Добавьте папку с исходными изображениями")
        self._add_file_input("Аудиодорожка диктора", "Добавьте аудиофайл с озвучкой")
        self._add_file_input("Сценарий для авто-режима (.txt)", "Файл с текстом по строкам")

        mode_label = ctk.CTkLabel(self.main_frame, text="Режим работы разметки:", font=ctk.CTkFont(size=14, weight="bold"))
        mode_label.pack(anchor="w", pady=(15, 8))

        mode_segmented = ctk.CTkSegmentedButton(
            self.main_frame, 
            values=["AI Автоматический (MiniMax)", "Интерактивный по клику"],
            selected_color="#2563eb"
        )
        mode_segmented.set("AI Автоматический (MiniMax)")
        mode_segmented.pack(fill="x", pady=(0, 30))

        action_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        action_frame.pack(fill="x", pady=10)

        run_btn = ctk.CTkButton(action_frame, text="Запустить выбранный метод разметки", height=45, fg_color="#2563eb", hover_color="#1d4ed8", font=ctk.CTkFont(size=15, weight="bold"))
        run_btn.pack(side="left", expand=True, fill="x", padx=(0, 10))

        stop_btn = ctk.CTkButton(action_frame, text="Стоп", height=45, width=100, fg_color="#991b1b", hover_color="#7f1d1d", font=ctk.CTkFont(size=15, weight="bold"))
        stop_btn.pack(side="right")

    def show_step2(self):
        """Вкладка 2: Финальная сборка видео"""
        self._clear_main_frame()
        self.btn_step2.configure(fg_color="#2563eb")
        self.btn_step1.configure(fg_color="transparent")

        title = ctk.CTkLabel(self.main_frame, text="Финальная сборка видео", font=ctk.CTkFont(size=22, weight="bold"))
        title.pack(anchor="w", pady=(0, 5))
        
        subtitle = ctk.CTkLabel(self.main_frame, text="Загрузите размеченные файлы и соберите видеоролик с эффектами", text_color="#94a3b8")
        subtitle.pack(anchor="w", pady=(0, 25))

        self._add_file_input("Папка с размеченными картинками", "Путь к папке...")
        self._add_file_input("Аудиодорожка диктора", "Основной аудиофайл...")
        self._add_file_input("Фоновая музыка (опционально)", "Трек для фона...")
        self._add_file_input("Куда сохранить готовое видео (.mp4)", "Путь для сохранения...")

        run_btn = ctk.CTkButton(self.main_frame, text="ПОЕХАЛИ! (Начать сборку)", height=45, fg_color="#16a34a", hover_color="#15803d", font=ctk.CTkFont(size=15, weight="bold"))
        run_btn.pack(fill="x", pady=(20, 0))

    def _add_file_input(self, label_text, placeholder):
        lbl = ctk.CTkLabel(self.main_frame, text=label_text, font=ctk.CTkFont(size=13, weight="bold"))
        lbl.pack(anchor="w", pady=(10, 4))
        
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 5))
        
        entry = ctk.CTkEntry(frame, placeholder_text=placeholder, height=38, fg_color="#0f172a", border_color="#334155")
        entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        btn = ctk.CTkButton(frame, text="Обзор", width=90, height=38, fg_color="#1e293b", hover_color="#334155", command=lambda: self._select_file(entry))
        btn.pack(side="right")

    def _select_file(self, entry_widget):
        path = filedialog.askopenfilename()
        if path:
            entry_widget.delete(0, "end")
            entry_widget.insert(0, path)

if __name__ == "__main__":
    app = ForgeHubApp()
    app.mainloop()
forgehub-YouTube-
