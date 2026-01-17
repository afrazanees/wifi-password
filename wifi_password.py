"""
WiFi Password Retriever
Retrieves all saved WiFi passwords from the local Windows system
"""

import subprocess
import re
import sys


def get_wifi_profiles():
    """Get all WiFi profiles stored on the system"""
    try:
        # Run netsh command to get all WiFi profiles
        profiles_data = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profiles'],
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Extract profile names using regex
        profile_names = re.findall(r'All User Profile\s*:\s*(.*)', profiles_data)
        return [name.strip() for name in profile_names]
    
    except subprocess.CalledProcessError as e:
        print(f"Error: Unable to retrieve WiFi profiles. {e}")
        return []
    except FileNotFoundError:
        print("Error: netsh command not found. This tool only works on Windows.")
        return []


def get_wifi_password(profile_name):
    """Get the password for a specific WiFi profile"""
    try:
        # Run netsh command to get profile details
        profile_data = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear'],
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Extract password using regex
        password_match = re.search(r'Key Content\s*:\s*(.*)', profile_data)
        
        if password_match:
            return password_match.group(1).strip()
        else:
            return None
    
    except subprocess.CalledProcessError:
        return None


def display_wifi_passwords():
    """Main function to display all WiFi passwords"""
    print("=" * 60)
    print("WiFi Password Retriever - Local Passwords Only")
    print("=" * 60)
    print()
    
    profiles = get_wifi_profiles()
    
    if not profiles:
        print("No WiFi profiles found.")
        return
    
    print(f"Found {len(profiles)} WiFi profile(s)\n")
    
    results = []
    for profile in profiles:
        password = get_wifi_password(profile)
        results.append((profile, password))
    
    # Display results in a formatted table
    print(f"{'Profile Name':<40} {'Password':<20}")
    print("-" * 60)
    
    for profile, password in results:
        if password:
            print(f"{profile:<40} {password:<20}")
        else:
            print(f"{profile:<40} {'[No password/Open]':<20}")
    
    print()
    print("=" * 60)


def export_to_file(filename="wifi_passwords.txt"):
    """Export WiFi passwords to a text file"""
    profiles = get_wifi_profiles()
    
    if not profiles:
        print("No WiFi profiles found.")
        return
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("WiFi Passwords - Local System\n")
        f.write("=" * 60 + "\n\n")
        
        for profile in profiles:
            password = get_wifi_password(profile)
            f.write(f"Profile: {profile}\n")
            if password:
                f.write(f"Password: {password}\n")
            else:
                f.write(f"Password: [No password/Open]\n")
            f.write("\n")
    
    print(f"Passwords exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--export":
        export_to_file()
    else:
        display_wifi_passwords()
