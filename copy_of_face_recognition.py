import face_recognition

# Load images
known_image = face_recognition.load_image_file("KnownFace.jpg")
known_face_encodings = face_recognition.face_encodings(known_image)[0]  # Indentation fixed

unknown_image = face_recognition.load_image_file("UnknownFace.jpg")
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

# Compare faces
for unknown_face_encoding in unknown_face_encodings:
    results = face_recognition.compare_faces([known_face_encodings], unknown_face_encoding)  # Plural form used

    if results[0]:
        print("Face recognized!")
    else:
        print("Face not recognized.")
