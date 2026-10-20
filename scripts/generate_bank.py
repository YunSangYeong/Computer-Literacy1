"""Deterministic original learning questions; no third-party exam text copied.
40 conceptual originals + 24 reasoning families x 40 inputs = 1000.
Independent evaluation lives in verify_bank.py and model.test.ts.
"""
import csv
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SUBJECTS=['컴퓨터 일반','스프레드시트 일반','데이터베이스 일반']
AUTHOR='https://github.com/YunSangYeong/Computer-Literacy1/blob/main/docs/question-provenance.md'
# Stem, correct answer, three distractors, authored rationale. No year/session invented.
CONCEPTS=[
[
('RAM의 일반적인 특성으로 옳은 것은?', '전원이 끊기면 저장 내용이 사라지는 휘발성 메모리이다.', '항상 읽기만 가능하다.|CPU의 산술 연산 전용 장치이다.|영구 보관용 광학 매체이다.', '일반적인 주기억장치 RAM은 읽기·쓰기가 가능하지만 전원 공급이 끊기면 내용이 유지되지 않는다. 영구 보관은 보조기억장치의 역할이다.'),
('CPU의 제어장치가 수행하는 핵심 역할은?', '명령어를 해석하고 각 장치에 제어 신호를 보낸다.', '모니터의 픽셀을 물리적으로 발광시킨다.|데이터를 자기 디스크에 영구 보관한다.|네트워크 주소를 자동으로 암호화한다.', '제어장치는 명령어 실행 순서와 데이터 흐름을 제어한다. 산술·논리 연산을 직접 수행하는 장치는 ALU이며 제어장치와 역할을 구별한다.'),
('캐시 메모리를 사용하는 주된 목적은?', 'CPU와 주기억장치 사이의 속도 차이를 줄인다.', '파일을 영구 보관한다.|전원 없이 모든 작업 상태를 보존한다.|프로그램의 소스 코드를 자동 작성한다.', '캐시는 자주 사용하는 명령어와 데이터를 CPU 가까이 두어 평균 메모리 접근 시간을 줄인다. 캐시는 보조기억장치를 대체하는 영구 저장소가 아니다.'),
('운영체제의 기능에 해당하는 것은?', '프로세스와 메모리 등의 자원을 관리한다.', '문서의 맞춤법만 검사한다.|하드웨어 없이 전력을 생산한다.|모든 악성코드 감염을 원천적으로 불가능하게 한다.', '운영체제는 프로세스·메모리·파일·입출력 장치를 관리하고 응용 프로그램에 실행 기반을 제공한다. 보안 기능이 있어도 모든 공격을 막는다는 보장은 없다.'),
('가상 메모리에 대한 설명으로 옳은 것은?', '보조기억장치의 일부를 활용해 주기억장치보다 큰 주소 공간을 제공할 수 있다.', '실제 RAM의 물리적 용량을 자동으로 늘린다.|CPU 레지스터를 영구 저장 장치로 바꾼다.|인터넷이 연결되어야만 사용할 수 있다.', '가상 메모리는 주소 변환과 필요한 페이지의 적재를 통해 큰 논리 주소 공간을 제공한다. 디스크 접근 비용이 있어 RAM 추가와 같은 성능 효과로 볼 수 없다.'),
('손실 압축에 관한 설명으로 옳은 것은?', '일부 정보를 버리므로 원본을 완전히 복원하지 못할 수 있다.', '압축 해제하면 언제나 원본과 비트 단위로 같다.|텍스트 실행 파일의 완전 복원에 항상 적합하다.|압축률은 모든 파일에서 반드시 동일하다.', '손실 압축은 중요도가 낮다고 판단한 정보를 제거하여 용량을 줄인다. 원본의 완전 복원이 필요한 파일에는 무손실 압축이 적합하다.'),
('피싱 공격의 전형적인 사례는?', '금융기관을 사칭한 링크로 가짜 로그인 페이지에 접속하도록 유도한다.', '정상 백업을 별도 저장장치에 보관한다.|운영체제의 보안 업데이트를 설치한다.|공식 사이트 주소를 직접 입력한다.', '피싱은 신뢰할 수 있는 기관이나 사람을 사칭해 인증 정보 등을 탈취한다. 링크의 실제 주소와 도메인을 확인하고 민감한 정보 입력을 신중히 해야 한다.'),
('다중 요소 인증의 예로 가장 적절한 것은?', '비밀번호와 소유한 인증 앱의 일회용 코드를 함께 사용한다.', '서로 다른 비밀번호 두 개만 사용한다.|같은 비밀번호를 두 번 입력한다.|사용자 이름을 두 번 입력한다.', '다중 요소 인증은 지식·소유·생체 등 서로 다른 종류의 인증 요소를 결합한다. 같은 종류의 비밀번호를 여러 번 입력하는 것만으로 요소 종류가 늘지는 않는다.'),
('DNS의 주된 역할은?', '도메인 이름에 대응하는 IP 주소 등의 정보를 조회하게 한다.', '전송되는 모든 파일을 자동 압축한다.|모니터 색상 수를 조절한다.|모든 IP 주소를 비밀번호로 변환한다.', 'DNS는 계층적인 분산 이름 시스템으로 도메인에 연결된 주소 등의 레코드를 조회한다. DNS 자체를 파일 압축이나 화면 설정 기능으로 혼동하지 않는다.'),
('HTTPS 연결에 대한 설명으로 옳은 것은?', 'TLS를 이용해 통신 내용을 보호하고 서버 인증을 지원한다.', '사이트에 기재된 모든 내용의 진실성을 보장한다.|접속하는 모든 사용자의 신원을 자동 실명 확인한다.|서버의 악성 파일 배포를 불가능하게 한다.', 'HTTPS는 전송 구간의 기밀성·무결성과 인증서 기반 서버 인증을 지원한다. 암호화된 연결이라는 사실만으로 운영자의 선의나 콘텐츠의 진실성을 보장하지는 않는다.'),
('랜섬웨어 피해 대비에 적절한 조치는?', '중요 자료의 분리된 백업을 유지하고 복원 가능 여부를 점검한다.', '백업을 한 번도 확인하지 않는다.|모든 보안 업데이트를 영구 중지한다.|의심스러운 첨부 파일을 우선 실행한다.', '분리된 백업과 복원 점검은 암호화나 파괴 피해 후 복구 가능성을 높인다. 백업만으로 감염 예방이 끝나는 것은 아니므로 업데이트와 접근 관리도 필요하다.'),
('유니코드와 UTF-8의 관계로 옳은 것은?', 'UTF-8은 유니코드 코드 포인트를 바이트열로 표현하는 인코딩 방식이다.', '유니코드는 한글만 표현한다.|UTF-8은 모든 문자를 항상 1바이트로 표현한다.|UTF-8은 이미지 전용 압축 형식이다.', '유니코드는 문자에 코드 포인트를 부여하는 표준이며 UTF-8은 이를 가변 길이 바이트열로 인코딩한다. 문자와 바이트 수는 항상 같지 않다.'),
('공개 키 암호 방식에 대한 설명으로 옳은 것은?', '공개 키와 개인 키라는 서로 연관된 키 쌍을 사용한다.', '암호화 키와 복호화 키가 항상 같은 하나의 비밀 키이다.|개인 키를 모든 사용자에게 공개해야 한다.|키를 전혀 사용하지 않는다.', '비대칭 암호는 공개 가능한 공개 키와 보호해야 하는 개인 키를 이용한다. 대칭 키 방식은 통신 당사자가 공유하는 비밀 키를 사용한다.'),
('SSD와 HDD에 대한 일반적인 설명으로 옳은 것은?', 'SSD는 일반적으로 회전하는 자기 디스크 없이 반도체 메모리에 데이터를 저장한다.', 'SSD는 반드시 회전 원판을 읽는다.|HDD는 언제나 RAM과 같은 휘발성 메모리이다.|두 장치는 모두 CPU 제어장치이다.', 'SSD는 보통 플래시 메모리 기반이며 기계적인 헤드 이동과 디스크 회전을 이용하는 HDD와 구조가 다르다. 실제 성능과 수명은 제품과 사용 조건에 따라 다르다.'),
],
[
('Excel 수식에서 절대 참조의 표기 예는?', '$A$1', 'A1|$A1|A$1', '달러 기호가 열 문자와 행 번호 앞에 모두 있으면 행과 열이 고정된다. $A1은 열만, A$1은 행만 고정하는 혼합 참조이다.'),
('Excel에서 셀의 표시 형식만 바꾸면 일반적으로 어떤 일이 일어나는가?', '화면에 표시되는 방식이 바뀌고 저장된 원래 값은 유지된다.', '저장된 모든 수치가 문자열로 영구 변환된다.|연결된 모든 통합 문서가 삭제된다.|수식이 반드시 값으로 덮어써진다.', '표시 형식은 수치·날짜 등의 화면 표현을 조정한다. 별도의 정밀도 설정 등 특수 조건을 변경하지 않는 한 값 자체를 편집하는 동작과는 구별된다.'),
('Excel의 COUNT 함수가 기본적으로 세는 대상은?', '숫자가 들어 있는 셀', '모든 빈 셀|글꼴이 굵은 셀만|오류 셀만', 'COUNT는 인수나 참조 범위의 숫자 개수를 센다. 비어 있지 않은 셀 개수는 COUNTA, 빈 셀 개수는 COUNTBLANK와 구별한다.'),
('Excel의 IFERROR 함수의 주된 용도는?', '수식에 오류가 발생하면 지정한 대체 값을 반환한다.', '모든 수식을 삭제한다.|정상 결과만 오류로 바꾼다.|오류가 없을 때만 무조건 0을 반환한다.', 'IFERROR(value, value_if_error)는 첫 번째 인수가 오류이면 두 번째 인수를 반환하고, 오류가 아니면 첫 번째 인수의 정상 결과를 반환한다.'),
('Excel에서 피벗 테이블의 주된 목적은?', '데이터를 여러 기준으로 집계하고 요약한다.', '운영체제를 설치한다.|바이러스 검사를 대신한다.|통합 문서를 반드시 암호화한다.', '피벗 테이블은 행·열·필터·값 영역을 이용해 대량의 자료를 집계한다. 원본 갱신 후에는 요약 결과에 반영되도록 새로 고침이 필요할 수 있다.'),
('Excel의 조건부 서식에 대한 설명으로 옳은 것은?', '조건을 만족하는 셀에 정해진 서식을 적용한다.', '조건을 만족하면 셀의 원본 수식을 모두 삭제한다.|파일 확장자를 자동으로 변경한다.|모든 시트를 반드시 숨긴다.', '조건부 서식은 값이나 수식 조건에 따라 글꼴·채우기 등의 표현을 바꾼다. 서식을 적용하는 기능이므로 셀의 원래 값 변경과는 구별한다.'),
('Excel의 데이터 유효성 검사가 주로 수행하는 기능은?', '셀에 입력할 수 있는 값의 종류나 범위를 제한한다.', 'CPU 사용량을 제한한다.|파일을 인터넷에 자동 배포한다.|모든 중복 행을 반드시 삭제한다.', '데이터 유효성 검사는 정수·목록·날짜·사용자 지정 수식 등의 조건으로 입력을 제어한다. 오류 메시지와 안내를 설정할 수 있으며 보안 경계로 간주하지 않는다.'),
('Excel에서 필터를 적용했을 때 일반적인 동작은?', '조건에 맞지 않는 행을 일시적으로 표시하지 않는다.', '조건에 맞지 않는 원본 행을 영구 삭제한다.|통합 문서를 자동 종료한다.|모든 수식이 텍스트로 바뀐다.', '필터는 조건에 맞는 레코드를 보여 주는 기능이며 보이지 않는 행도 원본 데이터에 남는다. 행 삭제와 필터링은 서로 다른 동작이다.'),
('Excel의 정렬 기능에 관한 설명으로 옳은 것은?', '하나 이상의 키를 기준으로 데이터의 순서를 바꾼다.', '항상 모든 중복을 제거한다.|정렬한 값은 다시 편집할 수 없다.|정렬은 글꼴 크기만 바꾸는 기능이다.', '정렬은 오름차순·내림차순 등으로 레코드 순서를 재배치한다. 관련 열을 함께 선택해 같은 행의 데이터 관계가 흐트러지지 않도록 해야 한다.'),
('Excel 매크로를 포함한 통합 문서를 저장하는 대표적인 확장자는?', '.xlsm', '.txt|.png|.xlsx', '매크로 사용 통합 문서의 대표 형식은 .xlsm이다. .xlsx 형식은 VBA 매크로 코드를 저장하는 형식이 아니므로 저장 시 기능 보존 여부를 확인한다.'),
('Excel의 SUMIFS 함수의 특징은?', '여러 조건을 모두 만족하는 셀의 값을 합산한다.', '조건 중 하나만 만족하면 항상 모든 값을 더한다.|문자열의 바이트 수만 센다.|오류 값을 무조건 삭제한다.', 'SUMIFS는 합계 범위와 조건 범위·조건의 쌍을 사용하며 여러 조건은 AND로 적용된다. 조건별 범위의 크기와 합계 범위를 일치시켜야 한다.'),
('Excel에서 이름 정의의 일반적인 장점은?', '셀 또는 범위에 의미 있는 이름을 붙여 수식의 가독성을 높인다.', '모든 참조를 자동으로 삭제한다.|파일 크기가 항상 0바이트가 된다.|조건부 서식이 영구적으로 금지된다.', '정의된 이름으로 범위나 상수 등을 참조하면 주소만 사용하는 것보다 의미가 명확해질 수 있다. 이름의 범위와 참조 대상을 확인해야 한다.'),
('Excel 차트의 범례가 주로 알려 주는 정보는?', '각 데이터 계열을 구분하는 이름과 표시', '운영체제 버전|컴퓨터의 IP 주소|문서 암호의 실제 값', '범례는 색상·표식 등과 데이터 계열의 대응을 보여 준다. 축 제목은 측정 기준이나 단위를, 데이터 레이블은 개별 데이터 값을 나타내는 용도로 구별된다.'),
],
[
('관계형 데이터베이스에서 기본 키의 일반적인 조건은?', '각 행을 유일하게 식별하며 NULL을 허용하지 않는다.', '중복과 NULL이 언제나 허용된다.|테이블마다 모든 열이 반드시 기본 키이다.|오직 날짜형 열만 가능하다.', '기본 키는 각 레코드의 식별자이므로 유일성과 NOT NULL 조건을 갖는다. 한 개 열 또는 여러 열의 조합으로 지정할 수 있다.'),
('외래 키의 주된 목적은?', '관련 테이블 사이의 참조 무결성을 유지한다.', '모든 문자열을 암호화한다.|저장장치를 자동 압축한다.|조회 결과를 항상 내림차순으로 정렬한다.', '외래 키는 다른 테이블 등의 키를 참조하여 유효하지 않은 관계 데이터의 입력을 제한한다. 참조 무결성의 적용과 NULL 허용 여부는 제약 조건에 따라 정해진다.'),
('SQL의 WHERE 절의 역할은?', '그룹화 전에 조건에 맞는 행을 선택한다.', '열의 물리적 저장 위치를 바꾼다.|집계 후의 그룹 조건만 검사한다.|조회 결과를 항상 정렬한다.', 'WHERE는 개별 행에 대한 조건을 적용한다. GROUP BY로 묶은 그룹의 집계 조건은 HAVING을 사용하며 정렬은 ORDER BY와 구별한다.'),
('SQL에서 그룹별 집계 결과에 조건을 적용하는 절은?', 'HAVING', 'ORDER BY|FROM|SELECT DISTINCT', 'HAVING은 그룹화·집계 결과에 대한 조건을 지정한다. WHERE는 그룹화 이전의 행을 필터링하므로 SUM 등의 집계 조건을 지정하는 역할과 구별한다.'),
('SQL에서 결과의 정렬 순서를 명시하는 절은?', 'ORDER BY', 'GROUP BY|WHERE|JOIN', 'ORDER BY는 조회 결과를 지정한 키와 방향으로 정렬한다. 명시적인 정렬 절이 없다면 테이블 입력 순서가 결과 순서로 보장된다고 가정하지 않는다.'),
('정규화의 주된 목적에 해당하는 것은?', '데이터 중복과 삽입·갱신·삭제 이상을 줄인다.', '모든 테이블을 하나의 열로만 만든다.|모든 키를 제거한다.|조회 결과를 항상 무작위로 만든다.', '정규화는 함수적 종속 등을 고려하여 관계 구조를 정리한다. 데이터 중복으로 인한 이상을 줄이는 것이 목적이며 어떤 경우에나 성능이 좋아진다고 단정할 수는 없다.'),
('트랜잭션의 원자성에 대한 설명으로 옳은 것은?', '관련 작업들이 모두 반영되거나 모두 반영되지 않도록 한다.', '모든 데이터를 항상 문자 하나로 저장한다.|모든 조회가 반드시 1밀리초 안에 끝난다.|모든 사용자가 같은 암호를 쓴다.', '원자성은 트랜잭션을 분리할 수 없는 작업 단위로 취급한다. 일부 작업만 반영되어 데이터가 불완전한 상태로 남지 않도록 커밋과 롤백을 이용한다.'),
('인덱스에 관한 일반적인 설명으로 옳은 것은?', '검색을 빠르게 할 수 있지만 갱신 비용과 추가 저장 공간이 필요할 수 있다.', '모든 작업의 시간이 반드시 줄어든다.|인덱스가 있으면 기본 키의 유일성이 항상 해제된다.|인덱스는 데이터를 영구 삭제하는 명령이다.', '인덱스는 검색 경로를 제공하지만 INSERT·UPDATE·DELETE 시 인덱스 유지 비용이 든다. 용도와 자료 분포를 고려하여 생성해야 한다.'),
('Access의 폼(Form)의 일반적인 용도는?', '사용자가 데이터를 입력하거나 조회할 화면을 구성한다.', '하드디스크를 포맷한다.|운영체제의 네트워크 드라이버를 설치한다.|모든 테이블의 관계를 자동 삭제한다.', '폼은 테이블이나 쿼리를 기반으로 입력·조회 등의 사용자 인터페이스를 제공한다. 인쇄용 정형 출력에 주로 쓰는 보고서와 역할을 구별한다.'),
('Access의 보고서(Report)가 주로 적합한 작업은?', '자료를 그룹화·요약하여 인쇄용 형태로 출력한다.', 'CPU 클럭을 조절한다.|네트워크 프로토콜을 교체한다.|항상 원본 테이블을 삭제한다.', '보고서는 페이지 단위의 서식과 그룹·집계 등을 이용한 출력에 적합하다. 폼이 주로 데이터 입력과 대화형 조회를 제공하는 기능과 구별한다.'),
('SQL에서 NULL 여부를 검사하는 적절한 조건은?', 'IS NULL', '= NULL|== NULL|LIKE NULL', 'NULL은 값이 없거나 알려지지 않았음을 나타내며 일반적인 등호 비교로 판정하지 않는다. NULL 검사는 IS NULL 또는 IS NOT NULL 조건을 사용한다.'),
('INNER JOIN의 기본적인 결과는?', '조인 조건에 일치하는 두 테이블의 행 조합', '항상 왼쪽 테이블의 모든 행만|조건과 무관한 모든 행의 전체 조합만|모든 NULL 값을 0으로 바꾼 결과만', '내부 조인은 지정한 관계 조건에 일치하는 행 조합만 반환한다. 일치하지 않는 쪽도 유지하는 외부 조인 및 모든 조합을 만드는 교차 조인과 구별한다.'),
('데이터베이스의 참조 무결성 위반 예로 적절한 것은?', '존재하지 않는 부모 키를 참조하는 자식 행을 입력한다.', '기본 키가 서로 다른 두 행을 입력한다.|필수 열에 유효한 값을 입력한다.|관련된 부모 행이 실제 존재한다.', '참조 무결성은 관계의 참조 대상이 유효하도록 하는 제약이다. 참조 대상이 없는 키를 자식 행에 입력하는 것은 해당 제약을 위반한다.'),
]]
bank=[]
def put(subject,stem,answer,distractors,explanation,topic,ident,family=None,calc=None):
 choices=[str(answer),*[str(v) for v in distractors]]
 assert len(set(choices))==4,(ident,choices)
 rotate=(len(bank)*7+1)%4
 choices=choices[rotate:]+choices[:rotate]
 q=dict(id=ident,subject=subject,topic=topic,question=stem,choices=choices,answer=choices.index(str(answer))+1,explanation=explanation,difficulty='중',year=None,session=None,type='original',sourceUrl=AUTHOR,verificationStatus='reviewed',reviewNote='AI 일반 지식으로 자체 작성. 내부 개념·해설 검토 및 수치/SQL 독립 재계산. 외부 전문가 검수·최신 공식 출제기준 대조 미완료. 출처 링크는 작성 이력이며 외부 정답 증빙이 아님.',version='main',rights='자체 제작 · CC BY 4.0 · Computer-Literacy1 contributors')
 if family:q['family']=family
 if calc:q['calculation']=calc
 bank.append(q)
