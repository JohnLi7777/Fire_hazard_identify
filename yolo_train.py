from ultralytics import YOLO



if __name__ == '__main__':
    a1 = YOLO('yolo11s.pt')

    a1.train(
        data='data.yaml',
        epochs=100,
        imgsz=640,
        batch=32,
        device='cuda'
    )

    print('模型训练完成')