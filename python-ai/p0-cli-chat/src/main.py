"""Typer CLI 入口。"""

import typer

from src.config import load_config

app = typer.Typer(help="P0 多轮 CLI 对话")


@app.callback(invoke_without_command=True)
def chat() -> None:
    """启动对话（W2 周三起实现）。"""
    load_config()
    typer.echo("p0-cli-chat 已就绪。W2 周三：接入 OpenAI SDK 非流式对话。")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
