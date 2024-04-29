# 기본 기능 구현중
# spartamarket-DRF
우리를 위한 중고거래 :: 스파르타 마켓(DRF)

### 사용 프로그램
python 3.10\
django\
그 외 패키지 - requirements.txt

<img src="static/images/spartamarket-DRF.png", alt="왜안뜸"/>

## 기능
회원가입
- **Endpoint**: **`/api/accounts`**
- **Method**: **`POST`**

<img src="static/images/#", alt="왜안뜸"/>

로그인
- **Endpoint**: **`/api/accounts/login`**
- **Method**: **`POST`**

<img src="static/images/#", alt="왜안뜸"/>

프로필 조회- 
- **Endpoint**: **`/api/accounts/<str:username>`**
- **Method**: **`GET`**

<img src="static/images/#", alt="왜안뜸"/>

상품 등록
- **Endpoint**: **`/api/products`**
- **Method**: **`POST`**

<img src="static/images/#", alt="왜안뜸"/>

상품 목록 조회
- **Endpoint**: **`/api/products`**
- **Method**: **`GET`**

<img src="static/images/#", alt="왜안뜸"/>

상품 수정
- **Endpoint**: **`/api/products/<int:productId>`**
- **Method**: **`PUT`**

<img src="static/images/#", alt="왜안뜸"/>

상품 삭제
- **Endpoint**: **`/api/products/<int:productId>`**
- **Method**: **`DELETE`**

<img src="static/images/#", alt="왜안뜸"/>
