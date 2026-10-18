---
title: "Atlassian工程师公开基础设施架构"
author: "marcus (@marcusyul)"
url: https://x.com/marcusyul/status/2061792686927909105
source: X
published: 2026-06-02 12:50 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 其他
roots: []
---

## 原文

atlassian factura $1.79 mil millones al trimestre.

despidieron al ingeniero que construyó su infraestructura.

¿la respuesta del ingeniero? publicar un vídeo de 38 minutos contando exactamente cómo lo hizo.

gratis, para todo el mundo.

lo que reveló:
→ Envoy proxy en vez de load balancers de empresa
→ arquitectura sidecar para auth, logs y rate limits
→ DynamoDB + SQS para aprovisionamiento asíncrono
→ Packer + SaltStack para desplegar VMs a escala

atlassian cobraba a 350.000 clientes diferentes.

el señor que lo diseñó acaba de darte el mismo manual por cero dólares.

sí, 0$.

les acaba de destruir.

guarda esto. https://t.co/IR2KeLLtwu

> 媒体：
> - https://video.twimg.com/amplify_video/2055120600625029120/vid/avc1/480x270/x8m8b7F8pMoQwmwo.mp4?tag=27

## 溯源

