# 引句原文比對（2026-10-15）

工具：tools/check_research_quotes.py（curl 抓原始網頁／PDF，比對引句前 8 個英文字）。WebFetch 回傳的是模型轉述，不能當原文。

另經手動查原文確認：S02（PMC6873141）、S12（PDF 換行造成失配）、S16、S24、S52、S53、S54。

```
S01	ok	1	1
S02	none	0	1
S03	ok	1	1
S04	ok	5	5
S05	no-url-or-no-english-quote	0	0
S06	ok	2	2
S07	ok	4	4
S08	ok	1	1
S09	partial	1	2
S10	ok	7	7
S11	ok	4	4
S12	none	0	8
S13	ok	2	2
S14	ok	2	2
S15	ok	3	3
S16	none	0	2
S17	partial	1	2
S18	ok	2	2
S19	partial	1	3
S20	ok	5	5
S21	partial	2	3
S22	ok	2	2
S23	partial	2	4
S24	none	0	1
S25	ok	2	2
S26	partial	3	5
S27	ok	5	5
S28	partial	3	4
S29	ok	5	5
S30	ok	4	4
S31	ok	9	9
S32	empty-page	0	5
S33	ok	2	2
S34	ok	3	3
S35	ok	4	4
S36	ok	6	6
S37	ok	2	2
S38	ok	4	4
S39	ok	6	6
S40	no-url-or-no-english-quote	0	0
S41	ok	4	4
S42	ok	2	2
S43	ok	2	2
S44	partial	2	3
S45	ok	2	2
S46	ok	6	6
S47	partial	18	20
S48	ok	5	5
S49	ok	4	4
S50	partial	3	4
S51	no-url-or-no-english-quote	0	0
S52	empty-page	0	2
S53	empty-page	0	3
S54	empty-page	0	5
S55	none	0	1
```
