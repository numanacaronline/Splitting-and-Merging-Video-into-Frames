import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os
import re

class VideoSplitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Karelerine Ayırma ve Birleştirme Uygulaması")
        self.root.geometry("400x300")
        
        # Set theme
        self.style = ttk.Style()
        self.style.theme_use('clam')  # You can choose 'clam', 'alt', or other themes

        # Configure the style
        self.style.configure('TButton', relief='flat', padding=10, background='#007bff', foreground='white', font=('Helvetica', 10))
        self.style.map('TButton', background=[('active', '#0056b3')], foreground=[('active', 'white')])

        self.video_path = ""
        self.output_dir = ""
        self.frames_dir = ""

        # Sekmeler
        self.tab_control = ttk.Notebook(root)
        
        self.split_tab = ttk.Frame(self.tab_control)
        self.merge_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.split_tab, text="Kare Ayırma")
        self.tab_control.add(self.merge_tab, text="Birleştirme")
        self.tab_control.pack(expand=1, fill='both')

        self.create_split_tab()
        self.create_merge_tab()

    def create_split_tab(self):
        # Video seçme butonu
        self.select_video_btn = ttk.Button(self.split_tab, text="Videoyu Seç", command=self.select_video)
        self.select_video_btn.pack(pady=10)

        # Çıkış dizini seçme butonu
        self.select_output_btn = ttk.Button(self.split_tab, text="Çıkış Dizini Seç", command=self.select_output_directory)
        self.select_output_btn.pack(pady=10)

        # İşlemi başlat butonu
        self.start_button = ttk.Button(self.split_tab, text="İşlemi Başlat", command=self.start_processing)
        self.start_button.pack(pady=10)

    def create_merge_tab(self):
        # Kare dizinini seçme butonu
        self.select_frames_btn = ttk.Button(self.merge_tab, text="Kareleri Seç", command=self.select_frames_directory)
        self.select_frames_btn.pack(pady=10)

        # Çıkış video yolu seçme butonu
        self.select_output_video_btn = ttk.Button(self.merge_tab, text="Çıkış Dizini Seç", command=self.select_output_video)
        self.select_output_video_btn.pack(pady=10)

        # Birleştirme işlemi başlat butonu
        self.merge_button = ttk.Button(self.merge_tab, text="Birleştirmeyi Başlat", command=self.start_merging)
        self.merge_button.pack(pady=10)

    def select_video(self):
        self.video_path = filedialog.askopenfilename(title="Videoyu Seç", filetypes=[("Video Dosyaları", "*.mp4;*.avi;*.mov")])
        if not self.video_path:
            messagebox.showwarning("Uyarı", "Lütfen bir video dosyası seçin.")

    def select_output_directory(self):
        self.output_dir = filedialog.askdirectory(title="Çıkış Dizini Seç")
        if not self.output_dir:
            messagebox.showwarning("Uyarı", "Lütfen bir çıkış dizini seçin.")

    def select_frames_directory(self):
        self.frames_dir = filedialog.askdirectory(title="Kareler Dizini Seç")
        if not self.frames_dir:
            messagebox.showwarning("Uyarı", "Lütfen karelerin bulunduğu dizini seçin.")

    def select_output_video(self):
        self.output_video_path = filedialog.asksaveasfilename(title="Çıkış Video Yolunu Seç", defaultextension=".mp4", filetypes=[("MP4 Dosyaları", "*.mp4")])
        if not self.output_video_path:
            messagebox.showwarning("Uyarı", "Lütfen bir çıkış video dosyası adı seçin.")

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
            messagebox.showwarning("Uyarı", "Lütfen hem video hem de çıkış dizinini seçin.")
            return
        
        fps = self.get_video_fps()
        if fps is None:
            messagebox.showerror("Hata", "FPS bilgisi alınamadı.")
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
            messagebox.showinfo("Bilgi", "İşlem tamamlandı! Tüm kareler kaydedildi.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Hata", "İşlem sırasında bir hata oluştu.")

    def start_merging(self):
        if not self.frames_dir or not hasattr(self, 'output_video_path'):
            messagebox.showwarning("Uyarı", "Lütfen kareler dizinini ve çıkış video dosyasını seçin.")
            return

        command = [
            "ffmpeg",
            "-framerate", "30",  # İstenilen FPS
            "-i", os.path.join(self.frames_dir, "frame_%04d.png"),
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            self.output_video_path
        ]

        try:
            subprocess.run(command, check=True)
            messagebox.showinfo("Bilgi", "Birleştirme işlemi tamamlandı!")
        except subprocess.CalledProcessError:
            messagebox.showerror("Hata", "Birleştirme sırasında bir hata oluştu.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoSplitterApp(root)
    root.mainloop()