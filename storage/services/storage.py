from storage.models import StickersStorage


def creation_context():
    """
     Формування контексту
     """
    storages = StickersStorage.objects.select_related('stickers_main').all()

    formatting_quantity(storages)

    context = {
        "storages": storages,
    }
    return context


def formatting_quantity(storages):
    """
    Форматуємо кількість так, щоб
    500шт -> 5 шт по 100
    75шт -> 1.5Шт по 50
    """
    for pack in storages:
        quantity_dima = pack.quantity_dima
        quantity_vlad = pack.quantity_vlad

        quantity_in_pack = pack.stickers_main.quantity_in_pack

        if quantity_dima % quantity_in_pack == 0:
            pack.quantity_dima = int(quantity_dima / quantity_in_pack)
        else:
            pack.quantity_dima = quantity_dima / quantity_in_pack

        if quantity_vlad % quantity_in_pack == 0:
            pack.quantity_vlad = int(quantity_vlad / quantity_in_pack)
        else:
            pack.quantity_vlad = quantity_vlad / quantity_in_pack