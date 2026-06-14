"""环境变量与配置（W2 周二起完善 Pydantic 模型）。"""

from pathlib import Path

from dotenv import load_dotenv

# python-ai/.env（与 p0-cli-chat 同级目录）
_ENV_PATH = Path(__file__).resolve().parents[2] / ".env"


def load_config() -> None:
    """加载 .env；未找到文件时不报错。"""
    load_dotenv(_ENV_PATH)

