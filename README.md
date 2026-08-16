# NCW v0.1

> ⚠️ **非正式版声明**
> 这是 NCW 项目的第一版（v0.1），用于功能验证与效果展示，**不是正式版**。
> 当前仅支持单轮生成；多人长文尾部偶有重复、偶发错字。后续版本会逐步修复这些问题，并加入多轮对话等能力。

NCW 是一个中文二次元场景长文生成 LoRA 模型，基于 [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) 微调。输入一句中文自然语言描述，输出约 400~1000 字的中文画面描写。

## 能力

- 中文口语 / 自然语言 → 二次元画面长文
- 支持 `safe` / `sensitive` / `nsfw` / `explicit` 四个分级（按输入意图生成对应内容）
- 支持单人、多人场景

## 快速开始

```bash
pip install -r requirements.txt
python inference.py \
  --base_model /path/to/Qwen2.5-7B-Instruct \
  --adapter /path/to/checkpoint-xxx \
  --prompt "写一个少女在教室值日，夕阳照进空教室"
```

## 推理参数

| 参数 | 值 |
| --- | --- |
| temperature | 0.9 |
| top_p | 0.9 |
| top_k | 40 |
| repetition_penalty | 1.15 ~ 1.2 |
| max_new_tokens | 1000 |

## 示例

完整输入 / 输出示例见 [examples.md](examples.md)。

## 内容分级与安全声明

本模型可生成包含成人向内容的长文，输出档位由输入意图决定。仅限研究与合规用途，请遵守当地法律法规和所在平台的内容政策。公开示例与样例数据只包含 `safe` 内容，`sensitive` / `nsfw` / `explicit` 正文未放入公开仓库。

## 训练

训练配置见 [training_config.yaml](training_config.yaml)，数据格式见 [data/README.md](data/README.md)。

## 许可证

Apache-2.0，与底座模型 Qwen2.5-7B-Instruct 一致。详见 [LICENSE](LICENSE)。
