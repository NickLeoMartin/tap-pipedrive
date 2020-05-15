from tap_pipedrive.streams.recents import RecentsStream


class RecentUsersStream(RecentsStream):
    items = 'user'
    schema = 'users'
    key_properties = ['id',  'name', 'default_currency',
                      'locale', 'email', 'phone', 'created',
                      'modified', 'lang', 'active_flag', 'is_admin',
                      'signup_flow_variation', 'has_created_company',
                      'role_id', 'activated', 'timezone_name',
                      'timezone_offset', 'icon_url', 'is_you']
    # state_field = 'modified'

    def process_row(self, row):
        return row['data'][0]
