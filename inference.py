# -*- coding: utf-8 -*-
"""NCW v0.1 推理脚本：加载 Qwen2.5-7B-Instruct + LoRA adapter 并生成正文。"""
import argparse
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel


def main():
    parser = argparse.ArgumentParser(description="NCW v0.1 inference")
    parser.add_argument("--base_model", required=True, help="Qwen2.5-7B-Instruct 路径")
    parser.add_argument("--adapter", required=True, help="LoRA checkpoint 路径")
    parser.add_argument("--prompt", default=None, help="单次生成 prompt")
    parser.add_argument("--interactive", action="store_true", help="交互式输入")
    parser.add_argument("--max_new_tokens", type=int, default=1000)
    args = parser.parse_args()

    tokenizer = AutoTokenizer.from_pretrained(args.base_model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.base_model,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    model = PeftModel.from_pretrained(model, args.adapter)
    model.eval()

    gen_kwargs = dict(
        max_new_tokens=args.max_new_tokens,
        do_sample=True,
        temperature=0.9,
        top_p=0.9,
        top_k=40,
        repetition_penalty=1.15,
    )

    def generate(prompt: str) -> str:
        messages = [{"role": "user", "content": prompt}]
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(text, return_tensors="pt").to(model.device)
        with torch.no_grad():
            output = model.generate(**inputs, **gen_kwargs)
        new_ids = output[0][inputs.input_ids.shape[-1]:]
        return tokenizer.decode(new_ids, skip_special_tokens=True)

    if args.interactive:
        print("输入 prompt 后回车生成；输入 exit 退出。")
        while True:
            prompt = input(">>> ").strip()
            if prompt.lower() in ("exit", "quit"):
                break
            if not prompt:
                continue
            print(generate(prompt))
            print()
    else:
        if not args.prompt:
            parser.error("需要 --prompt 或 --interactive")
        print(generate(args.prompt))


if __name__ == "__main__":
    main()
