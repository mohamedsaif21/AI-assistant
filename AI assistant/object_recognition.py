# object_recognition.py
import cv2
import numpy as np

# Load pre-trained YOLO model
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Load the COCO dataset for objects
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

def recognize_objects():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        height, width, channels = frame.shape

        # Prepare the frame for YOLO
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Analyze the output from YOLO
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Get object's name and coordinates
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    obj_class = classes[class_id]
                    print(f"Object Detected: {obj_class}")
                    # You can add additional authentication logic for specific objects
                    
        cv2.imshow('Object Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_objects()
