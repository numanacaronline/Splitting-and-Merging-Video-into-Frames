Video Splitter and Merger Application
This application allows users to split a video into individual frames and merge frames back into a video. Built using the Tkinter library for the GUI and FFmpeg for video processing, it offers an intuitive interface for managing video files.

Features
Split Video into Frames: Select a video file and an output directory to extract frames as PNG images.
Merge Frames into Video: Choose a directory containing extracted frames and specify an output file to create a new video.
User-Friendly Interface: Navigate through tabs for splitting and merging with simple button clicks.
Theme Customization: A clean and modern design using the clam theme.
Requirements
Python 3.x
Tkinter (included with Python)
FFmpeg (must be installed and accessible from the command line)
Usage
Splitting Video:
Go to the "Kare Ayırma" tab.
Click "Videoyu Seç" to choose a video file.
Click "Çıkış Dizini Seç" to select a directory for saving frames.
Click "İşlemi Başlat" to start the extraction process.
Merging Frames:
Switch to the "Birleştirme" tab.
Click "Kareleri Seç" to select the directory containing the extracted frames.
Click "Çıkış Video Yolunu Seç" to specify a filename for the new video.
Click "Birleştirmeyi Başlat" to create the video from frames.
License
This project is open-source and available for modification and distribution. Please ensure to comply with any licensing terms related to the use of FFmpeg.

Acknowledgments
FFmpeg - The powerful multimedia framework for handling video, audio, and other multimedia files and streams.
