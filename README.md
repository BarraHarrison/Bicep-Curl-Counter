# Bicep-Curl Counter using Machine Learning

## 📌 Project Overview
The **Bicep-Curl Counter** is a machine learning-based fitness application that utilizes **OpenCV** for real-time video processing, **scikit-learn** for classification, and **Tkinter** for a graphical user interface. The goal is to detect and count bicep curls automatically using computer vision and machine learning.

---

## 🏗 Project Structure

### **1️⃣ Purpose of Each File**

- **`main.py`**  
  - The main entry point of the application.  
  - Initializes the GUI and manages execution by integrating camera, ML model, and UI components.
  
- **`camera.py`**  
  - Handles webcam input using OpenCV (`cv2`).
  - Processes video frames for real-time bicep curl detection.
  - Prepares data for feature extraction and ML classification.

- **`app.py`**  
  - Manages the **Tkinter-based GUI** for the application.
  - Displays buttons, labels, and live feedback for user interaction.
  - Connects the UI to backend functionalities like starting/stopping the camera and running ML predictions.

- **`model.py`**  
  - Implements **machine learning logic** for detecting bicep curls.
  - Uses `sklearn.svm.LinearSVC` for classifying arm movements.
  - Trains on relevant features extracted from video frames and predicts curl movements.

- **`test.py`**  
  - A minimal Tkinter script used to debug **GUI-related issues**.
  - Helped confirm that Tkinter was functional on macOS by testing basic UI components like buttons and labels.

---

## ⚠️ Challenges & Troubleshooting

### **🔹 Problems Faced with Tkinter**
- **Invisible UI Elements:**
  - Labels, frames, and buttons were sometimes not rendering correctly.
  - The button appeared, but labels and frames were not visible even when correctly added to the layout.

- **MacOS Tkinter Deprecation Issues:**
  - Received warnings about **deprecated system Tk version** (Tk 8.5.9).
  - Upgraded to **Tk 9.0.1 via Homebrew**, but Python initially failed to recognize the update.

- **Virtual Environment and Dependencies:**
  - Reinstalled Python multiple times to ensure **Tkinter compatibility**.
  - Encountered `ModuleNotFoundError: No module named '_tkinter'`, requiring manual reconfiguration of Python.

---

## ✅ Positives from the Project
- **Successful Integration of ML with Tkinter** 🎉
  - Built a **functional GUI** for a machine-learning-based fitness application.

- **Hands-on Experience with OpenCV and Machine Learning** 🧠
  - Utilized `cv2` for **real-time video processing** and `scikit-learn` for **SVM-based classification**.
  - Gained experience in **feature extraction from video data**.

- **Debugging and Problem-Solving Skills** 🔍
  - Overcame **Tkinter rendering issues** and MacOS compatibility problems.
  - Learned how to manually **configure Homebrew Python to work with Tkinter**.

---

## ❌ Negatives from the Project
- **Time-Consuming Tkinter Fixes** ⏳
  - Spent a **long time troubleshooting GUI issues**, reducing focus on ML development.
  - Future projects might benefit from using **PyQt or Tkinter alternatives** for GUI.

- **MacOS-Specific Compatibility Issues** 💻
  - Required manual **Python and Tk** upgrades due to version mismatches.
  - Running Tkinter on **Windows/Linux** may have been smoother.

---

## 🏁 Final Thoughts
This project was a **great learning experience**, combining **real-time video processing, machine learning, and UI development**. While **Tkinter presented major challenges**, overcoming them helped refine **debugging skills** and **system configuration knowledge**. The end result is a **functional and interactive Bicep Curl Counter** that can be further improved! 🚀💪

