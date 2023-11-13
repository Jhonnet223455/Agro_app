def total_order(request):
    total = 0
    if request.session["cart"]:
        for key, value in request.session["cart"].items():
            total += value["accumulated"]

    return total