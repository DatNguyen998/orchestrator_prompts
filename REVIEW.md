# Đánh giá cấu trúc repository

**Ngày đánh giá:** 2026-08-20

**Phạm vi:** toàn bộ file được Git theo dõi tại commit `f195f50`, trước các sửa
lỗi được ghi trong tài liệu này.

**Repo tham chiếu:**
[`openai/openai-agents-python`](https://github.com/openai/openai-agents-python),
repo chính thức của OpenAI Agents SDK.

## Kết luận nhanh

Repo có lõi nội dung nhỏ, dễ đọc và phân tách đúng ba loại tài sản: prompt có
thể copy, Claude Code agent chạy trực tiếp, và skill có thể tái sử dụng. Phần
routing cũng đã chỉ rõ domain owner và merge owner, tốt hơn nhiều repo prompt
chỉ gom các file văn bản mà không mô tả cách phối hợp.

Điểm yếu lớn nhất không nằm ở chất lượng câu chữ mà ở **khả năng kiểm chứng**:
chưa có test/CI, schema chung, ví dụ chạy được, hay quy trình đóng góp. Lỗi đổi
tên `maya` thành `shinsho` đã lọt qua README, guide, routing và ba agent prompt;
đây là bằng chứng thực tế cho khoảng trống đó. Đợt review này sửa toàn bộ tham
chiếu đang hoạt động và thêm một validator tối thiểu để lỗi tương tự không quay
lại.

**Đánh giá tổng thể: 6.5/10** — nền tảng nội dung tốt, nhưng mới ở mức thư viện
prompt được biên tập kỹ; chưa đạt mức repository agent có quality gate đầy đủ.

## Cấu trúc hiện tại

```text
.
├── .claude/
│   ├── agents/              # Bốn Claude Code subagent
│   └── SQUAD-ROUTING.md     # Task graph và merge rule
├── .github/workflows/       # CI kiểm tra cấu trúc
├── docs/                    # Changelog HTML tĩnh
├── prompts/                 # Prompt độc lập, copy-paste được
├── scripts/                 # Validator không cần dependency ngoài
├── skills/                  # Skill instruction có thể dùng độc lập
├── CHANGELOG.md
├── GUIDE.md
├── README.md
└── REVIEW.md
```

## So sánh với repo Agent tham chiếu

Hai repo không cùng loại sản phẩm: repo này là thư viện Markdown; OpenAI Agents
SDK là framework Python. Vì vậy, so sánh tập trung vào các **thực hành có thể
chuyển giao**, không yêu cầu repo này sao chép cấu trúc package Python.

| Hạng mục | Repo hiện tại | Thực hành ở repo tham chiếu | Nhận định |
| --- | --- | --- | --- |
| Điểm vào cho người đọc | `README.md` và `GUIDE.md` giải thích ba loại tài sản | README, docs và examples tách vai trò rõ | **Tốt** |
| Phân ranh agent | Mỗi seat có owner, lens, checklist, refusal | Agent, handoff và guardrail là khái niệm tách biệt | **Tốt**, routing nên machine-readable hơn |
| Điều phối | Có diamond routing và `atlas` làm merge owner | Handoff/orchestration là primitive có thể chạy và quan sát | **Khá**, hiện mới là quy ước bằng văn bản |
| Ví dụ | Prompt có output mẫu; agent chưa có scenario end-to-end | Có examples chạy được cho nhiều pattern | **Thiếu** |
| Kiểm thử | Validator cấu trúc tối thiểu được thêm trong đợt review | Có test suite tự động | **Cần mở rộng mạnh** |
| CI | Workflow validator được thêm trong đợt review | Có nhiều quality gate tự động | **Khởi đầu tốt**, chưa kiểm thử hành vi |
| Metadata | Agent có front matter; prompt/skill dùng heading tự do | Package/API có kiểu và contract rõ | **Cần schema thống nhất** |
| Quan sát và đánh giá | Chưa có trace, fixture hay scorecard | Tracing và evaluation là phần quan trọng của agent lifecycle | **Khoảng trống lớn** |
| Quản trị dự án | Có changelog; chủ ý không cấp license | Có contribution, release và security conventions rõ | **Thiếu CONTRIBUTING/support policy** |

## Những điểm đang làm tốt

### 1. Phân loại tài sản rõ ràng

`prompts/`, `.claude/agents/` và `skills/` có mục đích khác nhau và README giải
thích đúng cách sử dụng từng loại. Người mới không phải đoán file nào để paste,
file nào được runtime nạp, và file nào là capability tái sử dụng.

### 2. Routing có owner cuối cùng

`SQUAD-ROUTING.md` không chỉ liệt kê agent mà còn đặt `atlas` làm merge owner,
giới hạn fan-out vào đúng seat liên quan và cấm đệ quy. Đây là một contract vận
hành cụ thể, tránh việc bốn agent trả bốn đáp án rời rạc.

### 3. Agent prompt ngắn và có guardrail theo domain

Mỗi agent front matter hóa `name`, `description`, `tools`; phần body giữ cấu
trúc owner → lens → checklist → out-of-lane/refusal. Prompt ngắn làm giảm xung
đột instruction và dễ review hơn một mega-prompt.

### 4. Prompt v2 có kiểm tra toàn vẹn đầu vào

Squad Director v2 bảo toàn tên agent, xử lý duplicate, quy định team-count,
kiểm tra dropped/invented agent, giới hạn vòng sửa và nêu edge case. Đây là các
failure mode thực tế, không phải chỉ là mô tả persona.

### 5. Documentation trung thực về giới hạn

Guide nói rõ repo chưa có canon knowledge base, agent không tự thực hiện hành
động không thể đảo ngược, và routing không tự thích nghi. Cách mô tả này giúp
người dùng không nhầm prompt với một hệ thống production hoàn chỉnh.

## Những điểm cần cải thiện

### P0 — tính nhất quán định danh

Lần rename `maya` → `shinsho` chỉ đổi file và front matter, nhưng bỏ sót nhiều
tham chiếu đang hoạt động. Hậu quả là README trỏ tới file không tồn tại, còn
routing yêu cầu gọi một seat không tồn tại. Đợt review đã sửa các tham chiếu và
validator hiện kiểm tra link local, front matter, filename/name, roster README
và tên cũ trong tài liệu đang hoạt động.

### P1 — test hành vi prompt/agent

Validator cấu trúc không thể phát hiện agent trả lời sai domain hoặc Squad
Director làm rơi input. Nên thêm:

1. `tests/fixtures/` chứa input nhỏ, duplicate, ambiguous và 50+ agents.
2. Scorecard bất biến: không đổi tên, không bịa agent, đúng membership rule.
3. Routing cases: single-domain, cross-domain, out-of-lane, và merge-owner.
4. Một runner tách model adapter khỏi assertion để chạy cùng fixture trên nhiều
   model; CI thường ngày có thể dùng test tĩnh, evaluation có model chạy theo
   lịch hoặc trước release để kiểm soát chi phí.

### P1 — schema và manifest chung

Hiện agent dùng YAML front matter, trong khi prompt và skill dùng prose. Nên có
manifest (JSON/YAML) hoặc schema tối thiểu cho mọi artifact: `id`, `version`,
`kind`, `purpose`, `when_to_use`, `inputs`, `outputs`, `tools`, `owner`,
`status`. Manifest giúp tạo catalog, validate duplicate ID, phát hiện broken
routing và hỗ trợ UI/tooling mà không phải parse Markdown tự do.

### P1 — ví dụ end-to-end

Tạo `examples/` với ít nhất hai luồng:

- Inventory → Squad Director → JSON teams → router proposal.
- Câu hỏi cross-domain → các seat liên quan → `atlas` merge → một đáp án.

Mỗi ví dụ cần input, expected shape, failure notes và cách chạy. Đây là cầu nối
còn thiếu giữa tài liệu mô tả và hành vi có thể xác nhận.

### P2 — governance

Thêm `CONTRIBUTING.md` nêu format artifact, checklist rename, cách chạy
validator/evaluation và yêu cầu cập nhật changelog. Thêm issue/PR template và
support/security policy nếu repo bắt đầu nhận contribution. Trạng thái
“all rights reserved” là quyết định hợp lệ, nhưng contributor vẫn cần biết họ
đang cấp quyền gì khi gửi thay đổi; nên ghi điều đó rõ trước khi nhận PR ngoài.

### P2 — changelog chỉ có một nguồn chuẩn

`CHANGELOG.md` và `docs/changelog.html` đang lưu cùng nội dung bằng tay, dễ lệch.
Nên coi Markdown là source of truth và sinh HTML trong CI/release. Validator có
thể kiểm tra generated file không dirty sau lệnh build.

### P2 — observability và versioning của artifact

Nếu agent được dùng ngoài repo, cần ghi lại artifact version, model, input,
route được chọn, tool call và kết quả guardrail. Không nhất thiết đưa tracing
SDK nặng vào thư viện Markdown; một JSONL event contract đơn giản cũng đủ để
điều tra regression. Version repo hiện chưa cho biết riêng agent nào thay đổi,
vì vậy manifest nên có version hoặc content hash cho từng artifact.

## Lộ trình đề xuất

### Trong 1 ngày

- Giữ CI validator chạy trên mọi push/PR.
- Bổ sung `CONTRIBUTING.md` và rename checklist.
- Chọn `CHANGELOG.md` làm nguồn duy nhất, sinh HTML tự động.

### Trong 1 tuần

- Thiết kế manifest/schema chung và migrate bốn agent trước.
- Thêm fixtures cùng test bất biến cho Squad Director v2.
- Viết hai ví dụ end-to-end ở trên.

### Trước khi gọi là production-ready

- Có model-backed evaluation với baseline và ngưỡng pass rõ ràng.
- Ghi trace/version cho mỗi lần chạy và có quy tắc xử lý dữ liệu nhạy cảm.
- Định nghĩa tool permission theo least privilege và approval boundary cho
  mọi agent có quyền ghi hoặc gọi dịch vụ ngoài.
- Có release checklist, compatibility policy và rollback path.

## Phương pháp và giới hạn

Review dựa trên inventory file, nội dung prompt/agent/skill, liên kết nội bộ,
lịch sử Git và cấu trúc quality gate. Repo tham chiếu được chọn vì là dự án
agent chính thức, trưởng thành và có các pattern docs/examples/tests/CI phù hợp
để đối chiếu. Môi trường review không truy cập được GitHub (HTTPS tunnel trả
`403`), nên không khóa đánh giá vào một snapshot mới clone ngày 2026-08-20;
đường dẫn tham chiếu được ghi rõ để lần review sau pin commit cụ thể. Những nhận
định về repo tham chiếu vì thế chỉ dùng ở mức pattern bền vững, không khẳng định
số file hay trạng thái branch tại thời điểm hiện tại.
