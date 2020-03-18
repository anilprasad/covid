from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class AgencyContactThrottle(UserRateThrottle):
    scope = 'agency_contact'
    rate = '5/min'


class AccountMessageFlagThrottle(UserRateThrottle):
    scope = 'account_message_flag'
    rate = '20/min'


class AccountBookmarkPropertyThrottle(UserRateThrottle):
    scope = 'account_bookmark_property'
    rate = '10/min'
