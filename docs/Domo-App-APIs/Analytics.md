---
stoplight-id: 
---

# Analytics API

Instructions for tracking user interactions and application events within a Domo app or brick. These functions send HTTP requests to a predefined analytics endpoint (/domo/analytics/v1), logging events such as filter changes, application loads, page views, or any user interaction. This enables real-time tracking of user behavior and app usage, which can help enhance the user experience and provide valuable data insights.

Each function makes use of the fetch API to send asynchronous POST requests, passing an authentication token (__RYUU_AUTHENTICATION_TOKEN__) in the headers to authorize the requests. The functions are designed to be easily integrated into the application’s codebase, with simple, clearly defined parameters for each type of event.
<!-- theme: info -->



### Uploading a file

Report a Page View

#### Code Example
```js
/**
 * Sends a request to log a page view event.
 * 
 * Use this function to report each time a user views a new page within the app.
 * 
 * @param {string} page - The identifier or name of the page that was viewed.
 * @returns {Promise<void>} Resolves when the request completes. Errors if the network request fails.
 *
 * @example
 * // Report that the "Home" page was viewed
 * reportPageView("Home");
 */
export const reportPageView = function(page) {
  return fetch(`/domo/analytics/v1`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-DOMO-Ryuu-Token': token,
    },
    body: JSON.stringify({
      type: 'NAVIGATION',
      properties: {
        pageViewed: page,
      },
    }),
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
  })
  .catch(error => {
    console.error('Failed to report page view:', error);
  });
};
```
