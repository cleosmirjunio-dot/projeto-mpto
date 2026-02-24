from github_report.src.report_service import ReportService
from github_report.src.repository import Repository


def test_total_repositories():
    repos = [
        Repository(
            id=1,
            name="repo1",
            full_name="user/repo1",
            html_url="http://example.com",
            stargazers_count=10,
            forks_count=5,
            language="Python",
            updated_at="2024-01-01T00:00:00Z",
            open_issues_count=1
        ),
        Repository(
            id=2,
            name="repo2",
            full_name="user/repo2",
            html_url="http://example.com",
            stargazers_count=5,
            forks_count=2,
            language="Python",
            updated_at="2024-01-02T00:00:00Z",
            open_issues_count=0
        ),
    ]

    service = ReportService(repos)

    assert service.total_repositories() == 2
    assert service.total_stars() == 15