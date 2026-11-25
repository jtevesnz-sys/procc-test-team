# PROCC Test Team: Website Check Reference

An early public demonstration of the Test Team's approach to checking a website and reporting evidence. Newly written for this repository, it is inspired by PROCC Test & Validation; it is not the original plugin or a complete testing platform.

The example checks a local HTML file for a non-empty page title, a main landmark, an H1 and image alternative-text attributes. It produces PASS or FAIL for those specific checks. A browser interaction check is explicitly NOT_RUN: inspecting source cannot establish that a button works in a browser.

## Run

Requires Python 3.11 or later, with no additional packages or network access:

```sh
python website_check.py example.html
python -m unittest -v
```

Exit status is 1 when a check fails and 2 when a file cannot be read. The example page is fictional.

## Test Team and Watchtower

The Test Team executes bounded checks and records what happened. Watchtower can independently review the stated criteria and test evidence when an independent reviewer and the necessary evidence are actually available. This example does not run Watchtower or prove independent review occurred.

These checks do not establish full accessibility, browser compatibility, responsive design, security, SEO performance, live website availability or correct form submission. An empty alt attribute can be appropriate for decorative images, and a present attribute does not prove quality. Human review and browser, device and functional testing remain necessary. No license has been selected.
