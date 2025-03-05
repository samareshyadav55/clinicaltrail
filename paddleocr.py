from paddleocr import PaddleOCR

def paddle_ocr_img(img):
    final_text = ''
    final_bboxes = []
    
    ocr = PaddleOCR(lang='en', use_angle_cls=True)
    result_ = ocr.ocr(img)
    
    # Iterate through the OCR result
    for line in result_[0]:
        # Extract the bounding box (polygon points)
        bbox = line[0]  # Bounding box as a polygon (list of four points)
        
        # Convert the polygon bounding box to x1, y1, x2, y2 format
        x_coords = [point[0] for point in bbox]  # Extract all x coordinates
        y_coords = [point[1] for point in bbox]  # Extract all y coordinates
        
        x1 = min(x_coords)
        y1 = min(y_coords)
        x2 = max(x_coords)
        y2 = max(y_coords)
        
        # Store the text and the transformed bounding box
        text = line[1][0]  # Text in the box
        final_text += ' ' + text
        final_bboxes.append([x1, y1, x2, y2])
        
        # Print the bounding box in x1, y1, x2, y2 format for debugging
        print(f"Text: {text} | Bounding Box: [{x1}, {y1}, {x2}, {y2}]")
    
    return final_text, final_bboxes
