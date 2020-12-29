from hashlib import md5


def get_md5(a: any):
    return md5(str(a).encode()).hexdigest()