for si,concepts in enumerate(CONCEPTS):
 for i,(stem,answer,ds,ex) in enumerate(concepts,1):put(SUBJECTS[si],stem,answer,ds.split('|'),ex,'기본 개념',f'CL1-C{si+1}-{i:03}')

def numerical(si,kind,i,stem,result,ex,values,unit='',extra=None):
 put(SUBJECTS[si],stem,str(result)+unit,[str(result+d)+unit for d in (1,3,7)],ex,kind,f'CL1-{kind}-{i:03}',kind,dict(kind=kind,values=values,result=result,unit=unit,**(extra or {})))
for i in range(1,41):
 # Computer fundamentals: unambiguous exact units and integer inputs.
 n=i+16
 numerical(0,'binary',i,f'2진수 {n:b}을 10진수로 변환한 값은?',n,f'각 비트에 오른쪽부터 2의 거듭제곱을 곱해 합한다. {n:b}(2) = {n}(10)이다.',[n],extra={'binary':f'{n:b}'})
 bits=i+4
 numerical(0,'states',i,f'서로 독립적인 {bits}비트로 표현 가능한 서로 다른 상태의 최대 개수는?',2**bits,f'한 비트는 2가지 상태다. 독립적인 {bits}비트의 조합 수는 2^{bits} = {2**bits}가지이다. 부호 유무와 관계없이 비트 패턴 수를 묻는다.',[bits])
 w=i+79;h=64
 numerical(0,'bitmap',i,f'가로 {w}픽셀, 세로 {h}픽셀, 픽셀당 24비트인 비압축 영상의 순수 픽셀 데이터 크기는? 헤더·패딩은 없으며 단위는 바이트이다.',w*h*3,f'픽셀 수 {w}×{h}, 픽셀당 24÷8=3바이트이므로 {w}×{h}×3 = {w*h*3}바이트이다. 헤더와 행 패딩은 제외한다.',[w,h,24], ' B')
 size=(i+5)*(1+i%4);rate=8*(1+i%4)
 numerical(0,'transfer',i,f'{size} MiB 파일을 {rate} Mibit/s로 전송한다. 프로토콜 부하 없이 일정 속도일 때 필요한 시간은? 1 MiB=2^20 B, 1 Mibit=2^20 bit.',i+5,f'바이트를 비트로 변환하여 시간=({size}×8)/{rate}={i+5}초이다. 두 접두 단위는 모두 2^20을 사용하여 약분된다.',[size,rate],'초')
 rate=8000+i*1000
 numerical(0,'pcm',i,f'표본화율 {rate} Hz, 표본당 16비트, 2채널로 2초간 녹음한 비압축 PCM의 순수 데이터 크기는? 헤더는 제외한다.',rate*8,f'초당 표본 수×표본당 비트×채널×시간÷8이다. {rate}×16×2×2÷8 = {rate*8}바이트이다.',[rate,16,2,2],' B')
 bits=i+9
 numerical(0,'address',i,f'한 주소가 1바이트를 가리키는 메모리에서 주소 비트가 {bits}개일 때, 주소 가능한 전체 용량은?',2**bits,f'{bits}비트로 2^{bits}개의 주소를 표현한다. 주소당 1바이트이므로 2^{bits} = {2**bits}바이트이다.',[bits],' B')
 n=i+64
 numerical(0,'hex',i,f'16진수 {n:X}를 10진수로 변환한 값은?',n,f'16진수는 각 자리의 값에 16의 거듭제곱을 곱해 더한다. {n:X}(16) = {n}(10)이다. A~F는 10~15를 뜻한다.',[n],extra={'hex':f'{n:X}'})
 numerical(0,'twosComplement',i,f'정수 -{i}을 8비트 2의 보수로 나타냈다. 그 비트열을 부호 없는 정수로 해석한 10진수 값은?',256-i,f'8비트에서 -{i}의 2의 보수 비트 패턴은 2^8-{i}={256-i}이다. 같은 패턴을 부호 없이 읽은 값을 묻는다.',[i])
 # Spreadsheet formula evaluations; all input cells contain plain numeric values.
 a=i+1;b=i+3;c=i+8
 numerical(1,'excelSum',i,f'Excel에서 A1={a}, A2={b}, A3={c}일 때 =SUM(A1:A3)의 결과는?',a+b+c,f'SUM은 지정 범위의 숫자를 더한다. {a}+{b}+{c}={a+b+c}이다. 모든 셀은 숫자이며 숨김·필터 조건은 없다.',[a,b,c])
 a=3*i;b=3*i+3;c=3*i+6
 numerical(1,'excelAverage',i,f'Excel에서 A1={a}, A2={b}, A3={c}일 때 =AVERAGE(A1:A3)의 결과는?',b,f'숫자 3개의 합을 3으로 나눈다. ({a}+{b}+{c})÷3={b}이다. 빈 셀이나 텍스트는 주어지지 않았다.',[a,b,c])
 a=i+10;v=a*2 if a>=30 else a+10
 numerical(1,'excelIf',i,f'Excel에서 A1={a}일 때 =IF(A1>=30,A1*2,A1+10)의 결과는?',v,f'먼저 {a}>=30 조건은 {"참" if a>=30 else "거짓"}이다. 따라서 {"A1*2" if a>=30 else "A1+10"}를 계산하여 {v}를 반환한다.',[a,30])
 a=i*7+3;b=i%7+3
 numerical(1,'excelMod',i,f'Excel 수식 =MOD({a},{b})의 결과는?',a%b,f'양의 정수에서 MOD는 나눗셈의 나머지이다. {a}={b}×{a//b}+{a%b}이므로 결과는 {a%b}이다.',[a,b])
 cents=i*113+21;v=(cents+50)//100
 numerical(1,'excelRound',i,f'Excel 수식 =ROUND({cents/100:.2f},0)의 결과는?',v,f'ROUND의 두 번째 인수가 0이면 정수 자리로 반올림한다. 양수 {cents/100:.2f}의 소수 부분에 일반적인 반올림을 적용하면 {v}이다.',[cents,100])
 vals=[i,i+3,i+7,i+10,i+14];t=20+i%9;v=sum(x>=t for x in vals)
 numerical(1,'excelCountif',i,f'Excel A1:A5에 순서대로 {", ".join(map(str,vals))}이 있다. =COUNTIF(A1:A5,">={t}")의 결과는?',v,f'{t} 이상인 값은 {", ".join(str(x) for x in vals if x>=t) or "없음"}이다. 조건에 맞는 셀의 개수는 {v}개이다.',[*vals,t])
 vals=[i+2,i+5,i+11,i+17];v=vals[0]+vals[2]+vals[3]
 numerical(1,'excelSumif',i,f'Excel A1:A4가 A,B,A,A이고 B1:B4가 {", ".join(map(str,vals))}일 때 =SUMIF(A1:A4,"A",B1:B4)의 결과는?',v,f'조건 범위에서 A인 행은 1·3·4행이다. 대응하는 합계 범위의 값 {vals[0]}+{vals[2]}+{vals[3]}={v}를 더한다.',vals)
 a=i+2;b=i%5+2;c=i+6;d=i%7+3;v=a*b+c*d
 numerical(1,'excelSumproduct',i,f'Excel A1={a}, A2={c}, B1={b}, B2={d}일 때 =SUMPRODUCT(A1:A2,B1:B2)의 결과는?',v,f'같은 위치의 값을 곱한 후 합산한다. {a}×{b}+{c}×{d}={v}이다. 두 범위는 모두 2행 1열이다.',[a,c,b,d])
 # SQL queries in the common Access/SQLite subset; actual queries independently executed.
 vals=[i,i+2,None,i+6];sql='SELECT COUNT(*) FROM T';v=4
 numerical(2,'sqlCountAll',i,f'테이블 T의 v 열에 {vals}가 있다(None은 SQL NULL). {sql}; 의 결과는?',v,'COUNT(*)는 NULL을 포함한 모든 행을 센다. 값의 합이 아니라 행의 개수이므로 4이다.',[i],extra={'rows':vals,'sql':sql})
 vals=[i,None,i+3,None,i+7];sql='SELECT COUNT(v) FROM T';v=3
 numerical(2,'sqlCountValue',i,f'T.v의 값이 {vals}이다(None은 NULL). {sql}; 의 결과는?',v,'COUNT(v)는 v가 NULL이 아닌 행만 센다. 숫자가 들어 있는 세 행이므로 결과는 3이다.',[i],extra={'rows':vals,'sql':sql})
 vals=[i,i+4,i+8,i+12];sql=f'SELECT SUM(v) FROM T WHERE v >= {i+5}';v=2*i+20
 numerical(2,'sqlSumWhere',i,f'T.v의 값이 {vals}일 때 {sql}; 의 결과는?',v,f'WHERE 조건을 만족하는 값은 {i+8}과 {i+12}이다. 합계는 {i+8}+{i+12}={v}이다.',[i],extra={'rows':vals,'sql':sql})
 vals=[2*i,2*i+4,2*i+8];sql='SELECT AVG(v) FROM T';v=2*i+4
 numerical(2,'sqlAverage',i,f'T.v의 값이 {vals}일 때 {sql}; 의 결과는?',v,f'AVG는 NULL이 아닌 숫자의 산술평균이다. ({2*i}+{2*i+4}+{2*i+8})÷3={v}이다.',[i],extra={'rows':vals,'sql':sql})
 vals=[i,i,i+1,None,i+1,i+2];sql='SELECT COUNT(*) FROM (SELECT DISTINCT v FROM T WHERE v IS NOT NULL) AS Q';v=3
 numerical(2,'sqlDistinct',i,f'T.v의 값이 {vals}이다(None은 NULL). {sql}; 의 결과는?',v,f'NULL을 제외하고 DISTINCT를 적용하면 {i}, {i+1}, {i+2}의 세 값이 남는다. 바깥 COUNT(*)는 이 세 행을 센다.',[i],extra={'rows':vals,'sql':sql})
 vals=[i,i+2,i+4,i+6,i+8];sql=f'SELECT COUNT(*) FROM T WHERE v BETWEEN {i+2} AND {i+6}';v=3
 numerical(2,'sqlBetween',i,f'T.v의 값이 {vals}일 때 {sql}; 의 결과는?',v,f'BETWEEN은 양 끝값을 포함한다. {i+2}, {i+4}, {i+6}의 세 행이 조건을 만족하므로 결과는 3이다.',[i],extra={'rows':vals,'sql':sql})
 vals=[i+3,i+17,i+8,i+25];sql='SELECT MAX(v)-MIN(v) FROM T';v=22
 numerical(2,'sqlRange',i,f'T.v의 값이 {vals}일 때 {sql}; 의 결과는?',v,f'최댓값 {i+25}에서 최솟값 {i+3}을 뺀다. {i+25}-{i+3}=22이다. NULL이나 그룹 조건은 없다.',[i],extra={'rows':vals,'sql':sql})
 vals=[i,i+1,i+2,i+3,i+4];t=i+2;sql=f'SELECT SUM(v) FROM T WHERE v < {t} OR v > {t+1}';v=3*i+5
 numerical(2,'sqlOr',i,f'T.v의 값이 {vals}일 때 {sql}; 의 결과는?',v,f'조건에 맞는 값은 {i}, {i+1}, {i+4}이다. {i}+{i+1}+{i+4}={v}이다. OR는 두 조건 중 하나라도 참인 행을 선택한다.',[i],extra={'rows':vals,'sql':sql})
assert len(bank)==1000
assert len({q['id'] for q in bank})==1000
(ROOT/'src/data/questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n')
# Examples are not part of the shared bank; importing them stays pending.
example={**bank[0],'id':'LOCAL-TEMPLATE-001','question':'[등록 예제] '+bank[0]['question'],'verificationStatus':'pending','reviewNote':'사용자가 출처·권한·정답을 확인하고 근거를 기록해야 합니다.'}
(ROOT/'public/templates/questions.json').write_text(json.dumps([example],ensure_ascii=False,indent=2)+'\n')
fields=['id','subject','topic','question','choice1','choice2','choice3','choice4','answer','explanation','difficulty','year','session','type','sourceUrl','verificationStatus','reviewNote','version','rights']
with (ROOT/'public/templates/questions.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();q={k:v for k,v in example.items() if k!='choices'};q.update({f'choice{i+1}':v for i,v in enumerate(example['choices'])});w.writerow(q)
print('Generated',len(bank),'original questions:',{s:sum(q['subject']==s for q in bank) for s in SUBJECTS})
