---
stoplight-id: wbwvwmq9rd714
---

# Filtering Options

All these filter types are layered in the sequence below:

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions1.png" />


## SECURE POLICIES

<h3><strong>Personalized Data Permissions (PDP) </strong></h3>

<strong>Documentation:</strong> <a href="https://domohelp.domo.com/hc/en-us/articles/360042934614-Creating-and-Deleting-PDP-Policies" rel="noopener" target="_blank">Creating and Deleting PDP Policies</a>

<strong>Definition:</strong> Outdated SSO integration reliant upon cookies for individual accounts for each viewer

<strong>Use case:</strong> Forced row-level security defined in the Domo interface that cannot be seen nor edited by viewers 	

<strong>Warning:</strong> Browsers are expanding their 3rd party cookie blocks. The best practice is to use Programmatic Filters instead of PDP to [stay future-proof](52ozpgfra3lsd-embedded-analytics-in-a-world-without-cookies). 

<strong>Note: </strong>If this older method must absolutely be used for personalization, protect yourself from embed viewers tracing the iframe back to the instance and seeing extra cards and pages beyond the embedded content. This is done by creating a dedicated instance for external use cases, applying the Whitelabel V1 template of feature switches, and embedding from there instead of your main internal instance. 

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions2.png" />


<h3><strong>Server-side Programmatic Filters </strong></h3>

<strong>Documentation:</strong> [Programmatic Filtering](1yafxad1u8azv-programmatic-filtering)

<strong>Definition:</strong> Newer SSO integration with cookie-less auth through a single service account for all viewers 

<strong>Use case:</strong> Forced row-level security defined in server side code that cannot be seen nor edited by viewers

<strong>Warning:</strong> This will shift contracts from user/viewer pricing to impression/view pricing since a single service account acts as proxy for all viewers.

<strong>Note:</strong> No dedicated external instance is required for this approach since the viewers will not have access to the client ID and secret of the service account. Therefore, they cannot trace the iframe and gain access to the Domo instance.

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions3.png" class="alignnone size-full" />

## CLIENT-SIDE PARAMS 

<h3><strong>JS API Filters </strong></h3>

<strong>Documentation:</strong> <a href="https://github.com/domoinc/domo-node-embed-filters/blob/master/public/jsapi.js" rel="noopener" target="_blank">JS API Sample Code Repo </a>
<ul>
	<li>Outputs: The JS API listens for click events on the embedded content and passes them back up to the host page for cross-system links and interaction analytics. </li>
	<li>Inputs: The JS API also completes the bidirectional passing of context by letting the host page push filters down into the embedded content </li>
	<li>Controls: The code above can be triggered by any external menu in the host page </li>
</ul>

<strong>Events:</strong> currently the following events are supported.

<table>
	<tr>
		<th>Event</th>
		<th>Type</th>
		<th>Description</th>
		<th>Message</th>
		<th>Support</th>
	</tr>
	<tr>
		<td>/v1/onFrameSizeChange</td>
		<td>Output</td>
		<td>Event communicating the content size of the embed asset. Use when wanting to make sure the iframe is the exact size of the content so no scroll bars appear. </td>
		<td></td>
		<td>App Studio,<br> Dashboard,<br> Card</td>
	</tr>
	<tr>
		<td>/v1/onFiltersChange</td>
		<td>Output</td>
		<td>Event communicating filter changes</td>
		<td></td>
		<td>App Studio,<br> Dashboard,<br> Card</td>
	</tr>
	<tr>
		<td>/v1/onAppData</td>
		<td>Output</td>
		<td>Event communicating "appData" between an app in an embedded asset and the embedding website</td>
		<td></td>
		<td>App Studio,<br> Dashboard,<br> Card</td>
	</tr>
	<tr>
		<td>/v1/onAppReady</td>
		<td>Output</td>
		<td>Event communicated by App Studio app to indicate the app finished loading</td>
		<td></td>
		<td>App Studio</td>
	</tr>
	<tr>
		<td>/v1/filters/apply</td>
		<td>Input</td>
		<td>Event to communicate filters for an asset to apply</td>
		<td>{<br>
	                id: 'setFilters123',<br>
        		jsonrpc: '2.0',<br>
        		method: '/v1/filters/apply',<br>
        		params: {<br>
        			filters: [{'column': 'name', 'operand': 'IN', 'values': ['ABC']}]<br>
                	}<br>
		}</td>
		<td>App Studio,<br> Dashboard,<br> Card</td>
	</tr>
	<tr>
		<td>/v1/appData/apply</td>
		<td>Input</td>
		<td>Event to communicate "appData" to an app within the embed asset</td>
		<td>{ <br>
			id: 'appData',<br>
			jsonrpc: '2.0',<br>
			method: '/v1/appData/apply',<br>
			params: {<br>
 				appData: appData <br>
			}<br>
		}</td>
		<td>App Studio</td>
	</tr>
</table>

<strong>Example</strong>

