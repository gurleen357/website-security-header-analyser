import requests  #Calling the requests library so we can send HTTP requests to websites

# List of important security headers to check
required_headers = {
    "Content-Security-Policy": "Helps prevent XSS and data injection attacks.",  #Stops attackers from injecting malicious scripts into a website. Protects against Cross-site scripting, Data injection and malicious external resources
    "Strict-Transport-Security": "Enforces HTTPS and protects against downgrade attacks.",  #Forces the browser to use HTTPS only, never HTTP. Protects against Man-in-the-middle attacks, protocol downgrade attacks and SSL stripping.
    "X-Frame-Options": "Prevents clickjacking attacks.",  #Prevents the site from being loaded inside an <inframe>. Protects against clickjacking attacks
    "X-XSS-Protection": "Provides basic protection against reflected XSS.",  #Enables basic browser level XSS filtering. Protects against reflected XSS attacks
    "Referrer-Policy": "Controls how much referrer info is shared.",  #Controls how much information the browser sends in the referer header. Protects against sensitive data leakage and internal IRL exposure
    "Permissions-Policy": "Restricts powerful browser features (camera, mic, etc)."  #Controls access to powerful browser features. Protects against camera misuse, microphone misuse, geolocation abuse, clipboard access, and fullscreen hijacking
}  #Dictionary of important security headers and a short description of each

def check_security_headers(url):  # Defines a function that checks security headers for a given website URL
    try:  #Starts a try block to safely handle any errors when sending the request
        response = requests.get(url)  # Sends a HTTP GET request to the URL provided by the user
        headers = response.headers  # Stores the response headers from the website in the 'headers' variable

        print(f"\n🔍 Checking security headers for: {url}\n")  #This message is output showing which website is being checked

        for header, description in required_headers.items():  # Loop through each required header and its description
            if header in headers:  # If the header exists  #Checks if the current header exists in the website's response headers
                print(f"✔ {header} — Present")  #Outputs message that this security header is present
            else:  # If the header is missing in the response
                print(f"✘ {header} — MISSING")  #Outputs this message that this security header is missing
                print(f"   ↳ Why it matters: {description}\n")  #Explains why the missing header is important for security

    except requests.exceptions.RequestException as e:  # Catch any request related errors like invalid URL, timeout, no internet.
        print(f"Error: {e}")  #This message is output to let the user know what went wrong

# Main program
url = input("Enter a website URL (e.g., https://example.com): ")  # Ask user for a website URL to analyse
check_security_headers(url)  #Recalls the function to check security headers for the entered URL
