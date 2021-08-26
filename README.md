

### 相關網站
-   http://plotly.com
-   http://viralml.com
-   https://getbootstrap.com/
-   https://finance.yahoo.com
-   https://plotly.com/python/reference/candlestick/


### Reference
-   For more information on candlestick attributes, see: https://plotly.com/python/reference/candlestick/

## Python 圖參考: candlestick跟踪(candlestick Traces)

一個plotly.graph_objects.Candlestick跟踪在圖中的一個圖形對象data與任何下面列出的命名參數或屬性列表。

燭台是一種金融圖表風格，描述給定“x”坐標（最可能的時間）的開盤價、最高價、最低價和收盤價。方框表示“開盤”和“收盤”值之間的價差，線條表示“低”和“高”值之間的價差，收盤價高於（低於）開盤價的樣本點稱為增加（減少）。默認情況下，增加的蠟燭以綠色繪製，而減少的蠟燭以紅色繪製。(該顏色台股剛好反向,可以自行設定)

**圖例名稱 name**

    代碼： fig.update_traces(name=<VALUE>, 
            selector=dict(type='candlestick'))
-   類型：字符串
-   設置跟踪名稱。跟踪名稱顯示為圖例項和懸停。

**可見的 visible**

    代碼： fig.update_traces(visible=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：枚舉，一個（True| False| "legendonly"）
-   默認： True
-   確定此跟踪是否可見。如果為“legendonly”，則不繪製軌跡，但可以作為圖例項出現（前提是圖例本身可見）。

**顯示圖例 showlegend**

    代碼： fig.update_traces(showlegend=<VALUE>, 
            selector=dict(type='candlestick'))
-   類型： boolean
-   默認值： True
-   確定與此跟踪對應的項目是否顯示在圖例中。

**圖例等級 legendrank**

    代碼： fig.update_traces(legendrank=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：數字
-   默認值： 1000
-   設置此跟踪的圖例等級。具有較小等級的項目和組顯示在頂部/左側，而“反向”`legend.traceorder` 它們位於底部/右側。默認的legendrank 是1000，這樣你就可以使用小於1000 的等級將某些項目放在所有未排名的項目之前，而大於1000 的排名則放在所有未排名的項目之後。

**圖例群組 legendgroup**

    代碼： fig.update_traces(legendgroup=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：字符串
-   默認值： ""
-   設置此跟踪的圖例組。切換圖例項時，同時跟踪同一圖例組隱藏/顯示的一部分。

**圖例抬頭標題 legendgrouptitle**

    代碼： fig.update_traces(legendgrouptitle=dict(...),         
            selector=dict(type='candlestick'))
-   類型：包含下面列出的一個或多個鍵的字典。
    -   **字體 font**
    
        代碼： * fig.update_traces(legendgrouptitle_font=dict(...), selector=dict(type='candlestick'))
        -   類型：包含下面列出的一個或多個鍵的字典。
設置此圖例組的標題字體。

    -   **顏色 color**

        代碼： fig.update_traces(legendgrouptitle_font_color=<VALUE>, selector=dict(type='candlestick'))
        -   類型：顏色
        
    -   **字形 family**
    
        代碼： fig.update_traces(legendgrouptitle_font_family=<VALUE>, selector=dict(type='candlestick'))
        -   類型：字符串
        -   HTML 字體系列 - 將由網絡瀏覽器應用的字體。網絡瀏覽器只有在其運行的系統上可用時才能應用該字體。提供以逗號分隔的多個字體系列，以指示在系統上不可用時應用字體的首選項。Chart Studio Cloud（位於 https://chart-studio.plotly.com 或內部部署）在服務器上生成圖像，其中僅安裝和支持選定數量的字體。其中包括“Arial”、“Balto”、“Courier New”、“Droid Sans”、“Droid Serif”、“Droid Sans Mono”、“Gravitas One”、“Old Standard TT”、“Open Sans”、“Overpass” ”、“PT Sans Narrow”、“Raleway”、“Times New Roman”。
        
    -   **尺寸 size**

        代碼： fig.update_traces(legendgrouptitle_font_size=<VALUE>, selector=dict(type='candlestick'))
        -   類型：大於或等於 1 的數字
        
**文本 text**

    代碼： fig.update_traces(legendgrouptitle_text=<VALUE>,        
                selector=dict(type='candlestick'))
-   類型：字符串
-   默認值： ""
-   設置圖例組的標題。

**透明度 opacity**

    代碼： fig.update_traces(opacity=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：介於或等於 0 和 1 之間的數字
-   默認值： 1
-   設置跟踪的不透明度。

**身份證 ids**

    代碼： fig.update_traces(ids=<VALUE>, selector=dict(type='candlestick'))
-   類型：列表、numpy 數組或 Pandas 系列的數字、字符串或日期時間。
為每個數據分配 id 標籤。這些 id 用於動畫期間數據點的對象恆定性。應該是一個字符串數組，而不是數字或任何其他類型。

**x**

    代碼： fig.update_traces(x=<VALUE>, selector=dict(type='candlestick'))
-   類型：列表、numpy 數組或 Pandas 系列的數字、字符串或日期時間。
設置 x 坐標。如果不存在，將生成線性坐標。

**收盤價 close**

    代碼： fig.update_traces(close=<VALUE>, 
        selector=dict(type='candlestick'))
-   類型：列表、numpy 數組或 Pandas 系列的數字、字符串或日期時間。
設置收盤價。

**開盤價 open**

    代碼： fig.update_traces(open=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：列表、numpy 數組或 Pandas 系列的數字、字符串或日期時間。
設置打開值。

**最高價 high**

    代碼： fig.update_traces(high=<VALUE>, selector=dict(type='candlestick'))
-   類型：列表、numpy 數組或 Pandas 系列的數字、字符串或日期時間。
設置高值。

**最低價 low**

    代碼： fig.update_traces(low=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：列表、numpy 數組或 Pandas 系列的數字、字符串或日期時間。
設置低值。

**文本 text**

    代碼： fig.update_traces(text=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：字符串或字符串數組
-   默認值： ""
-   設置與每個樣本點關聯的懸停文本元素。如果是單個字符串，則相同的字符串出現在所有數據點上。如果是字符串數組，則將項目映射到此跟踪的樣本點。

**懸停文本 hovertext**

    代碼： fig.update_traces(hovertext=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：字符串或字符串數組
-   默認值： "" 與“text”相同。

**懸停信息 hoverinfo**

    代碼： fig.update_traces(hoverinfo=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型： flaglist 字符串。"x"、"y"、"z"、"text"、"name"與"+"OR"all"或"none"or 的任意組合"skip"。
-   示例： "x" , "y", "x+y", "x+y+z","all"
-   默認值： "all"
-   確定在懸停時顯示哪些跟踪信息。如果設置了 `none` 或 `skip`，則懸停時不顯示任何信息。但是，如果設置了 `none`，點擊和懸停事件仍然會被觸發。

**x軸懸浮格式 xhoverformat**

    代碼： fig.update_traces(xhoverformat=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：字符串
-   默認值： ""
-   使用 d3 格式迷你語言設置 `x` 的懸停文本格式規則，這與 Python 中的非常相似。有關數字，請參閱：https://github.com/d3/d3-format/tree/v1.4.5#d3-format。
-   日期見：https://github.com/d3/d3-time-format/tree/v2.2.3#locale_format。我們向 d3 的日期格式化程序添加了兩項：“%h”表示半年的十進制數，以及“%{n}f”表示帶有 n 位數字的小數秒。例如，帶有刻度格式“%H~%M~%S.%2f”的“2016-10-13 09:15:23.456”將顯示“09~15~23.46”默認情況下，這些值使用`xaxis.hoverformat `.

**y軸懸浮格式 yhoverformat**

    代碼： fig.update_traces(yhoverformat=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：字符串
-   默認值： ""
-   使用與 Python 中的非常相似的 d3 格式迷你語言設置 `y` 的懸停文本格式規則。有關數字，請參閱：https://github.com/d3/d3-format/tree/v1.4.5#d3-format。
-   日期見：https://github.com/d3/d3-time-format/tree/v2.2.3#locale_format。我們向 d3 的日期格式化程序添加了兩項：“%h”表示半年的十進制數，以及“%{n}f”表示帶有 n 位數字的小數秒。例如，帶有刻度格式“%H~%M~%S.%2f”的“2016-10-13 09:15:23.456”將顯示“09~15~23.46”默認情況下，這些值使用`yaxis.hoverformat `.

**元 meta**

    代碼： fig.update_traces(meta=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：數字或分類坐標字符串
分配與此跟踪關聯的額外元信息，可用於各種文本屬性。軌跡`name`、圖形、軸和顏色條`title.text`、註釋`text`、`rangeselector`、`updatemenues`和`sliders``label`文本等屬性都支持`meta`。
-   要訪問同一跟踪中屬性中的跟踪“meta”值，只需使用“%{meta[i]}”，其中“i”是相關“meta”項的索引或鍵。
-   要訪問佈局屬性中的跟踪“meta”，請使用“%{data[n[.meta[i]}”，其中“i”是“meta”的索引或鍵，“n”是跟踪索引。

**自定義數據 customdata**

    代碼： fig.update_traces(customdata=<VALUE>, 
            selector=dict(type='candlestick'))
-   類型：列表、numpy 數組或 Pandas 系列的數字、字符串或日期時間。
為每個數據分配額外的數據。這在偵聽懸停、單擊和選擇事件時可能很有用。
-   請注意，“分散”跟踪還會在標記 DOM 元素中附加自定義數據項

**x軸 xaxis**

    代碼： fig.update_traces(xaxis=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型： subplotid
-   默認： x
-   設置此軌蹟的 x 坐標和 2D 笛卡爾 x 軸之間的參考。如果為“x”（默認值），則 x 坐標參考 `layout.xaxis`。如果是“x2”，則 x 坐標指的是 `layout.xaxis2`，依此類推。

**y軸 yaxis**

    代碼： fig.update_traces(yaxis=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型： subplotid
-   默認： y
-   設置此軌蹟的 y 坐標和 2D 笛卡爾 y 軸之間的參考。如果為“y”（默認值），則 y 坐標參考 `layout.yaxis`。如果是“y2”，則 y 坐標指的是 `layout.yaxis2`，依此類推。

**週期 xperiod**

    代碼： fig.update_traces(xperiod=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：數字或分類坐標字符串
-   默認值： 0
-   僅當軸“類型”為“日期”時才相關。在 x 軸上設置以毫秒或“M<n>”為單位的周期定位。“M<n>”形式的特殊值可用於聲明月數。在這種情況下，`n` 必須是一個正整數。

**週期對齊 xperiodalignment**

    代碼： fig.update_traces(xperiodalignment=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：枚舉，一個（"start"| "middle"| "end"）
-   默認： "middle"
-   僅當軸“類型”為“日期”時才相關。設置數據點在 x 軸上的對齊方式。

**X週期0 xperiod0**

    代碼： fig.update_traces(xperiod0=<VALUE>, selector=dict(type='candlestick'))
-   類型：數字或分類坐標字符串
僅當軸“類型”為“日期”時才相關。設置以毫秒為單位的周期定位基礎或 x0 軸上的日期字符串。
-   當 `x0period` 是整數週數時，默認情況下 `x0period0` 將在星期日，即 2000-01-02，否則它將在 2000-01-01。

**線 line**

    代碼： fig.update_traces(line=dict(...), selector=dict(type='candlestick'))
-   類型：包含下面列出的一個或多個鍵的字典。

     -   **線寬 line_width** 
     
       -    代碼： fig.update_traces(line_width=<VALUE>,  selector=dict(type='candlestick'))
    -    類型：大於或等於 0 的數字
    -   默認： 2
    -   設置邊界框線的寬度（以像素為單位）。請注意，此樣式設置也可以通過 `increasing.line.width` 和 `decreasing.line.width` 為每個方向設置。
    


**須寬 whiskerwidth**

    代碼： fig.update_traces(whiskerwidth=<VALUE>, selector=dict(type='candlestick'))
-   類型：介於或等於 0 和 1 之間的數字
-   默認值： 0
-   設置鬍鬚相對於框寬度的寬度。例如，對於 1，鬍鬚與盒子一樣寬。

**選定點 selectedpoints**

    代碼： fig.update_traces(selectedpoints=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：數字或分類坐標字符串
-   包含選定點的整數索引的數組。僅對支持選擇的跟踪有效。請注意，空數組意味著空選擇，其中所有點的“未選擇”都打開，而任何其他非數組值意味著“選擇”和“未選擇”樣式無效的所有選擇。

**增加 increasing**

    代碼： fig.update_traces(increasing=dict(...), selector=dict(type='candlestick'))
-   類型：包含下面列出的一個或多個鍵的字典。

**填色 fillcolor**

    代碼： fig.update_traces(increasing_fillcolor=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：顏色
-   設置填充顏色。默認為線條顏色、標記顏色或標記線條顏色的半透明變體，以可用者為準。

**線 line**

    代碼： fig.update_traces(increasing_line=dict(...),
                selector=dict(type='candlestick'))
-   類型：包含下面列出的一個或多個鍵的字典。

**顏色 color**

    代碼： fig.update_traces(increasing_line_color=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：顏色
-   默認值： "#3D9970"
-   設置框邊界線的顏色。

**寬度 width**

    代碼： fig.update_traces(increasing_line_width=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：大於或等於 0 的數字
-   默認： 2
-   設置邊界框線的寬度（以像素為單位）。

**減少 decreasing**

    代碼： fig.update_traces(decreasing=dict(...), 
                selector=dict(type='candlestick'))
-   類型：包含下面列出的一個或多個鍵的字典。

**填色 fillcolor**

    代碼： fig.update_traces(decreasing_fillcolor=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：顏色
-   設置填充顏色。默認為線條顏色、標記顏色或標記線條顏色的半透明變體，以可用者為準。

**線 line**

    代碼： fig.update_traces(decreasing_line=dict(...),
                selector=dict(type='candlestick'))
-   類型：包含下面列出的一個或多個鍵的字典。

**顏色 color**

    代碼： fig.update_traces(decreasing_line_color=<VALUE>,
        selector=dict(type='candlestick'))
-   類型：顏色
-   默認值： "#FF4136"
-   設置框邊界線的顏色。

**寬度 width**

    代碼： fig.update_traces(decreasing_line_width=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：大於或等於 0 的數字
-   默認： 2
-   設置邊界框線的寬度（以像素為單位）。

**懸停標籤 hoverlabel**

    代碼： fig.update_traces(hoverlabel=dict(...), 
                selector=dict(type='candlestick'))
-   類型：包含下面列出的一個或多個鍵的字典。

**對齊 align**

    編碼： fig.update_traces(hoverlabel_align=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：枚舉或enumerateds的陣列的一個（"left"| "right"| "auto"）
-   默認值： "auto"
-   設置懸停標籤框中文本內容的水平對齊方式。僅當懸停標籤文本跨越兩行或更多行時才有效

**背景色 bgcolor**

    代碼： fig.update_traces(hoverlabel_bgcolor=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：顏色或顏色數組
-   設置此跟踪的懸停標籤的背景顏色

**邊框顏色 bordercolor**

    代碼： fig.update_traces(hoverlabel_bordercolor=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：顏色或顏色數組
-   設置此跟踪的懸停標籤的邊框顏色。

**字體 font**

    代碼： fig.update_traces(hoverlabel_font=dict(...),
                selector=dict(type='candlestick'))
-   類型：包含下面列出的一個或多個鍵的字典。
-   設置懸停標籤中使用的字體。

**顏色 color**

    代碼： fig.update_traces(hoverlabel_font_color=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：顏色或顏色數組

**字型集 family**

    代碼： fig.update_traces(hoverlabel_font_family=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：字符串或字符串數組
-   HTML 字體系列 - 將由網絡瀏覽器應用的字體。網絡瀏覽器只有在其運行的系統上可用時才能應用該字體。提供以逗號分隔的多個字體系列，以指示在系統上不可用時應用字體的首選項。
-   Chart Studio Cloud（位於 https://chart-studio.plotly.com 或內部部署）在服務器上生成圖像，其中僅安裝和支持選定數量的字體。
-   其中包括“Arial”、“Balto”、“Courier New”、“Droid Sans”、“Droid Serif”、“Droid Sans Mono”、“Gravitas One”、“Old Standard TT”、“Open Sans”、“Overpass” ”、“PT Sans Narrow”、“Raleway”、“Times New Roman”。

**尺寸 size**

    代碼： fig.update_traces(hoverlabel_font_size=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：大於或等於 1 的數字或數字數組

**名稱長度 namelength**

    代碼： fig.update_traces(hoverlabel_namelength=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：整數或大於或等於 -1 的整數數組
-   默認值： 15
-   在所有跟踪的懸停標籤中設置跟踪名稱的默認長度（以字符數表示）。-1 顯示全名而不考慮長度。0-3 顯示前 0-3 個字符，如果小於那麼多字符，則大於 3 的整數將顯示整個名稱，但如果它更長，將截斷為 `namelength - 3` 個字符並添加省略號。

**分裂 split**

    代碼： fig.update_traces(hoverlabel_split=<VALUE>,
                selector=dict(type='candlestick'))
-   類型：布爾型
-   在單獨的標籤中顯示懸停信息（開盤價、收盤價、最高價、最低價）。

**X日曆 xcalendar**

    代碼： fig.update_traces(xcalendar=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：枚舉，一個（"chinese"| "coptic"| "discworld"| "ethiopian"| "gregorian"| "hebrew"| "islamic"| "jalali"| "julian"| "mayan"| "nanakshahi"| "nepali"| "persian"| "taiwan"| "thai"| "ummalqura"）
-   默認： "gregorian"
-   設置日曆系統以使用 `x` 日期數據。

**版本 uirevision**

    代碼： fig.update_traces(uirevision=<VALUE>, 
                selector=dict(type='candlestick'))
-   類型：數字或分類坐標字符串
-   控制一些用戶驅動的跟踪更改的持久性：`parcoords` 跟踪中的`constraintrange`，以及一些`editable: True` 修改，例如`name` 和`colorbar.title`。默認為`layout.uirevision`。
-   請注意，其他用戶驅動的跟踪屬性更改由`layout` 屬性控制：`trace.visible` 由`layout.legend.uirevision` 控制，`selectedpoints` 由`layout.selectionrevision` 和`colorbar 控制。（ x|y)`（可通過 `config: {editable: True}` 訪問）由 `layout.editrevision` 控制。
-   跟踪更改由 `uid` 跟踪，如果沒有提供 `uid`，它只會回退到跟踪索引。因此，如果您的應用程序可以在 `data` 數組末尾之前添加/刪除跟踪，以便相同的跟踪具有不同的索引，