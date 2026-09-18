# Localized database schema

Names: **求职申请追踪表** / **Job Application Tracker**.

| Order | Chinese | English | Type | Rule |
| --- | --- | --- | --- | --- |
| 1 | 公司 | Organization | Title | Employer name; separate rows for distinct roles. |
| 2 | 岗位 | Role | Text | Exact title, level, and program name if given. |
| 3 | 工作授权 | Work Authorization | Text | CPT, OPT, sponsorship on separate lines; retain consequential restrictions. |
| 4 | 申请开放日期 | App Opens | Date | Explicit opening date only; posted date is not automatically an opening date. |
| 5 | 申请截止日期 | App Due | Date | Explicit deadline; preserve time zone when provided. Unknown stays empty. Rolling recruitment goes in Notes. |
| 6 | 申请链接 | Link to Apply | URL | Actual application URL if supplied or verified; never fabricate one for a real role. |
| 7 | 申请状态 | Status | Select | Evidence-backed stage using the options below. |
| 8 | 已提交 | Submitted | Checkbox | Check only with submission evidence. Unknown unchecked must be accompanied by a note that submission is unconfirmed. |
| 9 | 下一步行动 | Next Action | Text | Concrete action and known date. Label proposed actions and personal target dates. |
| 10 | 备注 | Notes | Text | Short caveats, special conditions, and uncertainty; long requirements belong in the page. |

## Status options

| Chinese | English | Color |
| --- | --- | --- |
| 待申请 | Target | gray |
| 准备中 | Preparing | yellow |
| 已投递 | Applied | blue |
| 测评中 | Assessment | orange |
| 面试中 | Interviewing | purple |
| 已获录用 | Offer | green |
| 未录用 | Rejected | red |
| 已关闭 | Closed | gray |

For newly saved target jobs known to be unsubmitted, use Target and unchecked. For unknown history, leave Status empty and note the uncertainty. Rejection, closure, or an interview does not by itself prove an application was submitted; preserve or seek submission evidence. Do not downgrade a later stage because an older email arrives. Preserve the date and source of updates in the body.

## Notion tool adaptation

Use the current tool's accepted schema rather than assuming a specific MCP version. If the connector accepts SQL DDL, map Title to TITLE, Text to RICH_TEXT, Date to DATE, URL to URL, Select to SELECT with the localized options, and Checkbox to CHECKBOX. Exactly one title property avoids an extra auto-created Name column.

After creation, fetch the returned database to obtain its actual data-source ID and view ID. Set all 10 visible fields explicitly in order; creation order alone may not control display order. Wrap cells and freeze the first two columns when supported. Use the fetched property's write format for dates and checkboxes. With SQLite-style Notion properties, dates use date:PROPERTY:start and optional is_datetime, and checkboxes use __YES__ or __NO__.

Do not embed personal workspace IDs in reusable instructions. A matching database name is not sufficient to prove the correct destination; retain and verify the actual ID.

## Page headings

| Chinese | English |
| --- | --- |
| 岗位要求 | What They're Looking For |
| 必须具备 | Required |
| 加分条件 | Preferred |
| 其他条件 | Other Conditions |
| 工作授权 | Work Authorization |
| 原始 JD | Original JD |
| 申请进展 | Application Updates |

Omit unsupported requirement categories rather than filling them with invented qualifications. Preserve source excerpts in their original language.
