import contextvars
import threading

thread_local = threading.local()
current_info = contextvars.ContextVar("info")
current_root = contextvars.ContextVar("root")


def capture_request_middleware(next_middleware, root, info, *args, **kwds):
    """
    This middleware should be placed at the very top of the middleware stack.
    Selects the proper information from the request and stores it in thread local
    """
    thread_local.info = info
    thread_local.root = root

    current_info.set(info)
    current_root.set(root)
    return next_middleware(root, info, *args, **kwds)


class CaptureRequestMiddleware:
    """
    This middleware should be placed at the very top of the middleware stack.
    Selects the proper information from the request and stores it in thread local
    """

    def resolve(self, next, root, info, **kwargs):
        """relove next"""
        thread_local.info = info
        thread_local.root = root
        current_info.set(info)
        current_root.set(root)
        return next(root, info, **kwargs)
