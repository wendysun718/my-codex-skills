# One fictional example per new database

Clearly label the row and its page as fictional. These fixed dates are sample values, not current job deadlines. Do not fetch the placeholder URL.

| Chinese field | Chinese value | English field | English value |
| --- | --- | --- | --- |
| 公司 | 示例公司（虚构） | Organization | Example Company (Fictional) |
| 岗位 | 商业分析实习生 | Role | Business Analyst Intern |
| 工作授权 | CPT：未说明；OPT：未说明；申请者现在及未来均不得需要签证担保 | Work Authorization | CPT: Not stated; OPT: Not stated; must not require sponsorship now or in the future |
| 申请开放日期 | 2026-09-01 | App Opens | 2026-09-01 |
| 申请截止日期 | 2026-10-15 | App Due | 2026-10-15 |
| 申请链接 | https://example.com/jobs/business-analyst-intern | Link to Apply | https://example.com/jobs/business-analyst-intern |
| 申请状态 | 待申请 | Status | Target |
| 已提交 | 未勾选（示例中尚未投递） | Submitted | Unchecked (not yet applied in the example) |
| 下一步行动 | 建议：2026-09-25 前确认 CPT / OPT 是否接受 | Next Action | Suggested: Clarify CPT / OPT acceptance by 2026-09-25 |
| 备注 | 虚构示例；链接为占位；行动日期为个人计划 | Notes | Fictional example; placeholder URL; action date is a personal target |

## Fictional original JD

Example Company - Business Analyst Intern. Applications open September 1, 2026 and close October 15, 2026.

Required: Currently pursuing a bachelor's or master's degree in Business Analytics, Statistics, or a related field; graduating between May 2027 and June 2028; ability to write SQL JOINs and aggregation queries; proficiency with Excel pivot tables and lookup functions; ability to clean data and check data quality; ability to explain findings to non-technical teams.

Preferred: Python or R; Tableau or Power BI; at least one data analysis project or relevant internship.

Conditions: 20 hours per week for 12 consecutive weeks; onsite in Los Angeles at least two days per week; applicants must not require employer visa sponsorship now or in the future.

## Detail-page rendering

Create 6 Required bullets, 3 Preferred bullets, and 3 Other Conditions bullets from this text, in the selected output language. Retain both tools in each OR pair, both numeric bounds of the graduation window, hours AND duration, and the two-day onsite condition. Keep the full fictional JD in Original JD. Work Authorization must say CPT and OPT are not stated and quote the exact sponsorship sentence. Application Updates states that the fictional role has not been applied to, there is no confirmation or contact, and the next action is a suggested personal plan.

## Small review cases

- Input says only "No sponsorship available": CPT and OPT remain Not stated; do not invent a now/future applicant ban.
- Input contains only a posted date: App Opens stays empty.
- A cropped screenshot omits the bottom of a JD: mark incomplete, never claim all requirements are covered.
- The same requisition arrives again with a confirmation email: update the matching row, preserve requirements and notes, mark Submitted only from the confirmation evidence.
- Two roles share the same employer and title but have different requisition IDs: keep separate records.
