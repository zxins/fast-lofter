1. 初始化
```
alembic init alembic
```

2.创建更新脚本
```
alembic revision --autogenerate -m "XXXXXX"
```

3.提交修改
```
alembic upgrade head
```