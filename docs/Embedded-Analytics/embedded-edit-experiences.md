---
stoplight-id: ed061f0c295c0
---

# Embedded Capabilities

Provide more functionality to your external customers by empowering them to create, edit, save, and share their own content from the embedded experience.

The most advanced companies integrate the full power of the platform. Domo Everywhere allows you to share the rich data experience of the entire Domo platform -- any data, application, or visualization -- packaged together for your customers and partners that aligns with your brand and while maintaining the ability to easily govern and distribute at scale. You decide what tools and capabilities to enable. Start with the majority of your functionality already built so you can focus on your expertise.


https://player.vimeo.com/video/530952420?badge=0&amp;autopause=0&amp;player_id=0&amp


Your most strategic customers and partners demand more than dashboards. OEM all of Domo in your interface so your partners and customers can:
<ul>
 	<li>Create totally new content</li>
 	<li>Create their own alerts</li>
 	<li>Schedule their own reports</li>
 	<li>Connect their own data</li>
 	<li>Transform both sides together</li>
</ul>

## Domo Identity Broker
---
### What does the Domo Identity Broker do?
The Domo Identity Broker allows you to have one entity they can authenticate users against. The Identity Broker will then route that user to the appropriate Domo environment and authenticate them as a user. The identity broker can accept a variety of different authentication methods to make it easy for our customer to leverage their existing infrastructure. See basic architecture diagram below.

<img class="alignnone" src="https://web-assets.domo.com/blog/wp-content/uploads/2021/06/domo-identity-broker-3.png" alt=""/>

#### Supported Technologies
The Domo Identity Broker supports SAML2, OIDC, JWT or OAuth2.


### Configuration and Deployment Steps
Reach out to your CSM and be prepared to supply the following information:
<ul>
 	<li>URL to your Domo instance</li>
 	<li>Desired authentication mechanism(s): SAML2, OIDC, JWT or OAuth2</li>
 	<li>Attribute that will be used to route a user to an end customer account</li>
 	<li>Mappings of attributes to end customer accounts</li>
</ul>
&nbsp;

Once you’ve submitted that information, you will receive the following items:
<ul>
 	<li>URL of the Identity Broker</li>
 	<li>A cert used by the Domo End Customer Accounts to accept SAML assertions from the Domo Identity Broker</li>
 	<li>A secret that needs to be used to sign the JWT</li>
</ul>
&nbsp;

Configuration of the initial End Customer Account:
<ul>
 	<li>The End Customer Account needs to have SSO configured to allow the Domo Identity Broker to serve as the IDP for that environment</li>
 	<li>Navigate to the instance -&gt; Admin -&gt; Security -&gt; SSO -&gt; Manual Configuration</li>
 	<li>Identity provider endpoint URL is the URL for the Identity Broker</li>
 	<li>Entity ID is the URL for the Identity Broker</li>
 	<li>Please upload the provided certificate.</li>
 	<li>Ensure you select the “Use SAML Relay State to redirect” box.</li>
</ul>
<img src="https://web-assets.domo.com/blog/wp-content/uploads/2021/08/Picture1-2.png" width="1952" height="2130" class="alignnone size-full" />


#### Authenticating using a JWT (JSON Web Token)
JWT’s can be sent to the Domo Identity Broker as a GET parameter (in the URL) or a POST parameter (in the post body). A quick way for validation is to send a URL parameter to the Identity Broker URL, followed by /JWT?token={{token}}. You can also pass a destination parameter in the URL, which will determine which page is loaded (assuming you want to load something beyond the default landing page). Example: <strong>https://modocorp-idp.domo.com/jwt?token={{token}}&amp;destination=/page/{{page_ID}}</strong>

The minimum items required in the payload are:
<ul>
 	<li>Sub (email address)</li>
 	<li>User attribute key (lookup to tie the user to an end customer account)</li>
 	<li>Exp (JWT expiration in EPOCH time)</li>
  <li>JTI (Unique string to identify this JWT. Recommended to use a UUID.)</li>
