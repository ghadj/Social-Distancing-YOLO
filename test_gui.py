import os

def run_train(annotation_file, is_tiny):
    if is_tiny:
        cmd = 'python 2_Training/Download_and_Convert_YOLO_weights.py --is_tiny --annotation_file ' + annotation_file
        os.system(cmd)
        cmd = 'python 2_Training/Train_YOLO.py --is_tiny'
        os.system(cmd)
    else:
        cmd = 'python 2_Training/Download_and_Convert_YOLO_weights.py --annotation_file ' + annotation_file
        os.system(cmd)
        cmd = 'python 2_Training/Train_YOLO.py'
        os.system(cmd)

def run_inference(input_path, yolo_model, is_tiny, calibr_param):
    if is_tiny:
        cmd = 'python 3_Inference/Detector.py --is_tiny --input_path ' + input_path + ' --yolo_model ' + yolo_model + \
              ' --calibr_param ' + str(calibr_param)
        os.system(cmd)
    else:
        cmd = 'python 3_Inference/Detector.py --input_path ' + input_path + ' --yolo_model ' + yolo_model + \
              ' --calibr_param ' + str(calibr_param)
        os.system(cmd)

run_inference(r'C:\Users\const\Desktop\sample', r'C:\Users\const\Desktop\train\trained_weights_final[Dataset2].h5', False, 0.25)