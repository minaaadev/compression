# 압축 알고리즘
데이터를 압축하여 원래 데이터보다 적은 공간을 차지하도록 해서 데이터를 효율적으로 저장하거나 전송할 수 있게 하는 알고리즘. 

## DEFLATE 알고리즘
LZ77과 Huffman 알고리즘을 사용하여 데이터를 무손실 압축

### LZ77 알고리즘
중복되는 데이터를 찾아내어 이전 데이터와의 차이로 표현

### Huffman 알고리즘
빈도가 높은 문자 또는 기호 -> 짧은 코드를 할당
빈도가 낮은 문자 -> 긴 코드를 할당 

데이터를 압축해 빈도가 높은 문자에 더 작은 비트가 필요하게 되어 전체 데이터의 크기를 줄인다.

### 프로그램의 동작 과정 
1. 압축할 파일 선택
2. 선택된 파일 화면에 표시
3. 선택된 파일을 압축하여 하나의 파일로 만들어 압축된 파일을 저장
