import lz4.block
import os
import glob
import json
import time

# From https://gist.github.com/snorey/3eaa683d43b0e08057a82cf776fd7d83
# Given the path to a "mozlz4", "jsonlz4", "baklz4" etc. file, 
# return the uncompressed text.
def mozlz4_to_text(filepath):
    bytestream = open(filepath, "rb")
    bytestream.read(8)  # skip past the b"mozLz40\0" header
    valid_bytes = bytestream.read()
    text = lz4.block.decompress(valid_bytes)
    return text

def get_firefox_urls():
    recovery_lz4_path = glob.glob(os.path.join(os.getenv('APPDATA'), "Mozilla\\Firefox\\Profiles\\*\\sessionstore-backups\\recovery.jsonlz4"))

    if len(recovery_lz4_path) == 0:
        print('ERROR: Firefox recovery file not found')
        return

    recent_tabs = []

    for profile_path in recovery_lz4_path:
        # Load all tab data for given profile
        tab_data = json.loads(mozlz4_to_text(profile_path))
        for window in tab_data['windows']:
            for tab_entry in window['tabs']:
                # Append url of the tab and the unix time when the tab was last accessed
                recent_tabs.append([tab_entry['entries'][-1]['url'], tab_entry['lastAccessed']])
    # Sort tabs by recency
    recent_tabs = sorted(recent_tabs, key=lambda x: x[1], reverse=True)
    # Remove unix time to only return urls
    recent_tabs = [i[0] for i in recent_tabs]
    
    return recent_tabs

if __name__ == "__main__":
    print(get_firefox_urls())