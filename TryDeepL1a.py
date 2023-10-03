import os
import cv2
import xml.etree.ElementTree as ET
def rotate_and_modify_xml(image_path, xml_path, rotation_angle):
    # 读取图像
    I0 = cv2.imread(image_path)
    # 对图像进行旋转
    I1 = cv2.rotate(I0, rotation_angle)
    # 获取旋转后图像的宽度和高度
    rot_m = I1.shape[1]
    rot_n = I1.shape[0]
    # 解析XML文件
    tree = ET.parse(xml_path)
    root = tree.getroot()
    # 获取XML中的尺寸信息
    size = root.find('size')
    size_width = int(size.find('width').text)
    size_height = int(size.find('height').text)
    # 更新尺寸信息为旋转后的宽度和高度
    size_width1 = str(rot_m)
    size_height1 = str(rot_n)
    size.find('width').text = size_width1
    size.find('height').text = size_height1
    # 遍历所有边界框节点
    for bndbox in root.iter('bndbox'):
        # 获取边界框的坐标值
        bndbox_xmin = int(bndbox.find('xmin').text)
        bndbox_ymin = int(bndbox.find('ymin').text)
        bndbox_xmax = int(bndbox.find('xmax').text)
        bndbox_ymax = int(bndbox.find('ymax').text)
        # 根据旋转角度更新边界框的坐标值
        if rotation_angle == cv2.ROTATE_180:
            xmin = size_width - bndbox_xmin
            ymin = size_height - bndbox_ymin
            xmax = size_width - bndbox_xmax
            ymax = size_height - bndbox_ymax
        elif rotation_angle == cv2.ROTATE_90_CLOCKWISE:
            xmin = bndbox_ymin
            ymin = size_width - bndbox_xmin
            xmax = bndbox_ymax
            ymax = size_width - bndbox_xmax
        else:
            xmin = size_height - bndbox_ymin
            ymin = bndbox_xmin
            xmax = size_height - bndbox_ymax
            ymax = bndbox_xmax
        # 更新边界框的坐标值
        bndbox.find('xmin').text = str(xmin)
        bndbox.find('ymin').text = str(ymin)
        bndbox.find('xmax').text = str(xmax)
        bndbox.find('ymax').text = str(ymax)
    # 返回旋转后的图像和更新后的XML树
    return I1, tree

def process_images(rotation_angle, save_path, read_path_img, read_path, save_path_img):
    # 检查保存路径是否存在，如果不存在则创建
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    # 获取目标路径下所有以'.xml'结尾的文件
    Tfile = [file for file in os.listdir(read_path) if file.endswith('.xml')]
    # 检查保存图像路径是否存在，如果不存在则创建
    if not os.path.exists(save_path_img):
        os.mkdir(save_path_img)
    # 获取目标图像路径下所有以'.jpg'结尾的文件
    Tfile_img = [file for file in os.listdir(read_path_img) if file.endswith('.jpg')]
    # 遍历所有目标文件
    for iTfile in range(len(Tfile)):
        # 构造图像和XML文件的完整路径
        img_path = os.path.join(read_path_img, Tfile_img[iTfile])
        xml_path = os.path.join(read_path, Tfile[iTfile])
        # 调用rotate_and_modify_xml函数进行图像旋转和XML修改
        I1, modified_tree = rotate_and_modify_xml(img_path, xml_path, rotation_angle)
        # 构造保存文件名
        name_wj1 = name_wj + '000000'
        m = int(name_wj1) + iTfile
        m1 = str(m)
        # 构造保存的XML文件路径并写入修改后的XML树
        patName = os.path.join(save_path, m1 + '.xml')
        modified_tree.write(patName)
        # 构造保存的图像文件路径并保存图像
        patName_img = os.path.join(save_path_img, m1 + '.jpg')
        cv2.imwrite(patName_img, I1)

        
readPath = r'C:\windows_v1.3.3\data_original\lab'
savePath = r'C:\windows_v1.3.3\knife\Annotations'

# 检查保存路径是否存在，如果不存在则创建
if not os.path.exists(savePath):
    os.mkdir(savePath)

# 获取指定路径下所有以'.xml'结尾的文件列表
Tfile = [file for file in os.listdir(readPath) if file.endswith('.xml')]

readPath_img = r'C:\windows_v1.3.3\data_original\img'
savePath_img = r'C:\windows_v1.3.3\knife\JPEGImages'

# 检查保存路径是否存在，如果不存在则创建
if not os.path.exists(savePath_img):
    os.mkdir(savePath_img)

# 获取指定路径下所有以'.jpg'结尾的文件列表
Tfile_img = [file for file in os.listdir(readPath_img) if file.endswith('.jpg')]


n = 4  # 将360度分割成4份，即90,180,270
jd = 360 / n
name_start = 70
for i in range(int(jd), 360, int(jd)):
    name = int(name_start + i // jd - 1) # 新生成的数据保存的文件名
    name_wj = str(name)
    if i == 90:
        process_images(cv2.ROTATE_90_COUNTERCLOCKWISE, savePath, readPath_img, readPath, savePath_img)
    elif i == 180:
        process_images(cv2.ROTATE_180, savePath, readPath_img, readPath, savePath_img)
    elif i == 270:
        process_images(cv2.ROTATE_90_CLOCKWISE, savePath, readPath_img, readPath, savePath_img)
    else:
        print('错误角度')