Here are some <a href="https://github.com/STEEZENS/domo-pfilters" rel="noopener" target="_blank">examples</a> of external drop-down filter controls we used while building <a href="https://www.domo.com/covid19/daily-pulse/" rel="noopener" target="_blank">Domo’s COVID-19 Tracker</a>:  

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions4.png" />

<strong>Definition:</strong> Client-side approach here contrasts from server-side approach above because these are meant to be visible and editable for viewers. The filters applied via the embed API through event ports and listeners.  

<strong>Use case:</strong> Newer approach to applying external filter controls from the host page (like drop down menus outside of the iframe). Changes can be applied faster to multiple pieces of embedded content <strong><em>without forcing iframe refresh</em></strong>. Also supports bidirectional context passing (where click events on the embedded content can also be passed back to the home page for cross-iframe or cross-page drills, links, and interactions.) 

<strong>Warning:</strong> JS API (here) and Pfilters (below) are not a secure replacement for Programmatic Filters because the client-side parameters can be seen and changed by viewers by either glancing at the URL or inspecting the content. These should only be used for filters that aid exploration. 

<strong>Note:</strong> The <strong><em>main pre-requisite</em></strong> is population of the “Embed Authorized Domains” whitelist. This whitelist drives a CSP (content security policy) which ensures these bidirectional signals are only sent in ports for sites you approve:

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions5.png" />

The demo video below shows how the events are displayed with specific references even if multiple iframes are included in the same page: 

https://player.vimeo.com/video/515861680

<h3><strong>Pfilter URL parameters </strong></h3>
 
[Using Pfilters to Apply Filters from URL Query Parameters to Embedded Dashboards](url-parameters-in-embedded-content.md#pfilters)

<strong>Definition:</strong> Simpler setup in URL params instead of client side code like JS API filters. However, pfilters are slightly <strong><em>slower because they force an iframe</em></strong> refresh to apply the filter logic. They use the same filter pattern (column, operand, value) as client-side JS API and server-side Programmatic Filters. 

<strong>Use Case:</strong> Older approach to applying external filter controls. 
 
<strong>Warning:</strong> Pfilters and the JS API are not a secure replacement for Programmatic Filters because the client-side parameters can be seen and changed by viewers by either glancing at the URL or inspecting the content. These should only be used for filters that aid exploration. 

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions7.png"/>

<h3><strong>Additional App Studio URL parameter </strong></h3>

<strong>Definition:</strong> For additional control over an embedded App Studio app, the URL param <em>overrideFilters</em> can be added to provide more control over whether an app should load up its saved default filters. When <em>overrideFilters=true</em>, the App Studio app will not load up any filters, instead, it will wait for a filter event from the parent before loading filters. When <em>overrideFilters=false</em> or when not provided, the filters saved to the default filter view of an App Studio app will load.

<strong>Use Case:</strong> If you are actively applying filters to an embedded App Studio app, this parameter will help prevent getting in a mixed filtered state where the nested app may load up its own and get out of sync with the parent OR change the intended filters meant to be passed to the app.

<strong>Warning:</strong> If setting <em>overrideFilters=true</em>, filters will not load up <strong>UNTIL</strong> the parent communicates a filter state using the <em>/v1/filters/apply</em> event. Even if it is an empty filter state, the parent must communicate it to the embedded App Studio App.

## DOMO INTERACTIONS


<h3><strong>Page filters</strong></h3> 
(and named filter views) 

<strong>Documentation:</strong> <a href="https://domohelp.domo.com/hc/en-us/articles/360042923914-Applying-Page-Level-Filters-with-Filter-Views-BETA-" rel="noopener" target="_blank">Applying Page-Level Filters (with_Filter_Views) </a>

<strong>Definition:</strong> Top filter bar of embedded cards and dashboards similar to what is available in the full Domo instance  

<strong>Use Case:</strong> Ad hoc filter creation by the user when the creator does not know all the slices the viewer might want to explore 

<strong>Warning:</strong> Page filters are available in dashboard embed, but saved filter views are still in beta so they are not targeted for support in dashboard embed until later in 2021. 

<strong>Note:</strong> As emphasized in the layer sequence above, these lower priority filters can only return results within the subset of rows made available by PDP or Programmatic Filters. 

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions8.png" />

<h3><strong>Interaction filters across cards</strong></h3>
 
<strong>Documentation:</strong> <a href="https://domohelp.domo.com/hc/en-us/articles/360042923914-Applying-Page-Level-Filters-with-Filter-Views-BETA-#Applying_Card-to-Card_Filters" rel="noopener" target="_blank">Applying Card-to-Card Filters  </a>

<strong>Definition:</strong> Slicer cards similar to the cross-card interactions available in the full Domo instance 

<strong>Use Case:</strong> These are the simplest filter interaction for viewers. They are ideal when the content creator already knows the filters will want 

<strong>Note:</strong> As emphasized in the layer sequence above, these lower priority filters can only return results within the subset of rows made available by PDP or Programmatic Filters 

<img src="https://web-assets.domo.com/blog/wp-content/uploads/2022/08/FilteringOptions9.png" />
