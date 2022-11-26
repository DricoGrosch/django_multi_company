def hostname_from_request(request):
    # split on `:` to remove port
    return request.get_host().split(":")[0].lower()

