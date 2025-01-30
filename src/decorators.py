def log(filename: str = "") -> any:
    """logs whatever error occurs"""

    def decor_logger(func: any) -> any:
        def logg(*args, **kwargs):
            if not filename:
                print("Log file isn't assigned, log to console instead...")
                try:
                    result = func(*args, **kwargs)
                    print(f"{func.__name__} success | Args: {args} | Kwargs: {kwargs}")
                    return result
                except Exception as e:
                    print(f"{func.__name__} FAILED: {e} | Args: {args} | Kwargs: {kwargs}")
                    raise

            else:
                try:
                    with open(filename, "a") as f:
                        try:
                            result = func(*args, **kwargs)
                            f.write(f"{func.__name__} success | Args: {args} | Kwargs: {kwargs}\n")
                            return result
                        except Exception as e:
                            f.write(f"{func.__name__} FAILED: {e} | Args: {args} | Kwargs: {kwargs}\n")
                            raise

                except FileNotFoundError:
                    with open(filename, "w") as f:
                        pass
                    return logg(*args, **kwargs)

        return logg

    return decor_logger
