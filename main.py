from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.llms.llama_cpp.llama_utils import (
    messages_to_prompt,
    completion_to_prompt,
)

model_url = "https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q5_K_M.gguf"

llm = LlamaCPP(
    # 事前にダウンロードしたモデルを使用する場合は、model_urlの代わりにmodel_pathを使用する
    model_url=model_url,
    temperature=0.1,
    # 生成する最大のトークン数
    max_new_tokens=256,
    # 入力可能なトークン数
    context_window=2000,
    # kwargs to pass to __call__() : 推論中に渡す必要があるキーワード引数を指定
    generate_kwargs={},
    # kwargs to pass to __init__() : 初期化時に渡す必要があるキーワード引数を指定
    # set to at least 1 to use GPU
    model_kwargs={"n_gpu_layers": 1},
    # プロンプトをフォーマット
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    # 実行時にログを出力
    verbose=True,
)

response = llm.complete("Hello! Can you tell me a poem about cats and dogs?")
print(response.text)