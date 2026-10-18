---
title: "ZCode 回应安全问题并开源代码"
author: "ZCode (@zcode_ai)"
url: https://x.com/zcode_ai/status/2101844704933621971
source: X
published: 2026-09-21 01:23 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

In response to the ZCode product security issues reported by the community, we have completed the necessary remediation and sincerely apologize to all our users.

We have open-sourced ZCode at https://t.co/oADgletuha, placing the code under community scrutiny and making ZCode more open and transparent.

We sincerely thank the community developers who previously identified issues in ZCode. Going forward, we will establish an ongoing product security vulnerability reporting and response process. We welcome developers to continue reviewing ZCode and reporting potential issues, and we will provide rewards based on the severity of the issues reported.

With respect to the code data referenced by the community, we confirm that no such data is retained and that it has never been used for model training.

Following the remediation, we invited the China Academy of Information and Communications Technology (CAICT) and NSFOCUS to conduct security assessments. The results are as follows:

Through its technical assessment, CAICT confirmed that the zcode-prod Alibaba Cloud OSS bucket is in a zero-data state. Security remediation has been completed in the ZCode v3.14.0 client. The Repo Wiki feature has been removed, and the workflow for generating and uploading local repository snapshots has been disabled.

NSFOCUS confirmed that all data objects in the zcode-prod Alibaba Cloud OSS bucket, as well as the bucket itself, have been deleted. Remediation has been completed in the ZCode v3.14.0 client. The Repo Wiki entry point and the associated generation workflow have been removed, and no functional path capable of triggering the generation of local repository snapshots or transmitting local files externally was identified.

Once again, we sincerely apologize and welcome continued scrutiny from the community. The full security assessment report will be released soon.

## 溯源

