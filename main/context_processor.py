def total_order(request):
    total = 0
    if "cart" in request.session.keys():
        for key, value in request.session["cart"].items():
            total += float(value["accumulated"])

    return {
        'total_order': total   
    }