import cv2 

class Camera:

    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Camera not found or accessible.")
        
        self.width = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(f"Camera Initialized: {self.width}x{self.height}")

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()
        

    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                print("Warning: Failed to capture frame.")
                return False, None
        
        print("Warning: Camera is not open.")
        return False, None