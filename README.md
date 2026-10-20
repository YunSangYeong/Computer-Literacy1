# 컴퓨터활용능력 1급 필기 CBT

React + TypeScript + Vite로 만든 비공식 필기 연습 사이트입니다. 로그인·서버·유료 API 없이 이 브라우저에 학습 기록을 저장합니다. **기출 은행이 아닌 자체 제작 1,000문항**이며 최신 공식 안내 대조와 외부 전문가 검수는 미완료입니다. 실기는 제공하지 않습니다.

## 기능과 표준

- 실전 모의시험과 즉시 채점 랜덤 학습, 전체/과목 선택, 절대 시각 기반 제한 시간과 자동 제출, 답안 변경과 새로고침 복원
- 제출 후 과목별 점수·과락·정답·해설·출처, 오답 필터와 다시 풀기
- 오답노트, 북마크, 취약 과목·최근 시험·실제 풀이 통계, 이전 연습 이어하기
- 두 모드 모두 답안 선택/채점 후 Space 이동. 마지막 문제에서 Space 자동 제출 없음. 모바일 접이식 메뉴, 키보드 포커스·입력·대화상자 보호
- JSON/CSV 양식·가져오기·중복 제거·검증 대기·근거 기록 후 로컬 승인·검색·상태 필터·페이지·내보내기
- 기록 JSON 백업, 확인 후 초기화, 저장 실패 알림·손상 원본 자동 덮어쓰기 방지. 백업 복원 UI는 없음
- 학습 기준/버전 선택 메뉴 없음. 가짜 학습 이력 없음

[CBT 표준 스킬](.agents/skills/cbt-site-standard/SKILL.md) 전체와 references를 복사하고 [AGENTS.md](AGENTS.md)에 연결했습니다. 원래 이 저장소에는 AGENTS.md가 없어 새로 작성했습니다. 기준 `YunSangYeong/electrician-cbt@b9a682ccff1b460334b78d5bfad9375b7ec4fbb6`의 App·스타일·모델·테스트·설정·배포 코드를 직접 재사용하고 대상 시험에 맞게 수정했습니다. MIT 고지는 [LICENSE](LICENSE)에 유지했습니다.

## 시험 설정과 공식 확인 상태

단일 설정: [src/qualification.json](src/qualification.json).

| 항목 | 학습용 잠정 설정 |
| --- | --- |
| 과목 | 컴퓨터 일반 / 스프레드시트 일반 / 데이터베이스 일반 |
| 문제 | 과목별 20개, 총 60개, 객관식 4지선다 |
| 시간 | 60분 |
| 과목 점수 | 각 과목 정답 수 ÷ 20 × 100 (문항당 5점) |
| 합격 | 모든 과목 40점 이상, 세 과목 평균 60점 이상 |
| 과락 | 한 과목이라도 40점 미만이면 평균이 높아도 불합격 |
| 미응답 | 오답으로 처리 |

판정은 반올림 전 비율을 사용합니다. 화면 평균은 소수 첫째 자리로 표시합니다. 시험은 과목별 가족/개념에서 우선 1문항씩 뽑고 전체 순서를 섞습니다. 유형이 부족한 로컬 은행은 남은 고유 ID로 보충합니다.

