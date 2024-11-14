# Contributing to Domo's Developer Portal

Welcome to Domo's Developer Portal repository!

If you'd like to contribute to our public docs, then you are in the right place. If you're looking for the Developer Portal itself see https://developer.domo.com/.

Before contributing to the Developer Portal, please ensure you've reviewed the contribution guidelines below.

## Types of Documentation

In general, there are three types of articles in the Developer Portal. Please follow the style guide for each.

1. Guide / How-to Article
2. Tutorial
3. API Reference

## Stoplight

Domo partners with [Stoplight](https://stoplight.io/) to host our [Developer Portal](https://developer.domo.com/). To contribute to this repository, it's useful to understand a few things about how these docs are rendered in the Stoplight portal.

- `assets/` is where any image files that you want to display will live.
- `docs/` includes all guides, tutorials, and API References in the Developer Portal. The former two are markdown `.md` files and the latter is either a markdown `.md` file or an OpenAPI spec `.yaml ` file depending on the API.
- `toc.json` is the configuration file that defines the structure of the left navigation side bar in the Developer Portal.

The [Stoplight Documentation](https://docs.stoplight.io/) is a great resource for learning how to make the most out of the nice functionality Stoplight can unlock. For writing documentation articles like Tutorials or Guides, [Stoplight-flavored Markdown](https://docs.stoplight.io/docs/platform/b591e6d161539-stoplight-flavored-markdown-smd) is a particularly useful reference.

## Raising an Issue

The simplest way to contribute, is to raise a [GitHub issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) in this repository. Issues are great for suggesting ideas, feedback, or requesting particular documentation. Once you've raised an issue, others can follow it for updates and engage in discussion around it.

## Opening a Pull Request

If you are hoping to add documentation to the Developer Portal, please create a new branch with the following naming convention `<section>/<purpose>` where the section corresponds to the section of the developer portal you're adding to (e.g. `data-science`) and the purpose is the reason for requesting a change (e.g. `update-jupyter-examples`).

## Developer Portal Style Guide

Across all resources, it's important to remain consistent. Please follow these brief principles in your contributions.

- Markdown: Please use Markdown syntax `#` rather than HTML `<h1>`.
- Headings: Use h1 (`#`) headings for all article titles. Use h2 (`##`) and h3 (`###`) headings to organize content logically
- Emphasis: Apply bullet points or numbered lists for step-by-step instructions or key points, and emphasize important text using bold or italics sparingly.
- Code: Include code snippets within triple backticks for syntax highlighting, and use inline code formatting for short code references.
- Links: Hyperlink external references with descriptive text.
- Tone: Aim for a helpful and approachable tone, free of jargon unless necessary, while ensuring accessibility best practices are met.

### Guide / How To

Guides are the most common resource in the developer portal. They can range from overview articles, how-to achieve a specific task, or common code snippets and patterns that are useful.

They tend to be shorter and more focused on a single subject than tutorials.

#### Guide Template

1. Start with a brief overview to set context and state the article’s goal clearly.
2. Break down tasks into short, logically ordered steps, using bullet points or numbered lists as necessary. Introduce relevant code snippets with a brief explanation, ensuring they align with best practices.
3. Include tips, warnings, and common pitfalls in callout blocks for clarity.
4. Conclude by summarizing key takeaways or providing links to related resources for further exploration.

#### Examples

[Example Guide - How to Hit Code Engine from an App](docs/Apps/App-Framework/Guides/hitting-code-engine-from-an-app.md)​

### Tutorials

Tutorials are step-by-step, start-to-finish walkthroughs for complete solutions.

These usually have multiple parts, include all code required to build the solution, and explanations for the purpose of each step in the walkthrough. They can (and often do) bridge multiple features / areas of the Domo Product.

#### Tutorial Template

1. Begin with an introduction outlining the goals, prerequisites, and expected outcomes.
2. Divide the tutorial into clearly defined sections or parts, using numbered steps and descriptive headings to guide the user.
3. Provide complete code snippets for each step, with detailed explanations of what each part does and why it’s essential to the solution.
4. Incorporate visuals, such as diagrams or screenshots, to illustrate complex concepts.
5. Summarize key points at the end of each section and conclude the tutorial with a recap and next steps for further exploration or related topics.

#### Examples

[Example Tutorial - Building Dynamic Infographics with Domo and Canva](docs/Apps/App-Framework/Tutorials/Vanilla-Javascript/DynamicInfographic.md)​


### API Reference

API documentation is one of the most critical components to enabling developers to build on Domo.

For convenience we've divided APIs into three categories:

1. App Framework APIs: APIs available within the Domo App context.
2. Platform APIs: APIs that use an OAuth 2.0 authorization and authentication pattern which allows you to define clients with a variety of scopes.
3. Product APIs: APIs that allow you to do anything you can do in the Domo UI. Tokens generated for these APIs provide access to all resources the user has in Domo. These have often been referred to as "undocumented" APIs.

See https://developer.domo.com/portal/8ba9aedad3679-ap-is for more info about the distinction.

<!-- theme: info -->

> #### Undocumented APIs
>
> Note: There is currently a project underway on Esteban's team to annotate APIs so many of the OpenAPI spec / internal Swagger docs can be synced with our public facing developer docs.
>
> In the meantime, we should provide at least minimal documentation for Product APIs.

#### App Framework APIs

Please see the [AI Service Layer API](https://developer.domo.com/portal/wjqiqhsvpadon-ai-service-layer-api) for an example of how to document these endpoints.

Please include:

1. Overview of the service - (including links to relevant guides, examples, etc.)
2. Then, each endpoint should have:

- title: `h2`
- brief description: `plain text`
- code example: `code snippet`
- http request (including query params): `code snippet`
- request body arguments accepted: `table`
- request body example code example: `code snippet`
- http response example: `code snippet`

#### Platform APIs

See (https://developer.domo.com/portal/3b1e3a7d5f420-data-set-api)[DataSet API] for an example.

These APIs are actively testable in the documentation itself. They are all OpenAPI spec `.yaml` files.

#### Product APIs

As noted above, this is where we currently have the largest gap. Eventually, we'll be able to mirror the internal OpenAPI specs, but in the meantime many developers are already building on these APIs and we need to provide more documentation.

At a minimum, we should prioritize documenting the following APIs:

1. All endpoints referenced in Global Code Engine packages.
2. Anything that you, or customers have built scripts on.
