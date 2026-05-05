import requests
import logging

logger = logging.getLogger(__name__)

class HttpStatClient:
    BASE_URL: str = "https://tools-httpstatus.pickup-services.com/"

    def make_request(self, status_code: int) -> None:
        url: str = f"{self.BASE_URL}/{status_code}"
        response: requests.Response = requests.get(url, allow_redirects=False)
        
        status: int = response.status_code

        if 100 <= status < 400:
            content: str = response.text.strip() or "[Empty Body]"
            logger.info(f"Статус: {status} | Тело: {content}")
        elif 400 <= status < 600:
            raise requests.exceptions.HTTPError(
                f"Request failed with status {status}", 
                response=response
            )