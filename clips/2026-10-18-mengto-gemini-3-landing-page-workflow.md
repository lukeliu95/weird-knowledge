---
title: "用Gemini 3从头做落地页的流程"
author: "Meng To (@MengTo)"
url: https://x.com/MengTo/status/1995865589446054102
source: X
published: 2025-12-02 14:40 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 设计与前端
roots: []
---

## 原文

How I created these landing pages with Gemini 3 from start to finish

First, I start with the hero section. It includes the nav bar, eyebrow, headline, subheadline, cta, social proof and visual. I spend 50% of the time here because it sets the colors, typography, spacing, which AI uses for the rest of the site consistently.

“Create the hero section for my {app} called {name} in the style of {reference_site}”.

Pro tip: use a screenshot and you’ll get way better results.

Let’s get into the details.

For icons, I prompt: “Use Iconify {icon set name}”. Most people use Lucide, but there are hundreds of open-source sets on Iconify like Solar, HeroIcons, Iconoir, Phosphor, etc. Just need to mention in the prompt. Same for custom fonts.

For the animation, I prompt: “Animate fade in, slide in, blur in, element by element. Use 'both' instead of 'forwards'. Don't use opacity 0.”. This creates a subtle intro animation the first time users land on your page.

Gemini 3 is an excellent animator. For example, I created the beam animation with this prompt: “Add noodles that connect and beam animate into the right circle. Add subtle details to the right beam animation circle with sonar and decorations.”

For background animation, I use Unicorn Studio. Remix one of their templates and watch people click on your cover like crazy. What can I say, people love lasers.

In the hero or right below it, social proof is super important. You can put ratings or logos, or both. For logos, you can prompt: “Animate the logos with marquee animation looping infinitely using duplicated items and alpha mask.”.

Now the CTA. AI always creates basic buttons, which is fine 99% of the time. But Gemini 3 now sets a high bar for baseline design, so you will need to stand out. That’s why I put the extra human touch on animations and lickable buttons. I suggest browsing UIVerse and Codepen for buttons and reference the code in your prompt: “Change main button {code} and secondary button {code}. Add a 1px border beam animation around the pill-shaped main button on hover.”.

Once you’re happy with the hero, you’ll want to craft new sections based on your business. Features, action plan, pricing, testimonials, FAQ, CTA and footer are the popular ones. Insert a screenshot and prompt “Adapt a new section, change texts, names and numbers”. Gemini 3 is very smart. It reads your existing styles and site concept and will tastefully mold new designs to fit perfectly into your current site.

Finally, repeat the same prompts for icons, buttons and animations. Use midjourney images and remix using Nano Banana Pro. Ask ChatGPT to come up with better headlines, features, ctas, etc. Don’t skip the human part, this is where you’re irreplaceable. Start prompting top-tier landing pages and watch your numbers grow.

> 媒体：
> - https://video.twimg.com/amplify_video/1995864236451561473/vid/avc1/360x270/U9gdZoP6JC45PvNx.mp4?tag=21

## 溯源

