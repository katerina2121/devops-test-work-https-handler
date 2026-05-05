import logging
from typing import List
from src.clients import HttpStatClient

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def main() -> None:
    client = HttpStatClient()
    test_codes: List[int] = [100, 201, 301, 404, 500]

    for code in test_codes:
        logger.info(f"Проверка кода: {code}")
        try:
            client.make_request(code)
        except Exception as e:
            logger.error(f"Сгенерировано исключение: {e}")
        print("-" * 30)

if __name__ == "__main__":
    main()