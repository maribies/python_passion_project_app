# TODO: The base site url should always come from the business.
# In future, with a flag --all, get and update all designers by business.


def get_url(business):
    # TODO: If business site has multiple designers,
    # will need to understand how to append/change url accordingly.
    if len(business["designers"]) == 1:
        return business["site_url"]


def main(business, designer):
    url = get_url(business)

    Designer = {"name": designer, "site_url": url}

    return Designer
