import time
import requests

ZAP_API_URL = "http://localhost:8080"
TARGET_URL = "http://localhost:5000"

def start_scan(api_url, target_url):
    # Start a new scan
    spider_url = f"{api_url}/JSON/spider/action/scan/"
    params = {"url": target_url}
    response = requests.get(spider_url, params=params)
    if response.status_code == 200:
        print("Spider scan started.")
        scan_id = response.json().get("scan")
        return scan_id
    else:
        print(f"Error starting spider scan: {response.status_code}")
        print(response.text)
        return None

def check_scan_status(api_url, scan_id):
    # Check scan status
    scan_status_url = f"{api_url}/JSON/spider/view/status/"
    params = {"scanId": scan_id}
    while True:
        response = requests.get(scan_status_url, params=params)
        if response.status_code == 200:
            status = int(response.json().get("status"))
            print(f"Scan progress: {status}%")
            if status == 100:
                print("Spider scan completed.")
                break
        else:
            print(f"Error checking scan status: {response.status_code}")
            print(response.text)
            break
        time.sleep(5)

def generate_report(api_url, report_path):
    # Generate the report
    report_url = f"{api_url}/OTHER/core/other/htmlreport/"
    response = requests.get(report_url)
    if response.status_code == 200:
        with open(report_path, "w") as f:
            f.write(response.text)
        print(f"Report generated: {report_path}")
    else:
        print(f"Error generating report: {response.status_code}")
        print(response.text)

def main():
    print("Starting OWASP ZAP scan...")
    scan_id = start_scan(ZAP_API_URL, TARGET_URL)
    if scan_id:
        check_scan_status(ZAP_API_URL, scan_id)
        report_path = "reports/zap/zap_report.html"
        generate_report(ZAP_API_URL, report_path)
    else:
        print("Scan could not be started.")

if __name__ == "__main__":
    main()
