## 利用 celery 实现 多任务爬虫案例

1. 使用 celery + rabbmitmq 来发布任务
1. 使用 selenium 加上 headless chrome 来爬取结果

#### 测试爬取 [17ce](https://www.17ce.com/) 不同的网址测试结果

tornado 搭建的简易网页测试路由

1. first start rabbmit-server
1. `celery -A scheduler worker --loglevel=info`
1. `python run.py`


