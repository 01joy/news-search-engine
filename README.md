# 新闻搜索引擎
<img src="./news_search_engine3.png" width = "650" align=center />

# 使用方法
1. 安装python 3.4+环境（推荐[Anaconda](https://www.anaconda.com/distribution/)或[Miniconda](https://docs.conda.io/en/latest/miniconda.html)）
2. 安装lxml html解析器，命令为`pip install lxml`
3. 安装jieba分词组件，命令为`pip install jieba`
4. 安装Flask Web框架，命令为`pip install Flask`
5. 进入web文件夹，运行main.py文件
6. 打开浏览器，访问http://127.0.0.1:5000/ 输入关键词开始测试

如果想抓取最新新闻数据并构建索引，一键运行`./code/setup.py`，再按上面的方法测试。

2020.4.5：新增抓取[中国新闻网](http://www.chinanews.com/scroll-news/news1.html)的爬虫程序。先运行`./code/spider.chinanews.com.py`爬取最近5天新闻（约2500条）；然后注释`./code/setup.py`[第38行](https://github.com/01joy/news-search-engine/blob/master/code/setup.py#L38)并运行，自动构建索引。

# 项目介绍
1. [和我一起构建搜索引擎（一）简介](http://bitjoy.net/2016/01/04/introduction-to-building-a-search-engine-1/)
2. [和我一起构建搜索引擎（二）网络爬虫](http://bitjoy.net/2016/01/04/introduction-to-building-a-search-engine-2/)
3. [和我一起构建搜索引擎（三）构建索引](http://bitjoy.net/2016/01/07/introduction-to-building-a-search-engine-3/)
4. [和我一起构建搜索引擎（四）检索模型](http://bitjoy.net/2016/01/07/introduction-to-building-a-search-engine-4/)
5. [和我一起构建搜索引擎（五）推荐阅读](http://bitjoy.net/2016/01/09/introduction-to-building-a-search-engine-5/)
6. [和我一起构建搜索引擎（六）系统展示](http://bitjoy.net/2016/01/09/introduction-to-building-a-search-engine-6/)
7. [和我一起构建搜索引擎（七）总结展望](http://bitjoy.net/2016/01/09/introduction-to-building-a-search-engine-7/)
8. [和我一起构建搜索引擎（八）更新爬虫&修改打分&线上部署](https://bitjoy.net/2020/04/05/introduction-to-building-a-search-engine-8//)

# 感谢
* [jieba](https://github.com/fxsjy/jieba)
* [scikit-learn](https://github.com/scikit-learn/scikit-learn)
* [flask](https://github.com/mitsuhiko/flask)