# 数据说明

## 格式

训练数据为 LlamaFactory ShareGPT 格式的 JSONL，每条一行：

```json
{"conversations": [
  {"from": "human", "value": "中文自然语言画面描述"},
  {"from": "gpt", "value": "中文正文（400~1000 字）"}
]}
```

`from` / `value` 与 `human` / `gpt` 的映射在 LlamaFactory 的 `dataset_info.json` 中配置：

```json
"ncw_essay": {
  "file_name": "ncw_essay.jsonl",
  "formatting": "sharegpt",
  "columns": {"messages": "conversations"},
  "tags": {
    "role_tag": "from",
    "content_tag": "value",
    "user_tag": "human",
    "assistant_tag": "gpt"
  }
}
```

## 数据规模

- 完整训练集：5874 条
- 档位分布：safe 1475 / sensitive 1489 / nsfw 1414 / explicit 1496

## 公开策略

- 完整数据集包含成人向内容，未放入公开仓库。
- 本目录仅提供 30 条 safe 样例（`sample_safe_30.jsonl`），用于展示数据格式。
- 如需完整数据，请另行联系或在合规前提下自建。
