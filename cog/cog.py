def click(organisation):
    if "locations" in organisation:
        locations = organisation["locations"]
        del organisation["locations"]
    else:
        locations = {}

    for event_title, procedures in organisation.items():
        for procedure in procedures:
            pass