</ul>
In addition to the required items you can also include the following option attributes which can be used by Domo. These can be used in dynamic PDP policies, for group assignments and to complete the users profile within Domo:

<ul>
 	<li>Alternate email – a secondary contact email for the user.</li>
 	<li>Role – The role of the user at each login. The role must match exactly a valid role in the Domo instance.</li>
 	<li>Employee ID – Must be alphanumeric</li>
 	<li>Hire Date – Format: YYYY-MM-DD</li>
 	<li>Title – Example: Retail Team Lead</li>
 	<li>Department – Example: Sales</li>
 	<li>Location – Example: Salt Lake City, UT</li>
 	<li>Mobile phone – Accepts any combination of numbers and the characters +()-x. For example: +1 (555) 555-5555 x 5555</li>
 	<li>Desk phone – Accepts any combination of numbers and the characters +()-x. For example: +1 (555) 555-5555 x 5555</li>
 	<li>Locale – Sets the preferred language, metrics and formatting in Domo. Valid values include: de-DE, de-AT, de-CH, en-AU, en-CA, en-150, en-HK, en-IE, en-IL, en-MO, en-NZ, en-SG, en-GB, en-US, en-001, es-419, es-ES, es-US, es-MX, fr-BE, fr-CA, fr-FR, fr-CH, ja-JP, zh-CN, zh-Hans-HK, zh-Hans-MO, zh-Hans-SG</li>
 	<li>Timezone – For example: America/Denver or Asia/Tokyo. For a full list of valid timezone settings, see this article: <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank" rel="noopener">timezones</a></li>
 	<li>Group – A list of XML escaped strings</li>
</ul>
</li>
</ul>
The payload must signed using the provided secret and be encoded using an HS algorithm (we encourage HS256). A great site for learning more about JWT’s, creating them for testing purposes and finding access to different code repositories for creating and signing JWT’s is <a href="http://jwt.io" target="_blank" rel="noopener">jwt.io</a>.

Sample JWT payload:

```json
{
  "sub": "alex.lee@modocorp.co",
  "name": "Alex Lee",
  "customer_id": 1000,
  “groups”: [“a”,”b”,”c”],
  "exp": 1716239022
}
```

#### Authenticating using SAML2
When using SAML2 to authenticate against the Domo Identity Broker the following details are required for configuration of the IDP:
<ul>
 	<li>SAML Assertion Endpoint URL: {{identitybrokerURL}}/auth/saml</li>
</ul>
Once the configuration is completed in the IDP, you need to provide your technical resource at Domo with the following details from your IDP:
<ul>
 	<li>Identity Provider Endpoint URL</li>
 	<li>Entity ID</li>
 	<li>X.509 certificate</li>
</ul>

### Managing Instance Mapping
There are two ways to manage instance mappings in the Identity Broker:

1. Webform Dataset within the Main Instance
- Update the Dataset: If your mappings are managed through a Domo webform dataset within your main instance, you can create a support ticket to restart the mapping. This allows the changes made to the webform dataset to take effect in the Identity Broker.

2. Excel Sheet Managed by Engineering:
- Engineering Control: Alternatively, if your mappings are maintained in an Excel sheet managed by engineering, you will need to contact support and provide the new instances and their corresponding IDs. Engineering will manually update the mappings for you.

Both methods mentioned above require a support ticket to restart the mapping process and ensure that the changes made in the webform dataset or Excel sheet take effect within the Identity Broker.


## Next Steps
---
For more information also see the [Domo Knowledge Base](https://domo-support.domo.com/s/topic/0TO5w000000ZanbGAC/domo-everywhere?language=en_US). In particular, this article on [Routing, Creation, and Mapping](https://domo-support.domo.com/s/article/6523741250455?language=en_US) may be helpful.

