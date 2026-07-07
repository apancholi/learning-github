import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://avlokan-services.com"

# Every page on the site, with a friendly label
PAGES = [
    ("Home", "/index.html"),
    ("About", "/About.html"),
    ("Contact", "/Contact.html"),
    ("Quality Policy", "/Quality%20Policy.html"),
    ("Inspection Services", "/Services/InspectionServices.html"),
    ("Welding Procedure", "/Services/Welding.html"),
    ("Welding Supervision", "/Services/WeldingSupervision.html"),
    ("QA/QC Services", "/Services/QaQcServices.html"),
    ("Coating Consultancy", "/Services/CoatingConsultancy.html"),
]


@pytest.mark.parametrize("label,path", PAGES)
def test_page_loads_successfully(page: Page, label, path):
    response = page.goto(f"{BASE_URL}{path}")
    # Page must respond with success (not 404, 500, etc.)
    assert response.ok, f"{label} returned status {response.status}"
    # Page must actually have a non-empty title, not a blank/broken page
    title = page.title()
    assert len(title) > 0, f"{label} has an empty page title"
