from __future__ import annotations

from bt_api_base.error import ErrorTranslator, UnifiedErrorCode


class BitunixErrorTranslator(ErrorTranslator):
    @staticmethod
    def translate(error_code: int | str | None, response: dict | None = None) -> UnifiedErrorCode:
        if response is None:
            response = {}
        message = str(response.get("msg", "")) or str(response.get("message", ""))
        code_str = str(error_code) if error_code is not None else ""

        if code_str == "0" or "success" in message.lower():
            return UnifiedErrorCode.SUCCESS
        if "insufficient" in message.lower():
            return UnifiedErrorCode.INSUFFICIENT_BALANCE
        if "not_found" in message.lower() or "not found" in message.lower():
            return UnifiedErrorCode.ORDER_NOT_FOUND
        if "cancel" in message.lower():
            return UnifiedErrorCode.ORDER_ALREADY_CANCELLED

        return UnifiedErrorCode.UNKNOWN_ERROR
