# Contributing to Domo's Developer Portal

Welcome to Domo's Developer Portal repository! 

If you'd like to contribute to our public docs, then you are in the right place. If you're looking for our Developer Portal please see https://developer.domo.com/.


## Stoplight

Domo partners with [Stoplight](https://stoplight.io/) to host our [Developer Portal](https://developer.domo.com/). To contribute to this repository, it's useful to understand a few things about how these docs are rendered in the Stoplight portal.

- `assets/` is where any image files that you want to display with live
- `docs/` include all articles in the Developer Portal. These are all markdown `.md` files.
- `reference/` is where all API reference documentation lives. These are all `.yaml` files that respect the [OpenAPI Specification](https://www.openapis.org/)
- `toc.json` is the configuration file that defines the structure of the left navigation side bar in the Developer Portal.

The [Stoplight Documentation](https://docs.stoplight.io/) is a great resource for learning how to make the most out of the nice functionality Stoplight can unlock. For writing documentation articles like Tutorials or Guides, [Stoplight-flavored Markdown](https://docs.stoplight.io/docs/platform/b591e6d161539-stoplight-flavored-markdown-smd) is a particularly useful reference.

## Raising an Issue
The simplest way to contribute, is to raise a [GitHub issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) in this repository. Issues are great for suggesting ideas, feedback, or requesting particular documentation. Once you've raised an issue, others can follow it for updates and engage in discussion around it.


## Opening a Pull Request

If you are hoping to add documentation to the Developer Portal, please create a new branch with the following naming convention `<section>/<purpose>` where the section corresponds to the section of the developer portal you're adding to (e.g. `data-science`) and the purpose is the reason for requesting a change (e.g. `update-jupyter-examples`).
