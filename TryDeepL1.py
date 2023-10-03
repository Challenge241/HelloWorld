import os
import cv2
import xml.etree.ElementTree as ET
def DlabRand_crop_90(jd, name_wj):
    readPath = r'C:\DeepLearning\data\data_original\lab'
    savePath = r'C:\DeepLearning\data\knife\Annotations'
    if not os.path.exists(savePath):
        os.mkdir(savePath)
    Tfile = [file for file in os.listdir(readPath) if file.endswith('.xml')]

    readPath_img = r'C:\DeepLearning\data\data_original\img'
    savePath_img = r'C:\DeepLearning\data\knife\JPEGImages'
    if not os.path.exists(savePath_img):
        os.mkdir(savePath_img)
    Tfile_img = [file for file in os.listdir(readPath_img) if file.endswith('.jpg')]
    if jd == 90:
        for iTfile in range(len(Tfile)):
            # Read image
            img_path = os.path.join(readPath_img, Tfile_img[iTfile])
            I0 = cv2.imread(img_path)
            I1 = cv2.rotate(I0, cv2.ROTATE_90_COUNTERCLOCKWISE)
            rot_m = I1.shape[1]
            rot_n = I1.shape[0]
            # Read and modify XML
            xml_path = os.path.join(readPath, Tfile[iTfile])
            tree = ET.parse(xml_path)
            root = tree.getroot()
            size = root.find('size')
            size_width = int(size.find('width').text)
            size_height = int(size.find('height').text)
            size_width1 = str(rot_m)
            size_height1 = str(rot_n)
            size.find('width').text = size_width1
            size.find('height').text = size_height1
            for bndbox in root.iter('bndbox'):
                bndbox_xmin = int(bndbox.find('xmin').text)
                bndbox_ymin = int(bndbox.find('ymin').text)
                bndbox_xmax = int(bndbox.find('xmax').text)
                bndbox_ymax = int(bndbox.find('ymax').text)
                xmin = size_height - bndbox_ymin
                ymin = bndbox_xmin
                xmax = size_height - bndbox_ymax
                ymax = bndbox_xmax
                bndbox.find('xmin').text = str(xmin)
                bndbox.find('ymin').text = str(ymin)
                bndbox.find('xmax').text = str(xmax)
                bndbox.find('ymax').text = str(ymax)
            name_wj1 = name_wj + '000000'
            m = int(name_wj1) + iTfile
            m1 = str(m)
            patName = os.path.join(savePath, m1 + '.xml')
            tree.write(patName)
            patName_img = os.path.join(savePath_img, m1 + '.jpg')
            cv2.imwrite(patName_img, I1)
    elif jd == 180:
        for iTfile in range(len(Tfile)):
            # Read image
            img_path = os.path.join(readPath_img, Tfile_img[iTfile])
            I0 = cv2.imread(img_path)
            I1 = cv2.rotate(I0, cv2.ROTATE_180)
            rot_m = I1.shape[1]
            rot_n = I1.shape[0]
            # Read and modify XML
            xml_path = os.path.join(readPath, Tfile[iTfile])
            tree = ET.parse(xml_path)
            root = tree.getroot()
            size = root.find('size')
            size_width = int(size.find('width').text)
            size_height = int(size.find('height').text)
            size_width1 = str(rot_m)
            size_height1 = str(rot_n)
            size.find('width').text = size_width1
            size.find('height').text = size_height1
            for bndbox in root.iter('bndbox'):
                bndbox_xmin = int(bndbox.find('xmin').text)
                bndbox_ymin = int(bndbox.find('ymin').text)
                bndbox_xmax = int(bndbox.find('xmax').text)
                bndbox_ymax = int(bndbox.find('ymax').text)
                xmin = size_width - bndbox_xmin
                ymin = size_height - bndbox_ymin
                xmax = size_width - bndbox_xmax
                ymax = size_height - bndbox_ymax
                bndbox.find('xmin').text = str(xmin)
                bndbox.find('ymin').text = str(ymin)
                bndbox.find('xmax').text = str(xmax)
                bndbox.find('ymax').text = str(ymax)
            name_wj1 = name_wj + '000000'
            m = int(name_wj1) + iTfile
            m1 = str(m)
            patName = os.path.join(savePath, m1 + '.xml')
            tree.write(patName)
            patName_img = os.path.join(savePath_img, m1 + '.jpg')
            cv2.imwrite(patName_img, I1)
    elif jd == 270:
        for iTfile in range(len(Tfile)):
            # Read image
            img_path = os.path.join(readPath_img, Tfile_img[iTfile])
            I0 = cv2.imread(img_path)
            I1 = cv2.rotate(I0, cv2.ROTATE_90_CLOCKWISE)
            rot_m = I1.shape[1]
            rot_n = I1.shape[0]
            # Read and modify XML
            xml_path = os.path.join(readPath, Tfile[iTfile])
            tree = ET.parse(xml_path)
            root = tree.getroot()
            size = root.find('size')
            size_width = int(size.find('width').text)
            size_height = int(size.find('height').text)
            size_width1 = str(rot_m)
            size_height1 = str(rot_n)
            size.find('width').text = size_width1
            size.find('height').text = size_height1
            for bndbox in root.iter('bndbox'):
                bndbox_xmin = int(bndbox.find('xmin').text)
                bndbox_ymin = int(bndbox.find('ymin').text)
                bndbox_xmax = int(bndbox.find('xmax').text)
                bndbox_ymax = int(bndbox.find('ymax').text)
                xmin = bndbox_ymin
                ymin = size_width - bndbox_xmin
                xmax = bndbox_ymax
                ymax = size_width - bndbox_xmax
                bndbox.find('xmin').text = str(xmin)
                bndbox.find('ymin').text = str(ymin)
                bndbox.find('xmax').text = str(xmax)
                bndbox.find('ymax').text = str(ymax)
            name_wj1 = name_wj + '000000'
            m = int(name_wj1) + iTfile
            m1 = str(m)
            patName = os.path.join(savePath, m1 + '.xml')
            tree.write(patName)
            patName_img = os.path.join(savePath_img, m1 + '.jpg')
            cv2.imwrite(patName_img, I1)
    else:
        print('错误角度')
n = 4  # 将360度分割成4份，即90,180,270
jd = 360 / n
name_start = 70
for i in range(int(jd), 360 , int(jd)):
    print(i)
    name =int( name_start + i // jd - 1 )# 新生成的数据保存的文件名
    name_wj = str(name)
    DlabRand_crop_90(i, name_wj)