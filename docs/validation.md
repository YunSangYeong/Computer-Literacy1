# 실제 검증 기록

검증일: 2026-10-20 (한국 시간). 작업 디렉터리 `/workspace/Computer-Literacy1`.

| 검사 | 결과 | 실제 범위 |
| --- | --- | --- |
| 기준 소스 확보 | 통과 | 표준 1.0.0 기준 커밋 b9a682ccff1b460334b78d5bfad9375b7ec4fbb6의 코드 직접 재사용 |
| 스킬 연결 | 통과 | SKILL.md와 references 전체 복사, 없던 AGENTS.md 생성·연결 |
| `npm ci --cache /workspace/.npm-cache --no-audit --no-fund` | 종료 0 | lockfile 고정 설치, TLS/패키지 integrity 유지 |
| `python3 scripts/verify_bank.py` | 종료 0 | 1,000개 구조·중복·메타데이터, 실제 SQL 320개, 결정적 재생성 일치 |
| `npm test` | 종료 0, 657개 통과 | 640개 독립 수치 평가 + 17개 시험/학습/가져오기/은행 검사 |
| `npm run build` | 종료 0 | TypeScript와 Vite 프로덕션 번들. 데이터 포함 JS 약 1.31MB/압축 약146KB로 Vite 크기 권고 경고 있음 |
| `npm run test:e2e` | 종료 0, 26개 통과 | Chromium desktop + Pixel 7 에뮬레이션 각 13개, 실물 기기 아님 |
| 화면 직접 검토 | 통과 | 1440×1000 desktop 및 393×851 mobile 크기 스크린샷 확인, 수평 넘침 없음 |
| 공식 시험 규칙·출제범위 | 차단 | license.korcham.net CONNECT HTTP 403. 최신 공식 대조 미완료, 앱에 잠정 규칙 표시 |
| 외부 전문가 문항 검수 | 미실행 | 내부 개념 검토·독립 재계산과 구별 |
| GitHub API | 차단 | 기존 GH_TOKEN 존재 여부만 확인, 기존 Git 인증 사용. gh api가 Forbidden 반환 |
| Pages 공개 사이트 | 차단 | yunsangyeong.github.io CONNECT HTTP 403 |

브라우저 테스트는 두 모드·학습 기준 메뉴 부재·과목/개수·시험 중 해설 비공개·36정답 합격·평균 78.3점이어도 과락 불합격·북마크·새로고침·답안 변경·제출 확인 취소/확인·절대 시각 만료 및 만료 후 클릭·중복 제출·전체 해설·오답 필터/복습·연습 즉시 채점/통계/이어하기·JSON/CSV 수입·원자적 오류·중복·승인 근거·초기화·저장 용량 경고·손상 원본 보존·실제 기록 백업 다운로드·두 모드 실제 keydown/keyup Space·버튼 기본 동작·수정키/길게 누르기/선택 컨트롤/대화상자 보호·동일 origin iframe의 포커스/Space/저장 공유를 확인했다. 교차 사이트 블로그 iframe과 모든 브라우저 정책 검증은 아니다.

은행 SHA256: `4e90b355cd0b024fa9699b85208bf9119bbb63ed6fcec68bd0e6c3b592fc4324`.

## 재사용 환경

npm 캐시는 쓰기 가능한 `/workspace/.npm-cache`를 사용한다. 홈 디렉터리 기본 npm 캐시 쓰기 오류를 해결한 것이며 checksum/TLS를 끄지 않았다. `/usr/bin/chromium`이 현재 머신에 이미 있어 이를 사용했고 없으면 Playwright 정식 설치를 사용한다.

환경 설정 초안에는 공식 자료 및 배포 검증에 필요한 `license.korcham.net`, `api.github.com`, `yunsangyeong.github.io` 도메인을 기존 패키지 preset을 보존하여 추가했다. 초안 저장은 런타임 적용·환경 게시와 별개다. 현재 차단이 해제되었다고 주장하지 않는다.

## 원격 반영·배포

현재 소스의 로컬 검증은 완료했다. `.github/workflows/pages.yml`은 main의 은행/단위/브라우저 검증 성공 후 Pages 배포를 수행하도록 구성했다. 원격 반영과 CI·배포의 관측 결과는 별도로 아래에 기록한다. Pages Source는 GitHub Actions 설정이 필요하다.


### 원격에서 확인한 실제 실행

- 앱 최초 구현 커밋 `4de49ca13de89b50c51b91d65801e6521392b0e6`을 main에 푸시하고 `git ls-remote`로 일치 확인했다.
- [Actions #1](https://github.com/YunSangYeong/Computer-Literacy1/actions/runs/39347101872): **validate 성공**, **deploy 실패**. 공개 GitHub 웹의 작업 상태와 annotations로 확인했다. API 차단을 이유로 CI 결과 확인을 생략하지 않았다.
- validate 단계는 은행 검증·단위 테스트·PC/모바일 e2e·빌드·Pages 아티팩트 업로드를 완료했다. `github-pages` 아티팩트 153KB를 생성했다. 상세 콘솔 로그는 웹 로그인 제한 때문에 별도로 읽지 못했고 로컬의 657/26 테스트 수와 원격 job 성공을 구별한다.
- 배포 실패 원인: `actions/configure-pages@v5`에서 `Get Pages site failed` 및 `HttpError: Not Found`. 저장소에 Pages가 활성화되어 GitHub Actions Source로 설정되어 있지 않다. 앱 코드·문항·테스트 실패가 아니다.
- [configure-pages v5의 공식 action.yml](https://github.com/actions/configure-pages/blob/v5/action.yml)을 읽었다. `enablement`에는 기본 GITHUB_TOKEN 이외의 토큰이 필요하다고 명시한다. 기본 workflow 토큰으로 자동 활성화를 보장하는 변경을 하지 않았다. 기존 클라우드 Git 인증으로 푸시는 가능하지만 GitHub API는 Forbidden이므로 여기서 초기 Pages 설정을 바꿀 수 없다. 새 토큰을 채팅으로 요구하거나 노출하지 않았다.
- 필요한 외부 조치: 저장소 Settings → Pages → Source를 **GitHub Actions**로 설정한 다음 [Actions](https://github.com/YunSangYeong/Computer-Literacy1/actions)에서 배포 workflow를 다시 실행한다. 현재의 정확한 최종 커밋은 Git 이력 및 Actions에서 확인한다.
- 공개 주소 `https://yunsangyeong.github.io/Computer-Literacy1/`는 예정된 기본 주소이며 이번 실행에서 배포 성공 또는 실제 공개 동작이 확인된 URL이 아니다. Pages 배포 실패와 별도로 이 환경의 공개 도메인 CONNECT 403도 남아 있다.
- 재사용 설정 초안의 `install_script`, `start_skill`을 저장했고 개발 서버 HTTP 200과 대상 제목 및 프로덕션 preview/실제 브라우저 동작을 확인했다. 네트워크 변경은 환경 설정에서 검토·저장 후 환경 게시가 필요하다. 초안 저장을 런타임 적용·환경 게시 완료로 간주하지 않는다.
