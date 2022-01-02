# Car_Hackathon

# 교차로 모니터링 시스템 고도화 및 영상 데이터 활용 방안
> 2021 교차로 자동차 카운팅 인공지능 해커톤

- 기간: 2021.12.13-12.24
- 인원: 5명
- 일정관리: 카카오톡 오픈 채팅 및 슬랙
- 사용 모델: Yolov5
- 성과: 대상 수상
![image](https://user-images.githubusercontent.com/72932028/147867713-b3c3d1ab-968f-4b5c-b825-ecc4d07a57a3.png)


------------------------------------

> YOLOv5를 이용한 객체 탐지 및 카운팅 구현
1. YOLOv5 모델을 사용한 차량 객체 탐지  - 라온피플 데이터 활용

* ![image](https://user-images.githubusercontent.com/72932028/147867524-60440d40-5dd1-4d7a-a0d2-97988c154d64.png) 
* ![image](https://user-images.githubusercontent.com/72932028/147867564-01a1d226-8d2d-4dc0-9e79-54e32778b45d.png)
  * 도로교통 외부데이터(AI Hub Korea, 30743번, 주관사 라온피플) 사용하여 Yolo Custom 학습
  * 학습 이전 모델은 여러 차량의 나열된 모습을 열차(Train)로 인식하는 오류 존재
  * 외부데이터로 학습한 모델은 성능향상
  * 검증을 위해 도로영상을 프레임으로 분해하고, 각 프레임마다 YOLO 모델 연속적용 
  * Truck, bike, person 인식성능이 저조
  * 추후, COCO 데이터셋을 기반으로 재학습하여 Real Time Object Detection 성능 향상 성공

2. YOLOv5 모델을 사용한 차량 객체 탐지  - COCO dataset 데이터 활용

* https://user-images.githubusercontent.com/72932028/147867686-4d2e9aa8-7359-4f6d-bf69-47939778d774.mp4

  * 객체인식 알고리즘을 적용한 모니터링은 검출되는 객체에 대한 정보를 바탕으로 관리의 효율성을 높일 수 있는 장점이 있음
  * 현재 공공데이터를 바탕으로 자동차의 인식을 넘어서 차종에 따른 분류까지 구현이 가능함
