---
stoplight-id: xma9hezmttvid
---

# App Sessions

This guide will provide more technical detail on how sessions work in the App Framework.

### What is Stored in the App Session
---

When an App Platform App is loaded (the `index.html` file is requested), an app session is created. This session is used as authentication and stores any state passed to the app at load time that needs to be available on subsequent requests made by the app to the App Platform APIs.

Information stored in the app session:
- Authentication details (customer, user)
- App execution context (standard, public embed, private embed, oauth)
- Filters (supplied by headers or query parameters like 'pfilters' or 'analyzer', from the embed token, etc)
- App context override (was the app launched referencing a different app context than what its configuration references)

### How Sessions are Created
---

A new app session is created every time the app is loaded and the session ID is injected into the `index.html` file as a window parameter named `__RYUU_SID__` (note that is 2 _ characters at the beginning and the end). It is also written as a session cookie, on the full app domain, named `ryuu_sid`. This session cookie is a convenience so that the app code doesn't need to send the session ID some other way.

<!-- theme: warning -->
> #### Warning
>
> The existence of the session cookie can cause problems if the more than one copy of same app instance is running in a shared context (loaded on multiple browser tabs/windows, multiple copies of the same card on a page, etc). See an example of this scenario at the bottom of the page.
>
> Because of the shared context, the session cookie is shared, and all copies of the app instance will share the same session. If that is a concern, the session ID can be sent in a different way so that the session cookie is not considered.



**The App Platform needs to receive the session ID on all requests from the app.**

There are 3 ways to send the session ID. They are used in the following preference order

1. The `X-Domo-Ryuu-Session` header
2. The `ryuu_sid` query parameter
3. The `ryuu_sid` cookie

Thus if the session ID is sent as the header or the query parameter, the cookie will be ignored.

The code for the app can be written such that the session ID is explicitly added as a header or query parameter. This will work to override the session cookie but can be labor intensive. 

Another option is to use the `domo.js` library. The domo.js library can be included in the app (generally by loading it from the public-assets folder) and then requests that are sent, either as static asset requests or using the functions supplied in `domo.js` (such as `domo.get()`), will be modified to include either the header (on function calls) or the query parameter (static asset requests). See the [`domo.js` documentation here](../Tools/domo.js.md) for more details.

<!-- theme: info -->
> #### Make sure you have the most up-to-date Apps SDK (domo.js)
> If you are seeing any unexpected behavior that may be related to app sessions, try updating the Domo Apps CLI to the most recent version. As Domo has moved away from using cookies, we've updated the domo.js library to automatically include a session token in the header of all requests.


<!-- theme: info -->

> #### Note
>
> There is also a design version flag that can be used to disable the session cookie. In the flags section of the manifest set the flag `'authentication-cookies-disabled'` to `true` and the session cookie will not be set. This can be a good way to test that the app is correctly setting the session ID on requests. When this is enabled, you will get a `403` response on any request that is not.

To set the `authentication-cookies-disabled` flag in your `manifest.json` file, you can use code like the following:

```json
{
  "name": "My Sweet App",
  "version": "1.0.1",
  "flags": {
    "authentication-cookies-disabed": true,
  }
}
```

### Shared Session Example
---

Let's say you have an app that just displays the data in a dataset. 

The app has a button that sends the request to query the data and display it. You open 2 browser tabs and navigate to the same app in both tabs. In tab 1 you set page filters such that the dataset is filtered to rows where the column 'State' has the value 'UT'. Verify that the data is correctly filtered. 

Then in tab 2 you set the page filters to filter to the value 'TX' in the 'State' column. Verify that the data is correctly filtered. 

Now if you return to tab 1 and, without refreshing the app, click the button to query the data, it will show data filtered to 'TX' rather than 'UT'