from ultralytics import YOLO


# 加载模型
model = YOLO('runs/detect/train/weights/best.pt')

# 进行推理
results = model('3ae361a2c493a26b1cb5a9d4f032abb4.jpg', show=True, save=False)

# 检查是否有检测结果
if results[0].boxes is not None and len(results[0].boxes) > 0:
    print("检测出结果。")
    for box in results[0].boxes:
        # 获取边界框坐标（xyxy 格式）
        xyxy = box.xyxy[0].cpu().numpy()
        # 获取置信度
        confidence = box.conf[0].cpu().numpy()
        print(f"检测结果坐标（xyxy 格式）: {xyxy}, 置信度: {confidence}")
else:
    print("未检测出结果。")