공식 안내 확인 대상은 [대한상공회의소 자격평가사업단 컴퓨터활용능력 안내](https://license.korcham.net/co/examguide.do?cd=0103&mm=21)입니다. 2026-10-20 현재 클라우드 프록시 CONNECT HTTP 403으로 본문을 읽지 못했습니다. 따라서 위 규칙을 최신 공식 규칙으로 검증 완료했다고 표시하지 않습니다. 공식 출제범위·프로그램 버전 대조 및 기출 원문·정답·회차·재배포 권리 확인도 미완료입니다. 앱에 이 한계를 표시합니다.

## 문제은행

| 과목 | 개념형 | 계산·추론 조건 변형 | 합계 |
| --- | ---: | ---: | ---: |
| 컴퓨터 일반 | 14 | 8유형 × 40조건 = 320 | 334 |
| 스프레드시트 일반 | 13 | 8유형 × 40조건 = 320 | 333 |
| 데이터베이스 일반 | 13 | 8유형 × 40조건 = 320 | 333 |
| 전체 | 40 | 24유형 × 40조건 = 960 | **1,000** |

원문 기출 0 / 복원 0 / 자체 제작 1,000. 독립 유형 64개에 조건 변형을 포함한 수입니다. 개별 ID와 정규화 본문·보기는 중복되지 않습니다. 실제 시험의 전체 주제·난이도 분포를 재현하지 않으며 계산·추론 중심의 기본 학습 은행입니다. [출처·검수 상세](docs/question-provenance.md)에 작성 근거, 유형 반복, 내부 검토 및 외부 검증 한계를 공개합니다.

- 원고·생성: `scripts/generate_bank.py`. 고정 ID/순서, 난수 없음, 재생성 바이트 일치 확인
- 수치형 640개: 별도의 TypeScript 평가 경로. DB 320개: 실제 SQLite 실행. Excel/Access 제품에서 직접 실행한 것은 아님
- `reviewed`는 내부 검토 완료이며 외부 전문가 또는 공식 인증이 아님. 외부 수입은 항상 pending으로 시작하여 학습에서 제외
- 새 자체 작성 데이터 CC BY 4.0. 제3자 수입 권리는 개별 확인

## 개발·검증

Node.js 24.19.0 (`.node-version`), npm lockfile 사용. Node >=22.12 필요.

```sh
cd /workspace/Computer-Literacy1
npm ci --cache /workspace/.npm-cache --no-audit --no-fund
python3 scripts/verify_bank.py
npm run check
npm run test:e2e
npm run dev
```

Linux에 `/usr/bin/chromium`이 있으면 브라우저 테스트가 자동 사용합니다. 그 외에는 `npx playwright install --with-deps chromium`으로 설치하거나 `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH`를 지정하세요. 로컬 Vite 개발 서버는 기본 5173, 빌드 미리보기는 `npm run preview -- --port 4173`입니다. 프로젝트 base는 `/Computer-Literacy1/`입니다.

현재 실행 결과·배포 상태는 [검증 보고서](docs/validation.md)에 기록합니다. PC Chromium과 Pixel 7 크기/터치 에뮬레이션이며 실물 모바일 기기 검증이 아닙니다.

## 저장·보존

namespace `computer-literacy1-cbt:v1`로 같은 소유자의 다른 Pages 프로젝트와 구별합니다. 응답은 최근 5,000개, 시험은 최근 30회 보존하며 화면 통계는 보존된 응답 기준입니다. 북마크·오답·로컬 수입·진행 중 시험/연습을 저장합니다. 초기화는 기본 은행을 삭제하지 않습니다. 다른 브라우저/origin에는 기록이 공유되지 않습니다. iframe의 교차 사이트 저장 제한·시크릿 모드·용량 제한에 따라 저장이 실패할 수 있으며 경고를 표시합니다. 같은 origin iframe의 Space·저장 공유는 테스트하지만 모든 블로그·브라우저의 서드파티 저장 정책을 보장하지 않습니다.

## GitHub Pages

대상 브랜치 `main`, Actions workflow `.github/workflows/pages.yml`. 은행 검증 → 단위 테스트 → PC/모바일 브라우저 테스트와 프로덕션 빌드가 성공한 뒤 Pages 아티팩트를 배포합니다. 저장소 Settings → Pages → Build and deployment → Source는 **GitHub Actions**여야 합니다. 기본 주소는 `https://yunsangyeong.github.io/Computer-Literacy1/`이며 캐시 파라미터를 별도 주소로 삼지 않습니다.

설정된 workflow, 로컬 성공, 원격 반영, Actions 성공, Pages 배포 완료, 실제 공개 페이지 응답은 별도 단계입니다. 공식 사이트·GitHub API·공개 Pages 도메인 접근이 현재 환경에서 차단되어 있으면 그 부분은 확인 불가로 보고합니다. 최신 상태는 검증 보고서를 확인하세요.
