# 압축 알고리즘
데이터를 압축하여 원래 데이터보다 적은 공간을 차지하도록 해서 데이터를 효율적으로 저장하거나 전송할 수 있게 하는 알고리즘. 

![image](https://github.com/user-attachments/assets/4d889828-a438-4f51-9282-32c4326319bc)

이미지 출처 - https://www.samsungsds.com/kr/news/index.html
## DEFLATE 알고리즘
LZ77과 Huffman 알고리즘을 사용하여 데이터를 무손실 압축한다.
빈도가 높은 문자 또는 기호에 짧은 코드를 할당하고 빈도가 높은 문자에는 더 적은 비트가 필요하므로 전체 데이터의 크기를 줄일 수 있다.
![image](https://github.com/user-attachments/assets/b40a64ee-10e7-47cf-8742-afdede7aaf3f)


### LZ77 알고리즘
중복되는 데이터를 찾아내어 이전 데이터와의 차이로 표현

### Huffman 알고리즘
빈도가 높은 문자 또는 기호 -> 짧은 코드 할당<br>
빈도가 낮은 문자 -> 긴 코드 할당 

데이터를 압축해 빈도가 높은 문자에 더 작은 비트가 필요하게 되어 전체 데이터의 크기를 줄인다.

### 프로그램 동작 과정 
![image](https://github.com/user-attachments/assets/d2cff949-b59c-472c-8761-174a9d7675e4)

### 프로그램 실행화면
![image](https://github.com/user-attachments/assets/4c9ba397-96ca-413e-9e0b-03d007b92a87)
선택된 파일들을 화면에 표시
![image](https://github.com/user-attachments/assets/bd535802-7244-4479-aa00-e6150dbd3fc2)
압축 파일 이름 지정
![image](https://github.com/user-attachments/assets/81cc5d56-a206-42a8-b306-215700144406)
압축된 파일 생성 확인

