import requests

def get_job_listings():
    url = "https://remoteok.io/api"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an error if the request fails
        jobs = response.json()[1:]  # First item is metadata, remove it

        return [{"title": job.get("position", "N/A"), "company": job.get("company", "N/A")} for job in jobs]

    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch jobs: {e}"}

if __name__ == "__main__":
    jobs = get_job_listings()
    print(jobs)
