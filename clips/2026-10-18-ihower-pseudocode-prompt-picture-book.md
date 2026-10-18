---
title: "用伪代码提示词让 GPT-4o 生成绘本"
author: "ihower (@ihower)"
url: https://x.com/ihower/status/1801537916222771613
source: X
published: 2024-06-14 08:51 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 提示词与写作
roots: []
---

## 原文

尹相志老師用 GPT-4o 偽代碼的方式做繪本生成，真的是見鬼了，這樣也行，超強。

透過偽代碼可以讓模型更能執行複雜的控制流程，例如 for loop 迴圈中呼叫自訂 function。

實際的 prompt 如下，可產生15頁畫風一致的小蝌蚪繪本 (實際執行若 gpt-4o 停下來，請輸入繼續即可):

story=(請你角色扮演成一個暢銷的童書繪本作家，你擅長以孩童的純真眼光看這世界，製作出許多溫暖人心的作品。請以一隻與家人失散，不知道自己是甚麼的小蝌蚪，每次看到跟自己身體一部分相像，他就誤以為是同類，隨著他身體逐漸發展變化，他反而越來越迷惘，故事最後才遇到青蛙，這是一個調整自我認知的故事。) 
print(story) 

pages=(將故事大綱細分至預計15個跨頁的篇幅，每頁需要包括(text，image_prompt)，第13頁才可以出現青蛙，在這之前應該要讓小蝌蚪的自我認知旅程更多元化) print(pages) 
style_base=(基於以上故事，請思考大方向上你想要呈現的視覺效果，這是你用來統一整體繪本風格的描述，請盡量精簡，使用英文撰寫) 
print(style_base以及將style_base翻譯成中文) 

def image_generation(image_prompt, style_base): 
   final_prompt=請根據[image_prompt]以及[style_base]補充色調、背景描述、具體風格、畫面細節，以及主角小蝌蚪目前的顏色(一開始是黑色)、體型(沒有腳的蝌蚪直接叫做a tadpole即可)、尾巴長短，有幾隻腳必須具體的描述，同時至少3個效果詞(光照效果、色彩色調、渲染效果、視覺風格)和1個以上的構圖技巧，以構成完整的prompt，請設定隨機種子值為42，且不要有文字出現在圖中，使用英文撰寫
  
  請根據以下引數內容{size="1792x1024",n=1,prompt=final_prompt}來調用內部工具dalle以生成並展示圖片 
  
這不是個python任務 請實際執行此偽代碼為每頁生成圖片，確保必須等待該頁圖像生成後，才可以進行下一頁的操作 

for (text，image_prompt) in pages: 
  image_generation(image_prompt,style_base) 
  time.sleep(5)

> 媒体：
> - https://pbs.twimg.com/media/GQBYfTzbEAMCwX7.jpg

## 溯源

