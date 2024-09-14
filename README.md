Video Frame Splitter and Merger Application

Overview

This application allows users to split video files into individual frames and merge frames back into a video. Built using PySide6 and FFmpeg, it provides a user-friendly interface for both operations, supporting multiple languages.

Features

Split Video into Frames: Select a video file and an output directory to extract frames as PNG images.

Merge Frames into Video: Select a directory of frames and specify an output video file to combine them back into a video format (MP4).

Language Support: Toggle between English and Turkish for the UI, making it accessible to a broader audience.

Dependencies

PySide6

FFmpeg



Installation

To run this application, ensure you have Python installed along with the necessary dependencies. You can install the required Python packages using:

pip install PySide6


Additionally, make sure FFmpeg is installed on your system and accessible from your command line.


![Splitting and Merging Video into Frames](https://github.com/numanacaronline/Splitting-and-Merging-Video-into-Frames/blob/main/1.png)

![Splitting and Merging Video into Frames](https://github.com/numanacaronline/Splitting-and-Merging-Video-into-Frames/blob/main/2.png)

![Splitting and Merging Video into Frames](https://github.com/numanacaronline/Splitting-and-Merging-Video-into-Frames/blob/main/3.png)

Usage

Splitting Frames:

Navigate to the "Split Frames" tab.

Click "Select Video" to choose a video file.

Click "Select Output Directory" to choose where to save the frames.

Click "Start Process" to begin extracting frames.

Merging Frames:

Navigate to the "Merge Frames" tab.

Click "Select Frames" to choose the directory containing the extracted frames.

Click "Select Output Video Path" to specify the output video file.

Click "Start Merging" to combine the frames into a video.

Settings:

Change the application language using the dropdown menu in the "Settings" tab.

Contributing

Feel free to fork this repository and submit pull requests for any improvements or features you'd like to add.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

Special thanks to the developers of PySide6 and FFmpeg for providing powerful tools for application development and media processing.
