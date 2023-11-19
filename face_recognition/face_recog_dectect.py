import cv2
import face_recognition

def detect_faces_live(known_face_path):

    # Load the image with known faces---------------------------------------
    known_image = face_recognition.load_image_file(known_face_path)
    known_face_encoding = face_recognition.face_encodings(known_image)[0]

    # Open a connection to the camera (0 represents the default camera)-------------------------
    cap = cv2.VideoCapture(0)

    while True:

        # Capture frame-by-frame------------------------------------
        ret, frame = cap.read()

        # Convert the frame to RGB----------------------------------------
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces in the frame-------------------------------------------

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Compare with known faces-------------------------------------
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            results = face_recognition.compare_faces([known_face_encoding], face_encoding)

            name = "Unknown"
            if results[0]:
                name = "Known Person"

            # Draw rectangle around the face and display name-------------------------------
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Display the output
        cv2.imshow('Face Recognition', frame)

        # Break the loop when 'q' is pressed-------------------------------
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window---------------------------------
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Provide the path to the known face image -------------------------------------------
    known_face_path = 'img.jpeg'

    detect_faces_live(known_face_path)
