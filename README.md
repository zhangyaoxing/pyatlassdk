# pyatlassdk

MongoDB Atlas Administration API 的 Python SDK，自动生成。

> `src/pyatlassdk/` 下的文件由 [mongo-atlas-sdk](https://github.com/zhangyaoxing/mongo-atlas-sdk) 生成，请勿手动修改。

## 安装

```bash
pip install pyatlassdk
```

## 使用

```python
from pyatlassdk import AtlasClient
from pyatlassdk.models.cluster_description20240805 import ClusterDescription20240805

with AtlasClient(public_key="...", private_key="...") as client:
    cluster = client.clusters.create_group_cluster(
        group_id="...",
        body=ClusterDescription20240805(name="demo", cluster_type="REPLICASET"),
    )
```

- 认证：Atlas API 公钥/私钥，使用 HTTP Digest。
- 模型：pydantic v2，字段使用 snake_case，序列化时按 Atlas 原始字段名（alias）输出。
- 资源：55 个分类类，每个端点一个方法，方法名来自 `operationId`。

## 重新生成

在主仓库 `mongo-atlas-sdk` 中执行：

```bash
uv run mongo-atlas crawl       # 抓取 OpenAPI 文档
uv run mongo-atlas normalize   # 归一化
uv run mongo-atlas pygen      # 用模板写入 pyatlassdk/src/pyatlassdk
```

然后用本仓库提交并发布：

```bash
uv build
uv publish
```

## 开发

```bash
uv sync
uv run pytest
```
