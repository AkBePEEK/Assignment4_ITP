class BasicPlan(object):
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = "$8.99"


class StandardPlan(BasicPlan):
    can_stream = BasicPlan.can_stream
    can_download = BasicPlan.can_download
    has_SD = BasicPlan.has_SD
    has_HD = True
    has_UHD = True
    num_of_devices = 2
    price = "$12.99"


class PremiumPlan(StandardPlan):
    can_stream = StandardPlan.can_stream
    can_download = StandardPlan.can_download
    has_SD = StandardPlan.has_SD
    has_HD = StandardPlan.has_HD
    has_UHD = StandardPlan.has_UHD
    num_of_devices = 4
    price = "15.99"