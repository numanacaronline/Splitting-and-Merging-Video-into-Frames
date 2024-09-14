import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os
import re

class VideoSplitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Karelerine Ayırma ve Birleştirme Uygulaması")
        self.root.geometry("400x400")

        # Default language is English
        self.language = "en"
        self.translations = {
            "en": {
                "select_video": "Select Video",
                "select_output": "Select Output Directory",
                "start_process": "Start Processing",
                "select_frames": "Select Frames Directory",
                "select_output_video": "Select Output Video",
                "start_merging": "Start Merging",
                "warning": "Warning",
                "please_select_video": "Please select a video file.",
                "please_select_output": "Please select an output directory.",
                "fps_error": "Could not retrieve FPS information.",
                "process_complete": "Process completed! All frames saved.",
                "merge_complete": "Merging process completed!",
                "error": "Error",
                "please_select_frames": "Please select frames directory and output video path.",
                "settings": "Settings",
                "language": "Language",
                "select_language": "Select Language"
            },
            "tr": {
                "select_video": "Videoyu Seç",
                "select_output": "Çıkış Dizini Seç",
                "start_process": "İşlemi Başlat",
                "select_frames": "Kareleri Seç",
                "select_output_video": "Çıkış Video Yolunu Seç",
                "start_merging": "Birleştirmeyi Başlat",
                "warning": "Uyarı",
                "please_select_video": "Lütfen bir video dosyası seçin.",
                "please_select_output": "Lütfen bir çıkış dizini seçin.",
                "fps_error": "FPS bilgisi alınamadı.",
                "process_complete": "İşlem tamamlandı! Tüm kareler kaydedildi.",
                "merge_complete": "Birleştirme işlemi tamamlandı!",
                "error": "Hata",
                "please_select_frames": "Lütfen kareler dizinini ve çıkış video dosyasını seçin.",
                "settings": "Ayarlar",
                "language": "Dil",
                "select_language": "Dili Seç"
            }
        }

        # Set theme
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Configure the style
        self.style.configure('TButton', relief='flat', padding=10, background='#007bff', foreground='white', font=('Helvetica', 10))
        self.style.map('TButton', background=[('active', '#0056b3')], foreground=[('active', 'white')])

        self.video_path = ""
        self.output_dir = ""
        self.frames_dir = ""

        # Create tabs
        self.tab_control = ttk.Notebook(root)
        
        self.split_tab = ttk.Frame(self.tab_control)
        self.merge_tab = ttk.Frame(self.tab_control)
        self.settings_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.split_tab, text=self.translations[self.language]["select_video"])
        self.tab_control.add(self.merge_tab, text=self.translations[self.language]["select_frames"])
        self.tab_control.add(self.settings_tab, text=self.translations[self.language]["settings"])
        self.tab_control.pack(expand=1, fill='both')

        self.create_split_tab()
        self.create_merge_tab()
        self.create_settings_tab()

    def create_split_tab(self):
        # Video seçme butonu
        self.select_video_btn = ttk.Button(self.split_tab, text=self.translations[self.language]["select_video"], command=self.select_video)
        self.select_video_btn.pack(pady=10)

        # Çıkış dizini seçme butonu
        self.select_output_btn = ttk.Button(self.split_tab, text=self.translations[self.language]["select_output"], command=self.select_output_directory)
        self.select_output_btn.pack(pady=10)

        # İşlemi başlat butonu
        self.start_button = ttk.Button(self.split_tab, text=self.translations[self.language]["start_process"], command=self.start_processing)
        self.start_button.pack(pady=10)

    def create_merge_tab(self):
        # Kare dizinini seçme butonu
        self.select_frames_btn = ttk.Button(self.merge_tab, text=self.translations[self.language]["select_frames"], command=self.select_frames_directory)
        self.select_frames_btn.pack(pady=10)

        # Çıkış video yolu seçme butonu
        self.select_output_video_btn = ttk.Button(self.merge_tab, text=self.translations[self.language]["select_output_video"], command=self.select_output_video)
        self.select_output_video_btn.pack(pady=10)

        # Birleştirme işlemi başlat butonu
        self.merge_button = ttk.Button(self.merge_tab, text=self.translations[self.language]["start_merging"], command=self.start_merging)
        self.merge_button.pack(pady=10)

    def create_settings_tab(self):
        # Language selection
        language_label = ttk.Label(self.settings_tab, text=self.translations[self.language]["select_language"])
        language_label.pack(pady=10)

        self.language_var = tk.StringVar(value=self.language)
        language_menu = ttk.Combobox(self.settings_tab, textvariable=self.language_var, values=list(self.translations.keys()), state='readonly')
        language_menu.pack(pady=10)
        language_menu.bind("<<ComboboxSelected>>", self.change_language)

    def change_language(self, event):
        self.language = self.language_var.get()
        self.update_text()

    def update_text(self):
        # Update button texts and tab titles
        self.tab_control.tab(self.split_tab, text=self.translations[self.language]["select_video"])
        self.tab_control.tab(self.merge_tab, text=self.translations[self.language]["select_frames"])
        self.tab_control.tab(self.settings_tab, text=self.translations[self.language]["settings"])

        self.select_video_btn.config(text=self.translations[self.language]["select_video"])
        self.select_output_btn.config(text=self.translations[self.language]["select_output"])
        self.start_button.config(text=self.translations[self.language]["start_process"])
        self.select_frames_btn.config(text=self.translations[self.language]["select_frames"])
        self.select_output_video_btn.config(text=self.translations[self.language]["select_output_video"])
        self.merge_button.config(text=self.translations[self.language]["start_merging"])

    def select_video(self):
        self.video_path = filedialog.askopenfilename(title=self.translations[self.language]["select_video"], filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
        if not self.video_path:
            messagebox.showwarning(self.translations[self.language]["warning"], self.translations[self.language]["please_select_video"])

    def select_output_directory(self):
        self.output_dir = filedialog.askdirectory(title=self.translations[self.language]["select_output"])
        if not self.output_dir:
            messagebox.showwarning(self.translations[self.language]["warning"], self.translations[self.language]["please_select_output"])

    def select_frames_directory(self):
        self.frames_dir = filedialog.askdirectory(title=self.translations[self.language]["select_frames"])
        if not self.frames_dir:
            messagebox.showwarning(self.translations[self.language]["warning"], self.translations[self.language]["please_select_frames"])

    def select_output_video(self):
        self.output_video_path = filedialog.asksaveasfilename(title=self.translations[self.language]["select_output_video"], defaultextension=".mp4", filetypes=[("MP4 Files", "*.mp4")])
        if not self.output_video_path:
            messagebox.showwarning(self.translations[self.language]["warning"], self.translations[self.language]["please_select_output"])

    def get_video_fps(self):
        command = [
            "ffmpeg",
            "-i", self.video_path,
            "-hide_banner"
        ]

        result = subprocess.run(command, capture_output=True, text=True)
        fps = None

        for line in result.stderr.splitlines():
            if "fps" in line:
                match = re.search(r'(\d+(\.\d+)?)\s+fps', line)
                if match:
                    fps = float(match.group(1))
                    break
        
        return fps

    def start_processing(self):
        if not self.video_path or not self.output_dir:
            messagebox.showwarning(self.translations[self.language]["warning"], self.translations[self.language]["please_select_video"] + " " + self.translations[self.language]["please_select_output"])
            return
        
        fps = self.get_video_fps()
        if fps is None:
            messagebox.showerror(self.translations[self.language]["error"], self.translations[self.language]["fps_error"])
            return

        output_pattern = os.path.join(self.output_dir, "frame_%04d.png")
        command = [
            "ffmpeg",
            "-i", self.video_path,
            "-vf", f"fps={fps}",
            "-c:v", "png",
            output_pattern
        ]

        try:
            subprocess.run(command, check=True)
            messagebox.showinfo("Information", self.translations[self.language]["process_complete"])
        except subprocess.CalledProcessError:
            messagebox.showerror(self.translations[self.language]["error"], "An error occurred during processing.")

    def start_merging(self):
        if not self.frames_dir or not hasattr(self, 'output_video_path'):
            messagebox.showwarning(self.translations[self.language]["warning"], self.translations[self.language]["please_select_frames"] + " " + self.translations[self.language]["please_select_output"])
            return

        command = [
            "ffmpeg",
            "-framerate", "30",  # Desired FPS
            "-i", os.path.join(self.frames_dir, "frame_%04d.png"),
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            self.output_video_path
        ]

        try:
            subprocess.run(command, check=True)
            messagebox.showinfo("Information", self.translations[self.language]["merge_complete"])
        except subprocess.CalledProcessError:
            messagebox.showerror(self.translations[self.language]["error"], "An error occurred during merging.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoSplitterApp(root)
    root.mainloop()